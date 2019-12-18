from flask import Flask, redirect, request, url_for

from flask_cors import CORS
from url_shortener_from_asgard.data_mappers.configure_registry import (
    configure_data_mapper_registry,
)
from url_shortener_from_asgard.entities.url_pair import (
    UrlPair,
    get_url_pair_by_long_url,
    get_url_pair_by_short_url,
)
from url_shortener_from_asgard.entities.user import User
from url_shortener_from_asgard.entities.available_words_for_source import (
    AvailableWordsForSource,
)

app = Flask(__name__)
CORS(app)
configure_data_mapper_registry()


@app.route("/create-shortened-url")
def new_url_pair():
    original_url = request.args.get("original_url")
    user_id = request.args.get("user_id")
    url_pair = get_url_pair_by_long_url(original_url)
    user = User.get_by_id(user_id)

    if not url_pair:
        url_pair = UrlPair.create_new(original_url, user)

    short_url = url_pair._document["short_url"]
    long_url = url_pair._document["long_url"]

    return {"longUrl": long_url, "shortUrl": short_url}


@app.route("/create-user")
def create_user():
    user = User.create_new()

    return {
        "userId": user.id,
        "message": "user {} successfully created".format(user.id),
    }


@app.route("/get-all-urls-for-user")
def get_all_urls_for_user():
    user_id = request.args.get("user_id")
    url_pairs = UrlPair.get_url_pairs_by_user(user_id)
    url_pairs_json_response = [
        [url_pair["short_url"], url_pair["long_url"], url_pair["times_accessed"]]
        for url_pair in url_pairs.collection.find()
    ]

    return {"userId": user_id, "savedUrls": url_pairs_json_response}


@app.route("/get-remaining-asgardian-words-count")
def get_remaining_available_words_count():
    return {"remaining": AvailableWordsForSource.get_remaining_asgardian_words_count()}


@app.route("/<short_url>")
def dynamic_redirect(short_url):
    url_pair = get_url_pair_by_short_url(short_url)

    if not url_pair:
        message = "no url registered for /{}".format(short_url)
        return error_response(message, 404)

    if url_pair.is_max_access_limit_reached:
        message = "/{} has been accessed the max number of times".format(short_url)
        return error_response(message, 400)

    try:
        redirect_destination = url_pair.access_url()
        return redirect(redirect_destination)
    except Exception:
        raise


def error_response(message, status):
    return {"error": {"message": message, "status": status}}
