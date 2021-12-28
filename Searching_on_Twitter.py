#Hello and how are you??
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token =         "#########"
access_token_secret =  "#########"
consumer_key =         "#########"
consumer_secret =.     "#########"

#This is a basic listener that just prints received tweets to stdout.
class listiner(StreamListener):

    def on_data(self, data):
        try:
            print data
            saveFile = open('twitter_data_28_8pm.txt','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep (5)

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listiner())
twitterStream.filter(track=['climatechange','globalwarming', 'climate change', 'global warming'])
