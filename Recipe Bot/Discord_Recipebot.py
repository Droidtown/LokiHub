#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import discord
import json
import asyncio
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID):
        '''清空與 messageAuthorID 之間的對話記錄'''
        templateDICT = {
            "id": messageAuthorID,
            "updatetime": datetime.now(),
            "latestQuest": "",
            "false_count": 0,
            # 新增欄位
            "state": "COLLECT_INGREDIENTS",
            "collected_data": {
                "ingredients": [],
                "servings": {},
                "time_limit": {}
            },
            "last_recipe": None,
            "excluded_recipes": []
        }
        return templateDICT

    async def on_ready(self):
        # 多輪對話資訊設定
        self.templateDICT = {
            "updatetime": None,
            "latestQuest": "",
            "state": "COLLECT_INGREDIENTS",
            "collected_data": {
                "ingredients": [],
                "servings": {},
                "time_limit": {}
            },
            "last_recipe": None,
            "excluded_recipes": []
        }
        
        self.mscDICT = {}  # userid: templateDICT
        # 對話流程管理器將在需要時創建
        
        print(f'冰箱食譜小助手已啟動！ID: {self.user.id}')

    async def on_message(self, message):
        # 不要回應自己的訊息
        if message.author == self.user:
            return None

        logging.info(f"收到來自 {message.author} 的訊息")
        logging.debug(f"訊息內容: {message.content}")
        
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串...出了什麼錯！"
            msgSTR = message.content.replace(f"<@{self.user.id}> ", "").strip()
            logging.debug(f"處理訊息: {msgSTR}")
            
            # 基本指令處理
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"
            
            # 初次對話或問候
            elif msgSTR.lower() in ["哈囉", "嗨", "嗨嗨", "你好", "您好", "hi", "hello"]:
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    
                    # 10分鐘超時重置
                    if timeDIFF.total_seconds() >= 600:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但隱私政策不允許我記得你的資料，不過我很樂意重新幫你推薦料理！請告訴我你有什麼食材？"
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                        if not replySTR:
                            replySTR = "請告訴我你有什麼食材？"
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = "你好！我是冰箱食譜小助手，請告訴我你有什麼食材，我會根據現有食材幫你推薦食譜！"

            # 正式對話處理 - 使用 conversation_flow
            else:
                # 確保用戶有會話資料
                if message.author.id not in self.mscDICT:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                
                # 檢查超時
                timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                if timeDIFF.total_seconds() >= 600:  # 10分鐘
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = "我們已經很久沒聊了，讓我們重新開始吧！請告訴我你有什麼食材？"
                else:
                    try:
                        # 在需要時才 import 和創建 flow
                        from conversation_flow import RecipeConversationFlow
                        
                        flow = RecipeConversationFlow()
                        new_state, reply_messages, updated_session_data = flow.process_user_input(
                            msgSTR, 
                            self.mscDICT[message.author.id]
                        )
                        
                        # 更新用戶會話資料
                        self.mscDICT[message.author.id] = updated_session_data
                        self.mscDICT[message.author.id]["state"] = new_state
                        self.mscDICT[message.author.id]["updatetime"] = datetime.now()
                        
                        # 處理多條回覆訊息
                        if reply_messages:
                            logging.debug(f"收到回覆訊息: {reply_messages}")
                            logging.debug(f"回覆訊息類型: {type(reply_messages)}")
                            
                            # 確保 reply_messages 是列表
                            if isinstance(reply_messages, list) and len(reply_messages) > 0:
                                # 發送第一條訊息，確保是字串格式
                                first_message = reply_messages[0]
                                if isinstance(first_message, list):
                                    # 如果第一條訊息也是列表，取出內容
                                    first_message = first_message[0] if first_message else "處理錯誤"
                                
                                first_message = str(first_message).strip()
                                logging.debug(f"發送第一條訊息: {first_message}")
                                await message.reply(first_message)
                                
                                # 如果有多條訊息，間隔發送
                                if len(reply_messages) > 1:
                                    for additional_msg in reply_messages[1:]:
                                        await asyncio.sleep(0.5)  # 0.5秒間隔
                                        
                                        # 同樣處理每條訊息的格式
                                        if isinstance(additional_msg, list):
                                            additional_msg = additional_msg[0] if additional_msg else "處理錯誤"
                                        
                                        clean_msg = str(additional_msg).strip()
                                        logging.debug(f"發送額外訊息: {clean_msg}")
                                        await message.channel.send(clean_msg)
                                
                                return  # 已經發送完畢，不需要再發送 replySTR
                            else:
                                replySTR = "抱歉，我沒有理解你的意思，可以再說一次嗎？"
                        else:
                            replySTR = "抱歉，我沒有理解你的意思，可以再說一次嗎？"
                            
                    except Exception as e:
                        logging.error(f"對話流程處理錯誤: {e}")
                        replySTR = "抱歉，系統發生了一些問題，請稍後再試。"

            # 發送回覆
            await message.reply(replySTR)


if __name__ == "__main__":
    # 讀取帳號資訊
    try:
        with open("account.info", encoding="utf-8") as f:
            accountDICT = json.loads(f.read())
    except FileNotFoundError:
        print("錯誤：找不到 account.info 文件")
        print("請確保 account.info 文件存在且包含 discord_token")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"錯誤：account.info JSON 格式錯誤 - {e}")
        exit(1)
    
    # 檢查是否有 Discord token
    if "discord_token" not in accountDICT:
        print("錯誤：account.info 中缺少 discord_token")
        print("請在 account.info 中添加你的 Discord 機器人 Token")
        exit(1)
    
    print("啟動冰箱食譜小助手...")
    print("功能：根據食材推薦料理食譜")
    print("使用方法：@ 機器人並告訴它你有什麼食材")
    
    # 設定 Discord intents
    intents = discord.Intents.default()
    intents.message_content = True  # 需要讀取訊息內容
    
    # 啟動機器人
    client = BotClient(intents=intents)
    client.run(accountDICT["discord_token"])