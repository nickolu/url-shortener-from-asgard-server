# URL Shortener From Asgard

Rest API for URL Shortener from Asgard

This is a demo project. With this you can both shorten a URL and harness the power of norse mythology.

Everything built using python 3. You may have to replace some commands with `python` or `python3` depending on how your environment is set up and what your python PATH looks like.

## Info

This app just serves the rest endpoints. See app.py for available endpoints.

To run this you need to have mongo running on port 27017 with the database set up.

If you _really_ want to get this working, set up your mongo and get it running, then create a db called 'urlShortenerFromAsgard'

In that db, create the following collections:
`available_words_for_source`
`url_pairs`
`users`

Then, in the collection available_words_for_source, create one dictionary with the following:

```
{
    source: 'asgard',
    available_words: ['any', 'number', 'of', 'strings', 'here']
}
```

After doing that, activate the virtual environment:

`source venv/bin/activate`

Install dependencies

`pip install -r requirements.txt`

Then, start the app:

`make run`

Run tests:

`make test`

should work `¯\_(ツ)_/¯`
