from secret import *
import random

def main(): #TODO
    """
        The main script for the bot
    """
    pass

def select_random_tweet(filename):
    """
    Loads possible tweets from the specified filename and returns a random tweet as a string.
    Params:
        filename - string of filename without extension. file must be .txt and have 1 tweet per line
    """
    file=open(filename+".txt","r")
    list_of_tweets=[]
    for line in file:
        list_of_tweets.append(str(line))
    tweet = list_of_tweets[random.choice(range(len(list_of_tweets)))][:-1]
    print(tweet)
    return tweet