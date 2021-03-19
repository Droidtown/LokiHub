#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from med_bot_for_Loki import Result as medBot
from account_info import accountInfoDICT

DISCORD_TOKEN=accountInfoDICT["DISCORD_TOKEN"]
DISCORD_GUILD=accountInfoDICT["DISCORD_GUILD"]
BOT_NAME = "Med_Bot"
#DISCORD_TOKEN=""
#DISCORD_GUILD=""
#BOT_NAME = "my_med_bot"

# Documention
# https://discordpy.readthedocs.io/en/latest/api.html#client

client = discord.Client()
responseDICT = {}

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
    endconversationLIST = ["謝謝","謝啦","thx","ok","掰","bye","掰掰","好喔","你可以退下了"]   
    msgSTR = message.content.replace("<@!{}> ".format(client.user.id),"").lower().strip()
    if "<@!{}>".format(client.user.id) in message.content or "<@{}>".format(client.user.id) in message.content:
        if msgSTR == "":
            await message.channel.send("<@!{}>您好\n請簡述您的症狀:)\n如果患者為12歲以下孩童請至小兒科".format(message.author.id))
        elif any (e == msgSTR  for e in endconversationLIST ):
            await message.channel.send("<@!{}>好的:)".format(message.author.id))
        #medBot回傳string像是:請去家醫科
        else:
            await message.channel.send("<@!{}>".format(message.author.id)+medBot(msgSTR)["msg"])
   
client.run(DISCORD_TOKEN)
