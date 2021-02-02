from constants import *
# I keep my api keys from github.

import tweepy
from tweepy import API

# Authorization necessary to use the bot (raplybot) on twitter.com
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)
