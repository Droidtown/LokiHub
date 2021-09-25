#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
import datetime

from pprint import pprint
from Lease_Dispute import runLoki
from Lease_Dispute import botRunLoki

logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()

mscDICT = {
    # "userID": {creditTemplate, mortgageTemplate}
}
# </取得多輪對話資訊>


with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

from ArticutAPI import Articut
articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT


class BotClient(discord.Client):

    def getNewTemplate(self):
        leaseTemplate = {"confirm425_BOOL":None,
                         "confirm425tb1_BOOL":None,
                         "confirm425tb2_BOOL":None,
                         "confirm425tb3_BOOL":None,
                         "confirm429_BOOL":None,
                         "confirm429tb1_BOOL":None,
                         "confirm_Security_Deposit_BOOL":None,
                         "confirm_fees_BOOL":None,
                         "confirm_comein_BOOL":None,
                         "updatetime":"datetime",
                         "complete":False}
        return leaseTemplate

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("收到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msgSTR == 'ping':
                await message.reply('pong')
            elif msgSTR == 'ping ping':
                await message.reply('pong pong')

            elif msgSTR in ["哈囉","嗨","你好","您好","在嗎","Hi","hi","Hello","hello"]: #在使用者以問候開啟對話時，計算對話時間差
                if message.author.id in mscDICT.keys() and "updatetime" in mscDICT[message.author.id].keys():  #有講過話(判斷對話時間差)
                    nowDATETIME = datetime.datetime.now()
                    timeDIFF = nowDATETIME - mscDICT[message.author.id]["updatetime"]
                    if timeDIFF.total_seconds() >= 300:   #有講過話，但與上次差超過5分鐘(視為沒有講過話，刷新template)
                        mscDICT[message.author.id] = self.getNewTemplate()
                        await message.reply("嗨嗨，您好，我是您的租賃法律問題小幫手，請問您遇到什麼問題了呢？")
                    else:  #有講過話，而且還沒超過5分鐘(就繼續上次的對話)
                        await message.reply("我還在等您的回覆喔")
                else:  #沒有講過話(給他一個新的template)
                    mscDICT[message.author.id] = self.getNewTemplate()
                    mscDICT[message.author.id]["updatetime"] = datetime.datetime.now() #記錄開啟對話的時間
                    await message.reply("嗨嗨，您好，我是您的租賃法律問題小幫手，請問您遇到了什麼問題呢？")
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"

                #第一輪對話(都還不知道使用者要問什麼問題的時候，filterLIST就都跑過所有要確認問題的intent)
                if mscDICT[message.author.id]["confirm425_BOOL"] == None and mscDICT[message.author.id]["confirm429_BOOL"] == None and mscDICT[message.author.id]["confirm_Security_Deposit_BOOL"] == None and mscDICT[message.author.id]["confirm_fees_BOOL"] == None and mscDICT[message.author.id]["confirm_comein_BOOL"] == None:
                    lokiResultDICT = botRunLoki(msgSTR,filterLIST = ["425"]+["429"]+["Security_Deposit"]+["electricity_water_fees"]+["Come_in"]+["Haunted_House"])
                    print("Result => {}".format(lokiResultDICT))

                    #將Loki Intent跑出來的結果存入mscDICT
                    if "confirm425_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm425_BOOL"] = lokiResultDICT["confirm425_BOOL"]
                    if "confirm429_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm429_BOOL"] = lokiResultDICT["confirm429_BOOL"]
                    if "confirm_Security_Deposit_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm_Security_Deposit_BOOL"] = lokiResultDICT["confirm_Security_Deposit_BOOL"]
                    if "confirm_fees_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm_fees_BOOL"] = lokiResultDICT["confirm_fees_BOOL"]
                    if "confirm_comein_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm_comein_BOOL"] = lokiResultDICT["confirm_comein_BOOL"]
                    if "confirm_haunted_house_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm_haunted_house_BOOL"] = lokiResultDICT["confirm_haunted_house_BOOL"]
                    #不需要處理多輪對話的租賃問題
                    if mscDICT[message.author.id]["confirm_Security_Deposit_BOOL"] == True:
                        replySTR = """聽起來您的問題與押金有關。其實呢，押金的作用，是為了擔保您(承租人)在租賃關係中所生的租金債務或是損害賠償責任。
                                    因此，如果您沒有欠房東租金或是需要負擔損害賠償責任，那麼在租賃關係消滅(例如租期屆滿或租賃契約終止)，且您返還租賃住宅時，房東就應該要將押金全數返還給您。
                                    如果房東沒有依約返還押金，您可以到郵局寄發存證信函，定相當期限，請求房東在期限內返還押金。
                                    不過，若是您確實有欠租或需要負擔損害賠償責任的情形，房東是可以扣您的押金作為擔保的，所以如果有這方面的爭議問題，
                                    請您與房東確認您是否真的有欠租，或是具有需負擔損害賠償責任的情事(例如您是否有損壞屋內的家具或其他物品)，
                                    如果雙方無法達成共識，建議您可以依租賃住宅條例第16條的規定，向直轄市或縣（市）政府聲請調處，來維護雙方的權益，而且無須付調處費喔。""".replace(" ", "").replace("\n", "")
                        mscDICT[message.author.id]["complete"] = True #對話結束
                        await message.reply(replySTR)
                        mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                        print(mscDICT)
                        await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")

                    elif mscDICT[message.author.id]["confirm_fees_BOOL"] == True:
                        replySTR = """聽起來您的問題是關於水電費、網路費、瓦斯費等方面的爭議，根據內政部頒布的「住宅租賃契約應約定及不得約定事項」，
                                   原則上水費、電費、瓦斯費、網路費、管理費等費用，基於契約自由原則，都可以由雙方約定某一方負擔，所以請您注意您的租賃契約書面上關於這些費用的約定。
                                   不過，如果在租賃期間因不可歸責於租賃雙方之事由，致管理費增加者，承租人就增加部分之金額，以負擔百分之十為限。
                                   另外，關於電費的部分，雙方可以就夏季月分的費用與非夏季月分的費用分別約定，但不論怎麼約定，都不可以超過台電公司所定當月用電量最高級距的每度金額。
                                   所以房東的電費收取只要不超過現在台電規定的6.41元/度，就不算違法。但畢竟電費收取是代收費用，房東不可以此營利，
                                   如果您發現房東有超收行為，您可以向當地縣(市)政府的地政局(處)、消保官檢舉。""".replace(" ", "").replace("\n", "")
                        mscDICT[message.author.id]["complete"] = True #對話結束
                        await message.reply(replySTR)
                        mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                        print(mscDICT)
                        await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")

                    elif mscDICT[message.author.id]["confirm_comein_BOOL"] == True:
                        replySTR = """聽起來您遇到的問題是關於房東任意進出您租屋處的問題。其實當房屋出租之後，房東(出租人)雖然仍擁有房屋的所有權，
                                   但房客(承租人)已經取得了完整的使用收益的權限，所以如果房東想要進入出租房屋時，必須經過房客的同意，否則不可任意進出。
                                   如果房東未經您的同意，就擅自進入您的租屋處的話，恐怕會觸犯刑法第306條「無故侵入他人住宅罪」，也可能構成民法第195條第1項個人隱私權的侵權行為。
                                   若您向房東反應或溝通後未獲改善，建議您可以直接報警處理。""".replace(" ", "").replace("\n", "")
                        mscDICT[message.author.id]["complete"] = True #對話結束
                        await message.reply(replySTR)
                        mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                        print(mscDICT)
                        await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")
                    
                    elif mscDICT[message.author.id]["confirm_haunted_house_BOOL"] == True:
                        replySTR = """聽起來您租到凶宅了。依據內政部最新公布的「住宅租賃契約應約定及不得約定事項」，
                                   您與出租人(房東)在訂立租賃契約時，出租人應向您揭露房屋是否發生過非自然死亡之情事，
                                   如果出租人沒有在租賃契約上向您揭露，而且您已經確認您租到的是凶宅的話，
                                   您可以向出租人主張瑕疵擔保責任，看您要選擇減少租金(繼續住)，還是要終止租約(搬走)。
                                   不論您選擇哪一種，建議您可以寄存證信函通知房東，這是法律上較有力的保存證據的方式。""".replace(" ", "").replace("\n", "")
                        mscDICT[message.author.id]["complete"] = True #對話結束
                        await message.reply(replySTR)
                        mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                        print(mscDICT)
                        await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")
                        
                    #開始處理需要多輪對話的租賃問題
                    #425的第一輪對話
                    elif mscDICT[message.author.id]["confirm425_BOOL"] == True: #確認問題為425
                        replySTR = "請問您與房東是否已經簽訂租賃契約？" #往下問425_tb1
                        await message.reply(replySTR)

                    #429的第一輪對話
                    elif mscDICT[message.author.id]["confirm429_BOOL"] == True: #確認問題為429
                        replySTR = "請問您的租賃契約上，有沒有特別規定必須由承租人(您)負擔修繕義務？例如要求東西壞了必須由您自行修理。" #往下問429_tb1
                        await message.reply(replySTR)

                    else: #如果無法辨識是什麼問題，就給予統一的回覆
                        replySTR = """Sorry,我目前可能還沒有辦法處理您的問題。
                                   如果是關於租屋處被賣掉、修繕問題、押金問題、水電費問題、房東任意進出租處的問題，您可以試著用別的問句問我。
                                   如果是其他租賃問題的話，我現在還不會處理，建議您可以上崔媽媽基金會的網站查詢，不好意思。""".replace(" ", "").replace("\n", "")
                        await message.reply(replySTR)


                #425的第二輪對話
                elif mscDICT[message.author.id]["confirm425_BOOL"] == True and mscDICT[message.author.id]["confirm425tb1_BOOL"] != True: #425的第二輪對話
                    lokiResultDICT = botRunLoki(msgSTR,filterLIST = ["425_tb1"]) #filterLIST只跑425_tb1
                    if "confirm425tb1_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm425tb1_BOOL"] = lokiResultDICT["confirm425tb1_BOOL"]
                        if mscDICT[message.author.id]["confirm425tb1_BOOL"] == False:
                            replySTR = """您與出租人(房東)之租賃關係尚未正式成立，無法主張買賣不破租賃。
                                       但若您在準備或商議締約的過程中，房東有就訂約重要事項為惡意隱匿或不實說明，或有其他違反誠實信用方法之情形，
                                       您可依民法第245條之1之規定向房東請求信賴利益損害賠償。""".replace(" ", "").replace("\n", "")
                            mscDICT[message.author.id]["complete"] = True #對話結束
                            await message.reply(replySTR)
                            mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                            await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")

                        elif mscDICT[message.author.id]["confirm425tb1_BOOL"] == True:
                            replySTR = "請問房東是否已將房屋交付給您？例如您已經搬入您的租處，或是房東已經將鑰匙交給您、將大門密碼鎖的密碼告知您。" #往下問425_tb2
                            await message.reply(replySTR)
                    else: #聽不懂
                        replySTR = "抱歉，我有點不太懂您的意思，可以請您換一個說法再說一遍嗎？謝謝。"
                        await message.reply(replySTR)

                #425的第三輪對話
                elif mscDICT[message.author.id]["confirm425tb1_BOOL"] == True and mscDICT[message.author.id]["confirm425tb2_BOOL"] != True: #425的第三輪對話
                    lokiResultDICT = botRunLoki(msgSTR,filterLIST = ["425_tb2"]) #filterLIST只跑425_tb2
                    if "confirm425tb2_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm425tb2_BOOL"] = lokiResultDICT["confirm425tb2_BOOL"]
                        if mscDICT[message.author.id]["confirm425tb2_BOOL"] == False:
                            replySTR = """出租人(房東)尚未將租賃物交付給您，無法主張買賣不破租賃。
                                       但您與房東之間之租賃契約已經成立，若房東請您搬離，
                                       您可以向房東主張租賃契約之債務不履行，請求房東負履行利益損害賠償責任。""".replace(" ","").replace("\n","")
                            mscDICT[message.author.id]["complete"] = True #結束對話
                            await message.reply(replySTR)
                            mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                            await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")

                        elif mscDICT[message.author.id]["confirm425tb2_BOOL"] == True:
                            replySTR = "請問房東是否已經辦理所有權移轉登記，確實將租賃物(您租屋處)的所有權過戶給他人？" #往下問425_tb3
                            await message.reply(replySTR)
                    else: #聽不懂
                        replySTR = "抱歉，我有點不太懂您的意思，可以請您換一個說法再說一遍嗎？謝謝。"
                        await message.reply(replySTR)

                #425的第四輪對話
                elif mscDICT[message.author.id]["confirm425tb2_BOOL"] == True and mscDICT[message.author.id]["confirm425tb3_BOOL"] != True: #425的第四輪對話
                    lokiResultDICT = botRunLoki(msgSTR,filterLIST = ["425_tb3"]) #filterLIST只跑425_tb3
                    if "confirm425tb3_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm425tb3_BOOL"] = lokiResultDICT["confirm425tb3_BOOL"]
                        if mscDICT[message.author.id]["confirm425tb3_BOOL"] == False:
                            replySTR = "出租人(房東)尚未將租賃物(您的租處)的所有權讓與給他人房東仍然租賃所有權人，您可以繼續向原房東主張租賃關係中的一切權利。不用擔心喔。"
                            mscDICT[message.author.id]["complete"] = True #結束對話
                            await message.reply(replySTR)
                            mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                            await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")

                        elif mscDICT[message.author.id]["confirm425tb3_BOOL"] == True:
                            replySTR = """根據民法第425條第1項的規定，您的租賃契約對於租賃物的新所有人(新屋主)仍然繼續存在。
                                       新的屋主會成為您的新房東(新的出租人)，您可以依原本的租賃契約繼續就租賃物為使用收益，不用擔心。""".replace(" ","").replace("\n","")
                            mscDICT[message.author.id]["complete"] = True #結束對話
                            await message.reply(replySTR)
                            mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                            await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")
                    else: #聽不懂
                        replySTR = "抱歉，我有點不太懂您的意思，可以請您換一個說法再說一遍嗎？謝謝。"
                        await message.reply(replySTR)

                #429修繕義務的問題
                elif mscDICT[message.author.id]["confirm429_BOOL"] == True: #429的第二輪對話
                    lokiResultDICT = botRunLoki(msgSTR,filterLIST = ["429_tb1"]) #filterLIST只跑429_tb1
                    if "confirm429tb1_BOOL" in lokiResultDICT:
                        mscDICT[message.author.id]["confirm429tb1_BOOL"] = lokiResultDICT["confirm429tb1_BOOL"]
                        if mscDICT[message.author.id]["confirm429tb1_BOOL"] == False:
                            replySTR = """根據民法第429條第1項的規定，如果您與房東之間沒有特別約定由您負擔修繕義務，則出租人(房東)應負擔修繕租賃物的義務。
                                       所以您可以定相當期限催告房東來修。如果房東沒有在您訂的期限內處理的話，
                                       依據民法第430條，您可以自行修繕，之後再向房東請求償還費用，或是直接在租金中扣除修繕費用。""".replace(" ","").replace("\n","")
                            mscDICT[message.author.id]["complete"] = True #結束對話
                            await message.reply(replySTR)
                            mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                            await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")

                        elif mscDICT[message.author.id]["confirm429tb1_BOOL"] == True:
                            replySTR = "請注意，您的租賃契約上有約定由您自行負擔修繕義務，所以您必須自行修繕您的租賃物喔。"
                            mscDICT[message.author.id]["complete"] = True #結束對話
                            await message.reply(replySTR)
                            mscDICT[message.author.id].clear() #對話結束，清空mscDICT的user資料
                            await message.reply("謝謝您使用本Bot，希望我有幫到您，祝您有個美好的一天！")
                    else:
                        replySTR = "抱歉，我有點不太懂您的意思，可以請您換一個說法再說一遍嗎？謝謝。"
                        await message.reply(replySTR)





if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])

