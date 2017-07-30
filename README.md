# twitter-bot
compliment generating bot for twitter - WIP

Dependencies needed:
- python 3.5
- tweepy

Steps:
1. Set up bot's twitter account and get dev keys for twitter API
2. Write code to interact with twitter API, write cron scripts to run at regular intervals
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

Crontab notes:
- crontab -e to edit crontab file
- crontab -l to view current crontab
- use "#" to comment out lines in crontab file
- In the crontab file, add:
	- SHELL=/bin/bash
	- PATH=(whatever your path is when you type "env" in terminal)
	- * * * * * cd ~/PathToRepo/twitter-bot/src; python nicebot.py >> ~/PathToRepo/twitter-bot/out/out.txt 2>&1

Other notes:
- scraper.py is a script reused from the Proton Compliment Bot project, it is used as a helper to collect the old TheNiceBot's tweets
- secret.py with API_KEY, API_SECRET, ACCESS_TOKEN, and ACCESS_SECRET are required for this to run, it is not provided in the repo since it's connected to our dev account

To do:
 - select random user to tweet at