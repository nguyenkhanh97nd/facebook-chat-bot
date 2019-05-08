# Project FacebookChatBot 2019
# Created by khanhnguyen
# Version 1.0
from api import fb

def handle(sender_psid, received_postback):
    payload = received_postback.get('payload')
    if payload == "test_postback":
        response = "Message postback"
        fb.post_api_text(sender_psid, response)