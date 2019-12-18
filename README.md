# URL Shortener From Asgard

Rest API for URL Shortener from Asgard

This is a demo project. The world probably expected me to generate a string of n random characters to use for the shortened URLs. I say, why do that when bit.ly exists and so many other services. Its not hard to do so don't judge me for not doing it. I did something vastly more cool, however less useful. With my app, you can harness the power of the Norse gods, can bit.ly do that? I don't think so.

Let this also be a lesson in vague requirements.

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
