# URL Shortener From Asgard

Rest API for URL Shortener from Asgard

This is a demo project. With this you can both shorten a URL and harness the power of norse mythology.


## Info

To run this you need to have mongo running on port 27017 with the database set up.

Am I going to create a database migration script so you know what to put in there? I totally would IRL, so just imagine that I have. But I'm out of time now and that wasn't a top priority.

In the mean time, if you _really_ want to get this working, set up your mongo and get it running, then create a db called 'urlShortenerFromAsgard'

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

should work `¯\_(ツ)_/¯`

After doing that, activate the virtual environment:

`source venv/bin/activate`

Then, start the app:

`make run`

Run tests:

`make test`
