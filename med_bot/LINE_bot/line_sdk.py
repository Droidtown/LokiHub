#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install line-bot-sdk
"""

from linebot import LineBotApi
from linebot import WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage


class Linebot:

    bot = None
    webhookParser = None

    def __init__(self, channel_access_token, channel_secret):
        self.bot = LineBotApi(channel_access_token)
        self.webhookParser = WebhookParser(channel_secret)#get authorization

    def parse(self, body, signature): 
        resultLIST = []

        try:
            events = self.webhookParser.parse(body, signature)
            for event in events:
                if event.source.user_id == "Udeadbeefdeadbeefdeadbeefdeadbeef":
                    continue

                if event.type == "message":
                    try:
                        resultDICT = {
                            "status": True,
                            "type": event.type,
                            "userID": event.source.user_id,
                            "replyToken": event.reply_token,
                            "message": event.message.text,
                            "timestamp": event.timestamp
                        }
                    except Exception as e:
                        print("Linebot parseError => {}".format(str(e)))
                        resultDICT = {"status": False}

                resultLIST.append(resultDICT)
                if event.type == "sticker":
                    try:
                        resultDICT = {
                            "status": True,
                            "type": event.type,
                            "userID": event.source.user_id,
                            "replyToken": event.reply_token,
                            "message": event.message.text,
                            "timestamp": event.timestamp
                        }
                    except Exception as e:
                        print("Linebot parseError => {}".format(str(e)))
                        resultDICT = {"status": False}                    
                    
                    

        except InvalidSignatureError as e:
            print("Linebot InvalidSignatureError => {}".format(str(e)))
        except LineBotApiError as e:
            print("Linebot LineBotApiError => {}".format(str(e)))

        return resultLIST

    def respText(self, replyToken, text):
        self.bot.reply_message(replyToken, TextSendMessage(text=text), notification_disabled=True)