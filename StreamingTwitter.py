#Christian Caicedo | April 2014
#christiancaicedo.com/myblog | Twitter: #@caicedoc1741
#This file streams tweets from the Twitter API and saves them into a file 
#It will create a file with thousands of positive and negative tweets  
#The format is already set up, but you can modify it too.  

import sys
import tweepy
import re 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

#******Creating a dataset with POSITIVE Tweets*********** 

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, maxnum, api=None):
        self.n = maxnum
        self.api = api

    def on_status(self, status):
        try:
            tweets = []
            name = status.author.screen_name
            textTwitter = status.text
            
            #Convert into lowercase
            Tweet = textTwitter.lower()
            
            #Convert www.* or https?://* to URL
            Tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',Tweet)
            
            #Convert @username to User
            Tweet = re.sub('@[^\s]+','TWITTER_USER',Tweet)
            
            #Remove additional white spaces
            tweet = re.sub('[\s]+', ' ', Tweet)
            
            #Replace #word with word Handling hashtags
            Tweet = re.sub(r'#([^\s]+)', r'\1', Tweet)
            
            #trim
            Tweet = Tweet.strip('\'"')
            
            #Deleting happy and sad face emoticon from the tweet 
            a = ':)'
            b = ':('
            Tweet = Tweet.replace(a,'')
            Tweet = Tweet.replace(b,'')
            
            #Deleting the Twitter @username tag and reTweets
            tag = 'TWITTER_USER' 
            rt = 'rt'
            Tweet = Tweet.replace(tag,'')
            Tweet = Tweet.replace(rt,'')
            
            final_tweet = '|positive|, |%s| ' % (Tweet)

            f = open('YourFileHereName', 'r+')
            old = f.read()
            f.write(final_tweet+'\n')
            f.close()
        
            self.n = self.n+1
            if self.n < 250: 
                return True
            else:
                print 'maxnum = '+str(self.n)
                return False
        
        except Exception as e:
            print (e)

    def on_error(self, status_code):
        #print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        #print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream
        
        
        
        
        
        
