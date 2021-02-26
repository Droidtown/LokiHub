#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import discord
from DrugBot import runLoki as drugbot

DISCORD_TOKEN=""
DISCORD_GUILD="Droidtown Linguistics Tech."
BOT_NAME = "DrugBot"

# Documention
# https://discordpy.readthedocs.io/en/latest/api.html#client

client = discord.Client()
UserResponseDICT = {}
logging.basicConfig(level=logging.DEBUG) # 檢查Bug

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break
    print(f'{BOT_NAME}bot has connected to Discord!')
    print(f'{guild.name}(id:{guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    print("message.content", message.content)
    
    if "<@!{}>".format(client.user.id) in message.content: # 是用computer發的訊息
        PhoneOrComputerChar = 'c'
    elif "<@{}>".format(client.user.id) in message.content: # 是用phone發的訊息
        PhoneOrComputerChar = 'p'
        
    if "<@!{}>".format(client.user.id) in message.content or "<@{}>".format(client.user.id) in message.content: # (client.user.id) is botID
        
        # 拿掉message content中的userID
        if PhoneOrComputerChar == 'c':
            index = message.content.index("<@!{}>".format(client.user.id)) + len("<@!{}>".format(client.user.id))
            userIDSTR = "<@!{}>".format(message.author.id) # 儲存說話者的ID格式，用於回覆
        else:
            index = message.content.index("<@{}>".format(client.user.id)) + len("<@{}>".format(client.user.id))
            userIDSTR = "<@{}>".format(message.author.id) # 儲存說話者的ID格式，用於回覆
        message.content = message.content[index:] 
        

        # 測試用messages
        if " haiyya" == message.content:
            responseLIST = "Help!"
            await message.channel.send(userIDSTR + "\n" + responseLIST)
            
        elif ' test' == message.content:
            responseLIST = "Sleeping zZzZ"
            await message.channel.send(userIDSTR + "\n" + responseLIST)
            
        elif " 你在幹嘛" == message.content:
            responseLIST = "https://tenor.com/view/pedro-monkey-puppet-meme-awkward-gif-15268759" #猴子gif
            await message.channel.send(userIDSTR + "\n" + responseLIST)
        
        elif " 你有沒有那種白色的粉末" == message.content:
            responseLIST = "我要報警了"
            await message.channel.send(userIDSTR + "\n" + responseLIST)
        
        # 多輪對話 - 遇到無特定形狀之藥丸/藥片時需詢問形狀
        elif message.author.id in UserResponseDICT:
            logging.warning('round 2 in')
            if "形" in message.content:
                logging.warning('message correct')
                # 把url中的"藥丸"換成"藥物形狀"，[1:]是去掉空格
                if "藥丸" in UserResponseDICT[message.author.id]:
                    msgLIST = UserResponseDICT[message.author.id].replace("藥丸",message.content[1:])
                    
                # 把url中的"藥片"換成"藥物形狀"，[1:]是去掉空格
                elif "藥片" in UserResponseDICT[message.author.id]:
                    msgLIST = UserResponseDICT[message.author.id].replace("藥片",message.content[1:])
                    
                del UserResponseDICT[message.author.id] # 多輪對話結束，刪除此user的暫存訊息
                await message.channel.send(userIDSTR + "\n" + msgLIST)
        
        else:
            # call RunLoki
            responseLIST = drugbot([message.content])
            UserResponseDICT[message.author.id] = responseLIST # 把A輸入且已轉成網址的string加到A專屬的回答欄中
            logging.error(UserResponseDICT[message.author.id])
            # 當url中的shape出現無特定形狀的"藥丸"or"藥片"，以多輪對話詢問其確切形狀
            if "藥丸"in responseLIST:
                await message.channel.send(userIDSTR + "\n請問此藥丸是什麼形狀？")
                return
            elif "藥片"in responseLIST:
                await message.channel.send(userIDSTR + "\n請問此藥片是什麼形狀？")
                return
            
            # 沒有get到intent
            elif responseLIST == "https://drugs.olc.tw/drugs/outward/": 
                responseLIST = "這看起來不像藥物的外觀QQ" # 可以建 List of List 回答庫

            await message.channel.send(userIDSTR + "\n" + responseLIST)
        
    elif "bot 點名" == message.content:
        responseLIST = "又 (˙w˙)"
        await message.channel.send(responseLIST)
    
    else:
        pass


client.run(DISCORD_TOKEN)
