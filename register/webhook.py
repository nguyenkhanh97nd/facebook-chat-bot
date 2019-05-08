# Project FacebookChatBot 2019
# Created by khanhnguyen
# Version 1.0

from config import *

def verify(req):

    mode = req.args.get("hub.mode")
    token = req.args.get("hub.verify_token")
    challenge = req.args.get("hub.challenge")
    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge
        else:
            return "403 Forbidden"