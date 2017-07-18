from django.db import models

# Create your models here.

class Tweet(models.Model):
	tweet_id = models.IntegerField(default=0)
	tweet_text = models.CharField(max_length=140)
	pub_date = models.DateTimeField('date tweeted')
