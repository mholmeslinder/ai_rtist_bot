''' A simple tweepy-based Twitter bot that will use generate_artist.py 
to spit out AI-generated fictional artists'''
import time
import sys
import tweepy
import generate_artist
import os

# use this one for testing
# from dotenv import load_dotenv
# load_dotenv()

# CONSUMER_KEY = os.getenv('CONSUMER_KEY')
# CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
# ACCESS_KEY = os.getenv('ACCESS_KEY')
# ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print("about to get artist...")
    artist = generate_artist.get_tweet()
    api.update_status(artist)
    time.sleep(INTERVAL)
