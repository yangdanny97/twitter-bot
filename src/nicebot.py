from secret import *
import random, tweepy, time

DEBUG = True

class NiceBot:
    """
    An instance of the Compliments Bot. This is created whenever the bot runs.
    Fields:
        api - accesses Twitter API through tweepy
        compliments - a tuple of the set of possible compliments
        last_mention - the integer ID of the last mention the NiceBot replied to
    """
    def __init__(self):
        """
        Initializes the bot and handles authentication
        """
        try:
            auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            self.api = tweepy.API(auth)
        except:
            raise RuntimeError("Error. Authenticaton failed")

        self.compliments = self.load_tweets("tweets.txt")

        data = self.load_data()
        if len(data) == 0 or len(data[0])==0:
            print("""Unable to load data""")
            self.last_mention = None
        else:
            self.last_mention = int(data[0])


    def main(self):
        """
        The main script for the bot, WIP
        """
        #Reply to mentions
        if self.last_mention and self.last_mention>0:
            mentions = self.api.mentions_timeline(since_id = self.last_mention)
        else:
            mentions = self.api.mentions_timeline(count = 10)

        for mention in mentions:
            self.select_and_send_random_compliment(handle = mention.user.screen_name, reply_id = mention.id)
            self.last_mention = max(self.last_mention, mention.id)

        self.save_data()
        print("Bot execution complete")


    def load_tweets(self,filename):
        """
        Loads possible tweets from the specified file and returns it as a tuple of strings
        Params:
            filename - string of filename, file must have 1 tweet per line
        """
        file=open(filename,"r")
        tweets=[]
        for line in file:
            tweets.append(str(line)[:-1])
        return tuple(tweets)


    def select_and_send_random_compliment(self,handle=None,reply_id=None):
        """
        Selects and returns a random compliment and tweets it
        Params:
            handle - string of twitter handle of person to tweet to, without the @ (optional)
            reply_id - int id of tweet to reply to (optional)

        """
        random_compliment = random.choice(self.compliments)
        if handle and reply_id:
            tweet = "@"+str(handle)+" "+random_compliment+" #NiceBot"
            self.api.update_status(tweet, reply_id)
        elif handle:
            tweet = "@"+str(handle)+" "+random_compliment+" #NiceBot"
            self.api.update_status(tweet)            
        else:
            tweet = random_compliment+" #NiceBot"
            self.api.update_status(tweet)
        if DEBUG: print(tweet)
        
        

    def load_data(self):
        """
        Loads saved data of the last bot instance from a text file and returns a tuple
        """
        file=open("data.txt","r")
        data = []
        for line in file:
            data.append(str(line))
        return tuple(data)


    def save_data(self):
        """
        Saves the data of the current bot instance to a text file
        """
        file=open("data.txt","w")
        file.write(str(self.last_mention))


if __name__ == "__main__":
    print("Starting...")
    bot = NiceBot()
    bot.main()