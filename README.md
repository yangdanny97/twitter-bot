# twitter-bot
compliment generating bot for twitter - sporadically testing @NiceBot_Reboot

Inspired by the original @TheNiceBot, which was deactivated in 2016. We scraped the set of 241 unique compliments that it gave, and wrote a bot that has the exact same functionality as the original. Users can request a compliment by mentioning @NiceBot_Reboot, and the bot will also compliment a random user at a set interval. The bot is currently undergoing live testing before deploying to production.

Dependencies needed:
- python 3.5
- tweepy

The bot script (nicebot.py) can be run once to reply to any new mentions and give one random compliment to a random user.
For production, this will be deployed on Heroku and set to run at every 5 minutes with cron.

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

Future Ideas:
- original compliment generation (essentially porting over the markov chain from Proton, my Alexa compliment bot)
- automated DM responses



Current Progress:
8/4 Bot complete and livetested twice on 7/30 and 7/31, future plans - few bugfixes and live tests, then a deployment on Heroku

