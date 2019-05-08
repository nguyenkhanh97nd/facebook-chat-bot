# Project FacebookChatBot 2019
# Created by khanhnguyen
# Version 1.0
from config import *
import requests

def post_api_text(sender_psid, text):
    payload = {
        "message": {
            'text': text
        },
        'recipient': {
            'id': sender_psid
        }
    }
    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }
    response = requests.post(
        API_FOR_MESSAGE,
        params=auth,
        json=payload
    )
    return response.json()