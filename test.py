"""
File for testing python code for the bot.
"""

from api import *


# The mentions to @raplybot
mentions = api.mentions_timeline()

# The text inside the most recent mention to the bot.
latest_mention_content = mentions[0].text

# The username of the person who most recently mentioned @raplybot.
latest_mention_username = '@' + mentions[0].user.screen_name

# Tweet to send on twitter.com
tweet = latest_mention_username + ' yo ' + latest_mention_content + ' yo yo'

