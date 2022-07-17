import os
from slack import WebClient
import time
from slack.errors import SlackApiError
import logging
from flask import Flask
from slackeventsapi import SlackEventAdapter

retrieve_oauth = 'xoxb-3798846067510-3832053253968-seElW6MD0ssLsPdiGkN27byV'

client = WebClient(token=retrieve_oauth)
app = Flask(__name__)
# channel_name = "5"
# conversation_id = None
# try:
#     for result in client.conversations_list():
#         if conversation_id is not None:
#             break
#         for channel in result["channels"]:
#             if channel["name"] == channel_name:
#                 conversation_id = channel["id"]
#                 #Print result
#                 print(f"Found conversation ID: {conversation_id}")
#                 break

# except SlackApiError as e:
#     print(f"Error: {e}")
    
slack_event_adapter = SlackEventAdapter('1e2445239f7c8f9935b179dbf574e075','/slack/events',app)

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    print(text)

# conversation_history = []
# channel_id = 'C03PRSCNUF6'

# try:

#     result = client.conversations_history(
#         channel=channel_id,
#         limit=1
#     )
#     time.sleep(5)
#     message = result["messages"][0]
#     # Print message text
#     print(message["text"])


# except SlackApiError as e:
#     print("Error creating conversation: {}".format(e))


if __name__ == '__main__':
    app.run(debug=True)
