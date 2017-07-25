from secret import *
import random, tweepy, time

def main(): #WIP
    """
        The main script for the bot
        currently for testing, it tweets a random compliment at @yangdanny97
    """
    #Authentication
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
    except:
        print("Error. Authenticaton failed")

    #Update status
    random_compliment = select_random_tweet("tweets.txt")
    tweet = "@yangdanny97 "+random_compliment+" #NiceBot"
    api.update_status(tweet)
    print("Status update complete")

def select_random_tweet(filename):
    """
    Loads possible tweets from the specified filename and returns a random tweet as a string.
    Params:
        filename - string of filename, file must have 1 tweet per line
    """
    file=open(filename,"r")
    list_of_tweets=[]
    for line in file:
        list_of_tweets.append(str(line))
    tweet = list_of_tweets[random.choice(range(len(list_of_tweets)))][:-1]
    return tweet

if __name__ == "__main__":
    print("Starting...")
    #main()