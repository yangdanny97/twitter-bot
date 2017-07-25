from secret import *
import random, tweepy, time

DEBUG = True

class NiceBot:
    """
    An instance of the Compliments Bot. This is created whenever the bot runs.
    Fields:
        api - accesses Twitter API through tweepy
        compliments - a tuple of the set of possible compliments
        last_mention - the ID of the last mention the NiceBot replied to
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
        self.last_mention = data[0]


    def main(self):
        """
        The main script for the bot, WIP
        """
        self.select_and_send_random_compliment()
        #self.save_data()
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


    def select_and_send_random_compliment(self,handle=None):
        """
        Selects and returns a random compliment and tweets it
        Params:
            handle - string of twitter handle of person to tweet to, without the @
        """
        random_compliment = random.choice(self.compliments)
        if DEBUG: print(random_compliment)
        if handle:
            tweet = "@"+str(handle)+" "+random_compliment+" #NiceBot"
        else:
            tweet = random_compliment+" #NiceBot"
        self.api.update_status(tweet)
        

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