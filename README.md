# twitter-bot
compliment generating bot for twitter - WIP

Dependencies needed:
- Django
- Celery
- psql??? (not sure if we need a database)

Steps:
1. Make a Django project, set up bot's twitter account
2. Write code to interact with twitter API
3. Write and test code to generate compliments
4. Integrate 2 and 3
5. Test locally with bot account(private) and second test account
6. Deploy and test on heroku

Twitter related documentation to read:
- authentication
- GET statuses/mentions_timeline
- POST statuses/update
- Tweet objects
- working with timelines
- Twitter ID

Todo:
discuss server design/necessity of a database, discuss tweet generation method
