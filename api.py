from constants import consumer_key, consumer_secret, access_token, access_token_secret
# I keep my api keys from github.

import tweepy
from tweepy import API

# @WHAT & @WHY: Authorization necessary to use the bot (raplybot) on twitter.com
# @ALTERNATIVES: None.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)
