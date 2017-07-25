import html
from twython import Twython
from twython import TwythonError

def get_tweets(handle, output):
    """
    Gets last 3200 tweets by the specified twitter handle, parses out mentions, and writes them to a file
    Params:
        handle - a string representing the twitter handle of the account to scrape
        output - a string representing the name of the output file, without file extension
    """
    try:
        app = Twython('EIULTBuVR8QSG8ZUo90hRemIb', 'wA7CggtcGsm89PBCbFatFiwvtO6ed26rIOc4oYmESRpbLMTYOK')
        user = app.lookup_user(screen_name=handle)
        tweets = []
        for i in range(16):
            a=app.get_user_timeline(screen_name=handle, count=200)
            tweets=tweets+a
            lastid.append(a[-1]['id'])

        list_of_tweets=[html.unescape(tweet["text"].replace("\n", " ")) for tweet in tweets]

        file=open(output+".txt","w")

        for tweet in list_of_tweets:
            words=tweet.split()
            newWords=words[:]
            for word in words:
                if word[0]=='@':
                    newWords.remove(word)
            tweet=' '.join(newWords)
            file.write(tweet+'\n')

    except TwythonError:
        print("Twython Error")

def get_unique(inputfile, output):
    """
    Takes and reads file input, returns a new file containing all the unique lines from the first file
    Params:
        inputfile - a string representing the name of the input .txt file, without file extension
        output - a string representing the name of the output file, without file extension
    """
    i=open(inputfile+".txt","r")
    o=open(output+".txt","w")
    list_of_tweets=[]
    for line in i:
        if str(line) not in list_of_tweets:
            list_of_tweets.append(str(line))
    count=0
    for tweet in list_of_tweets:
        count+=1
        o.write(tweet)
    print("Done. "+str(count)+" unique lines.")
# Example use case below:
# get_tweets("TheNiceBot","alltweets")
# get_unique("alltweets","uniquetweets")
