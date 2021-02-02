from api import *

# @WHAT: A file containing all the functions that the bot will be able to use.

# @WHY: It seemed logical to me to seperate all the functions in a different file from the api.py.
# This also makes the project more readable and managable. (src: https://blog.tecladocode.com/python-30-day-21-multiple-files/)

# @ALTERNATIVES: There are many alternatives to this method.
# It would be possible to put all the code in api.py since there is not a lot of code yet.

def reply_to_tweet():
    """
    Sends a tweet to the user who most recently replied to @raplybot on twitter
    with a tweet containing 'rap for me'.
    """

    print('retrieving and replying to tweets...')
    all_mentions = api.mentions_timeline()

    # The content of the reply that the bot will send.
    rap_message = ' yo yo yo yo'

    for mention in reversed(all_mentions):

        # print(str(mention.id) + '-' + mention.text)

        if 'rap for me' in mention.text.lower():
            # checks if the bot received a request to deliver a rap
            print('received a request')
            print('dropping a new single...')
            # Checks if the latest mention came from the same person.
            if mention.id == mention.id[0]:
                # Posts a tweet saying the bot is 'too tired' and won't generate a new rap.
                api.update_status('@' + mention.user.screen_name + ' yo sorry I am too tired right now')
            else:
                # Posts a tweet with the rap to the user.
                api.update_status('@' + mention.user.screen_name + rap_message, mention.id)
            print('single dropped.')