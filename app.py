# Project FacebookChatBot 2019
# Created by khanhnguyen
# Version 1.0

from flask import Flask, request
from register import webhook
from event import message, postback, referral

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!!!"

@app.route("/webhook", methods=["GET", "POST"])
def listen_webhook():
    if request.method == "GET":
        return webhook.verify(request)
    if request.method == "POST":
        payload = request.json
        if payload["object"] == "page":
            for entry in payload["entry"]:
                webhook_event = entry["messaging"][0]
                sender_psid = webhook_event['sender']['id']
                print('Sender PSID: ' + sender_psid)
                print(webhook_event)
                if webhook_event.get('message'):
                    message.handle(sender_psid, webhook_event.get('message'))
                if webhook_event.get('postback'):
                    postback.handle(sender_psid, webhook_event.get('postback'))
                if webhook_event.get('referral'):
                    referral.handle(sender_psid, webhook_event.get('referral'))

            return "EVENT_RECEIVED"
        else:
            return "404 Not Found"

if __name__ == "__main__":
    app.run()