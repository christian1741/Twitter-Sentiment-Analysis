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
from tweepy import Stream
from nltk.corpus import stopwords
