#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json
from fc_info import information
from fc_info import growth
from fc_info import safety
from DICT import companyDICT


    
from ArticutAPI import Articut
articut = Articut(username= "", apikey= "")

from stockBOT_Loki import runLoki



class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("到到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msg in ("hi","hello","嗨"):
                await message.reply("嗨，我是一個查詢上市半導體公司股票財報資料的BOT！！請輸入公司名或是股票代碼與想要查詢的資訊(公司基本資料、財報分析指標)。若有不懂的財報名詞也可以問我喔")         
            else:
                inputLIST = [msg]
                filterLIST = []
                resultDICT = runLoki(inputLIST, filterLIST)
                print("Result => {}".format(resultDICT))
                
                print(resultDICT)
                
                if  "fun_information" in resultDICT.keys():
                    result_infoDICT = information(resultDICT["symbol"])
                    resultDICT.update(result_infoDICT)
                elif "fun_growth" in resultDICT.keys():
                    result_growthDICT = growth(resultDICT["symbol"])
                    resultDICT.update(result_growthDICT)
                elif "fun_profitability" in resultDICT.keys():
                    result_profitabilityDICT = profitability(resultDICT["symbol"])
                    resultDICT.update(result_profitabilityDICT)   
                elif "fun_safety" in resultDICT.keys():
                    result_safetyDICT = safety(resultDICT["symbol"])
                    resultDICT.update(result_safetyDICT)                       
                elif "reply" in resultDICT.keys():
                    pass
                    
            
                    if "fun_information" in resultDICT.keys():
                        await message.reply(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"的公司基本資料如下！"+"\n公司名稱："+resultDICT["name"]+"\n產業別："+resultDICT["industry"]+"\n市值："+resultDICT["value"]+"\n主要業務："+resultDICT["business"])  
                    elif "fun_growth" in resultDICT.keys():
                        await message.reply(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"在"+resultDICT["quarter"]+"的獲利年成長率如下！"+"\n營收年成長率："+resultDICT["revenue_YOY"]+"\n毛利年成長率："+resultDICT["gross_profit_YOY"]+"\n營業利益年成長率："+resultDICT["operating_income_YOY"]+"\n稅前淨利年成長率："+resultDICT["NIBT_YOY"]+"\n稅後淨利年成長率："+resultDICT["NI_YOY"]+"\n每股稅後盈餘年成長率："+resultDICT["EPS_YOY"])    
                    elif "fun_profitability" in resultDICT.keys():
                        await message.reply(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"在"+resultDICT["quarter"]+"的獲利能力如下！"+"\n營業毛利率："+resultDICT["GPM"]+"\n營業利益率："+resultDICT["OPM"]+"\n稅前淨利率："+resultDICT["PTPM"]+"\n稅後淨利率："+resultDICT["NPM"]+"\n每股稅後盈餘："+resultDICT["EPS"]+"\n每股淨值(元)："+resultDICT["NASPS"]+"\n股東權益報酬率："+resultDICT["ROE"]+"\n資產報酬率："+resultDICT["ROA"])    
                    elif "fun_safety" in resultDICT.keys():
                        await message.reply(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"在"+resultDICT["quarter"]+"的償債能力如下！"+"\n現金比："+resultDICT["CR"]+"\n速動比："+resultDICT["QR"]+"\n流動比："+resultDICT["current_ratio"]+"\n利息保障倍數："+resultDICT["ICR"]+"\n現金流量比："+resultDICT["OCFR"]+"\n負債總額比(元)："+resultDICT["DR"])    
                    elif "reply" in resultDICT.keys():
                        await message.reply(resultDICT["reply"])
                    elif resultDICT["symbol"] == None:
                        await message.reply("不確定您要找哪一支股票的資訊！請再輸入一次股票名稱或是代號！")
                    else:
                        await message.reply("不確定您要找哪一類的資訊！請再輸入一次要查的資料類別！")
                                    

if __name__ == "__main__":
    client = BotClient()
    client.run("")