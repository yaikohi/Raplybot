from constants import *
import tweepy
from tweepy import API

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

# mentions Contains the mentions to @ raplybot on twitter.
mentions = api.mentions_timeline()

# The text inside the latest mention @raplybot
latest_mention_text = mentions[0].text

# username_latest_mention contains the username of the person who mentioned @raplybot.
username_latest_mention = '@' + mentions[0].user.screen_name


# # Creates a message based on the latest mention.
# message = username_latest_mention + ' yo ' + latest_mention_text + ' yo yo'
print(api.rate_limit_status())

#
# # Sending a reply to the latest mention to @raplybot
# def reply_to_tweet():
#     print('retrieving and replying to tweets...')
#     all_mentions = api.mentions_timeline()
#
#     rap_message = ' yo yo yo yo'
#
#     for mention in reversed(all_mentions):
#         print(str(mention.id) + '-' + mention.text)
#         if 'rap for me' in mention.text.lower():
#             print('received a request')
#             print('dropping a new single...')
#             # Checks if the latest mention came from the same person.
#             if mention.id == mention.id[0]:
#                 api.update_status(('@' + mention.user.screen_name + ' yo sorry I am too tired right now'))
#             else:
#                 api.update_status('@' + mention.user.screen_name + rap_message, mention.id)
#             print('single dropped.')
#
#
# while True:
#     reply_to_tweet()
#     time.sleep(20)
