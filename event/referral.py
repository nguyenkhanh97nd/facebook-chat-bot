# Project FacebookChatBot 2019
# Created by khanhnguyen
# Version 1.0
from api import fb

def handle(sender_psid, received_referral):
    payload = received_referral.get('ref')
    if payload == "tricksmagical":
        response = "Test referral"
        fb.post_api_text(sender_psid, response)