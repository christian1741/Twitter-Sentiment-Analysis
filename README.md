Twitter-Sentiment-Analysis
==========================

Twitter Sentiment Analysis | Naive Bayes Classifier | 

                                               ***Introduction***

I present an approach for classifying the sentiment of Twitter messages or tweets; these messages are classified as positive or negative with respect to a sentence. I accomplish this by mining tweets using Twitter’s search API and subsequently processing them for analysis. Moreover, I use Distant Supervision, in which my training data consists of tweets with emoticons. Furthermore, I examine the effectiveness of three machine-learning techniques on providing a positive or negative sentiment on a tweet corpus. I test the effectiveness using Naive Bayes classifier, Maximum Entropy classifier, and Decision Tree classifier. I show that the accuracy of those algorithms is above 60% when trained with emoticon data. (In my github account, I only have the code for Naive Bayes! I will be posting the others later)

In this example, I implemented Naive Bayes classifier using Python, Tweepy, and NLTK library. 

- Tweepy | There are excellent tutorials in its website http://www.tweepy.org 
- NLTK - Natural Language ToolKit | Please read the documentation found in its website http://www.nltk.org

In order to build a Twitter sentiment analyzer, first we need to understand the right tools and methods. Machine learning is one such tool where people have developed various methods to classify. Classifiers may or may not need training data. 

When trainning a classifier, supervised learning usually requires hand-labeled training data. With the large range of topics discussed on Twitter, it would be very difficult to manually collect and label enough data to train a sentiment classifier for tweets. One solution I propose is to use distant supervision, in which the training data consists of tweets with emoticons. The emoticons serve as noisy labels. For instance, :) in a tweet indicates that the tweet contains positive sentiment and :( indicates that the tweet contains negative sentiment. With the help of the Twitter API, it is easy to extract large amounts of tweets with emoticons in them. This is a significant improvement over the many hours it may otherwise take to hand-label training data.

                                           ***Implementation Details***

- In order to work with this project, you will need to have a Twitter account. 
- Register your client application with Twitter. 
- Create a new application and once you are done you should have your consumer token and secret. 
- Keep these two handy, you will need them. 

CREATING YOUR OWN DATASET

- I decided to create my own dataset based on emoticons such as :) and :(  
- I streamed thoudands of tweets and stored them into a file (I used a file, but you can store them into a database)
- Preprocess tweets
  * Lower case - I converted the tweets to lower case 
  * URLs - I eliminated all the URLs
  * #hashtag - hash tags can give us some useful information, so I replaced them with the exact same word without the      hash.
  * Punctuations and additional white spaces - I decided to remove punctuation at the starting and ending of the           tweets.


TRAINING THE CLASSIFIER (Naive Bayes)

