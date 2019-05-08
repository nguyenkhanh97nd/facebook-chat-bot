# Project FacebookChatBot 2019
# Created by khanhnguyen
# Version 1.0
from api import fb

def handle(sender_psid, received_message):
    print(received_message)
    if received_message.get('text'):
        response = "Test response: Received " + received_message.get('text')
        fb.post_api_text(sender_psid, response)