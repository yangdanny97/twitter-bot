from secret import *
import random, tweepy, time

DEBUG = True

class NiceBotStreamListener(tweepy.StreamListener):
    """
    Stream listener for Twitter Streaming API
    Fields:
        bot - an instance of the NiceBot
    """
    def __init__(self, bot):
        tweepy.StreamListener.__init__(self)
        self.bot = bot

    def on_status(self, status):
        print("Recieved tweet from stream")
        if DEBUG: print(status.user.screen_name, status.text, status.in_reply_to_status_id)
        # self.bot.select_and_send_random_compliment(handle = status.user.screen_name)
        return False

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

class NiceBot:
    """
    An instance of the Compliments Bot. This is created whenever the bot runs.
    Fields:
        auth - stores authentication details
        api - accesses Twitter API through tweepy
        compliments - a tuple of the set of possible compliments
        last_mention - the integer ID of the last mention the NiceBot replied to
        random_compliment - boolean, whether or not a random person has been complimented
    """
    def __init__(self):
        """
        Initializes the bot and handles authentication
        """
        try:
            auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            self.auth = auth
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

    def reply_mentions(self):
        """
        Reply to mentions with a compliment
        """
        last_mention = self.last_mention

        if self.last_mention and self.last_mention>0:
            mentions = self.api.mentions_timeline(since_id = self.last_mention)
        else:
            mentions = self.api.mentions_timeline(count = 10)
        if DEBUG: print(str(len(mentions))+" new mentions found")
        for mention in mentions:
            if mention.in_reply_to_status_id is None:
                if DEBUG: print("Replied to mention"+str(mention.id))
                self.select_and_send_random_compliment(handle = mention.user.screen_name, reply_id = mention.id)
                self.last_mention = max(self.last_mention, mention.id)
        
        if last_mention!=self.last_mention:
            self.save_data()
            print("Updated data")

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
    bot.reply_mentions()

    listener = NiceBotStreamListener(bot)
    stream  = tweepy.Stream(auth = bot.auth, listener=listener)
    stream.sample()
    print("Execution complete")
    