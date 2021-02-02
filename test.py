"""
File for testing python code for the bot.
"""

from api import *

# @WHAT: Lines of code for testing smaller things with the bot.
# @WHY: So that I can easily test the twitter bot before applying bigger functions.
# @ALTERNATIVES: There is a lot I can still learn about code-testing.
# Interesting read: https://realpython.com/python-testing/
# Very much a work-in-progress for me.


# The mentions to @raplybot
mentions = api.mentions_timeline()

# The text inside the most recent mention to the bot.
latest_mention_content = mentions[0].text

# The username of the person who most recently mentioned @raplybot.
latest_mention_username = '@' + mentions[0].user.screen_name

# Tweet to send on twitter.com
tweet = latest_mention_username + ' yo ' + latest_mention_content + ' yo yo'

