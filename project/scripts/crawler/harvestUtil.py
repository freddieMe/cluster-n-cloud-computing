
import tweepy
from sentiment import classifier
from database import database

from crawler.config import db_name
from database.parser import Parser
from crawler.config import app_auth,topics_file
import re
import time


def loadTopicFiles():
    file = open(topics_file,"r")
    topics = []
    for topic in file:
        topics.append(topic.strip())
    topics = set(topics)
    return topics

def containTopic(topics,text):
    text = text.split(' ')
    for word in text:
        if word in topics:
            print(word)
            return True
    return False
    


def searchById(admin, userid):
    print("on search...")

    #set up
    db = database.DButils()
    cl = classifier.MyClassifier()
    parser = Parser()    
    user = admin
    auth = tweepy.OAuthHandler(app_auth[user].ckey, app_auth[user].csec)
    auth.set_access_token(app_auth[user].atoken, app_auth[user].asec)
    api = tweepy.API(auth)
    try:
        query = api.user_timeline(user_id=userid, count=25)
    except tweepy.TweepError:
        print("search API access time limited, searching sleeps n back soon ")
        time.sleep(60*15)
    for status in query:
        
        # filter out retweets
        try:
            if status.retweeted_status:
                return None
        except:
            pass
        
        #filter out tweets without interested topics
        topics = loadTopicFiles()
        if not containTopic(topics, status.text):
            return
        
        # perform sentiment analysis n store scores to json
        polarity, subjectivity, label = cl.get_sent_score(status.text)
        sent = {
            'polarity':str(polarity), 
            'subjectiviy':str(subjectivity),
            'label':label
        } 
        #parse tweets
        try:
            record = parser.status_parse(status,sent)
        except:
            pass
        if record is None:
            return        
                
        # save into couchdb
        db.save(db_name,record)        

# setting up stream listener
class MyStreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False    

    def on_status(self, status):
        #setup
        db = database.DButils()
        cl = classifier.MyClassifier()
        parser = Parser()
        
        # filter out retweets
        try:
            if status.retweeted_status:
                return None
        except:
            pass
        
        #filter out unrelated topics
        topics = loadTopicFiles()
        
        if not containTopic(topics, status.text):
            return
                
        
        # perform sentiment analysis n store scores to json
        polarity, subjectivity, label = cl.get_sent_score(status.text)
        sent = {
            'polarity':str(polarity), 
            'subjectiviy':str(subjectivity),
            'label':label
        }
        
        #parse tweets
        record = parser.status_parse(status,sent)
        if record is None:
            return        
         
        # save into couchdb
        db.save(db_name,record)
        
        #get all tweets from users timeline
        try:
            searchById("jiyu",status.user.id)
        except Exception as e:
            # access time limit handling
            print(e)
            time.sleep(20)
        print("finish search on user: "+str(status.user.id))
        return True