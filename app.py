from flask import Flask
from entities.url_pair import UrlPair
from entities.user import User
from data_mappers.configure_registry import configure_data_mapper_registry

app = Flask(__name__)

configure_data_mapper_registry()


@app.route("/")
def hello_world():
    return "Hello, world"


@app.route("/new-url-pair")
def new_url_pair():
    test_user = User()
    url_pair = UrlPair.create_new("test-long-url")
    short_url = url_pair._document["short_url"]
    long_url = url_pair._document["long_url"]
    message = "short url: http://127.0.0.1/{} <br /> \
    long url: {}".format(
        short_url, long_url
    )

    print(url_pair)
    return message

