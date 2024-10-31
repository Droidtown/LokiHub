#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from .common import AccountManager, CrawledDataManager
from requests import post
from pprint import pprint
import requests
import json
from time import sleep


COPYTOASTER_URL = "https://api.droidtown.co/CopyToaster/API/V2/"
POST_INTERVAL_SEC = 5

class CopyToasterManager:
    def __init__(self, account_manager, url=None):
        self._account_manager = account_manager
        self.url = url or "https://api.droidtown.co/CopyToaster/Call/"

    def _make_request(self, func, data=None, category_name=None, use_copytoaster_key=True):
        payload = {
            "username": self._account_manager.username,
            "func": func,
            "data": data
        }
        
        print(payload)
        
        if category_name is not None:
            payload["category"] = category_name

        print(f"\n{payload}")

        if use_copytoaster_key:
            copytoaster_key = self._account_manager.copytoaster_key
            if isinstance(copytoaster_key, str) and copytoaster_key:
                payload["copytoaster_key"] = copytoaster_key
            else:
                raise ValueError("Invalid or missing copytoaster_key.")

        response = post(self.url, json=payload)
        return response.json()

    def create_project(self, project_name):
        data = {
            "name": project_name,
        }
        response = self._make_request(
            "create_project", data, use_copytoaster_key=False)
        copytoaster_key = response.get("copytoaster_key")
        if isinstance(copytoaster_key, str) and copytoaster_key:
            # 更新 account_gs.info 文件中的 loki_key
            self._account_manager.update_key(
                "copytoaster_key", copytoaster_key)
        else:
            raise ValueError(
                "Failed to retrieve a valid copytoaster_key from the response.")
        pprint(response)
        return response
    
    def create_category(self, category_name):
        print(f"Creating category for category_name: {category_name}")

        # Make request to create category
        response = self._make_request(
            "create_category", category_name=category_name, data={})
        pprint(response)    

    def add_documents(self, source, category_name):
        print(f"Adding documents to the category")
    
        # Assume source is the parsed content you want to add as documents
        documents = source
    
        print(f"Document type: {type(documents)}")
        data = {"document": documents}
        #data = {"document": [
            #{'title': 'cluster_41', 'content': '未來一年借房貸恐變難...交報告後還有這關 銀行圈 這次楊金龍是玩真的', 'hashtag': []}]}
    
        # print(f"\n{data}")
        # Make request to insert documents
        response = self._make_request(
            "insert_document", data=data, category_name=category_name)
        pprint(response)

    # Deploy the model for the NeuroKumoko project
    def deploy_model(self):
        response = self._make_request("deploy_model", {})
        pprint(response)
        return response

    # Check the deployment status of the model
    def check_model_status(self):
        response = self._make_request("check_model", {})
        pprint(response)
        return response

    # Retrieve detailed information about the deployed model
    def get_model_info(self):
        response = self._make_request("get_info", {})
        pprint(response)
        return response

    def build_model(self, filename, source):
        self.create_project("PDF_Answers")
        self.create_category(filename)
        self.add_documents(source, filename)
        self.deploy_model()
        self.check_model_status()
        self.get_model_info()

    def getCopyToasterResult(self, categorySTR, inputSTR, count=15):
        payloadDICT = {
            "username": self._account_manager.username,
            "copytoaster_key": self._account_manager.copytoaster_key,
            "category": categorySTR,
            "input_str": inputSTR,
            "count": count
        }
        
        print(payloadDICT)
    
        while True:
            response = post(COPYTOASTER_URL, json=payloadDICT)
            if response.status_code == 200:
                try:
                    resultDICT = response.json()
                    if resultDICT["status"]:
                        if resultDICT["progress_status"] == "processing":
                            sleep(POST_INTERVAL_SEC)
                            continue
                    return resultDICT
                except Exception as e:
                    return {"status": False, "msg": str(e)}
            else:
                return {"status": False, "msg": "HTTP {}".format(response.status_code)}

    def extract_category_documents(self, response_data):
        result_list = response_data.get('result_list', [])
        if result_list:
            document = result_list[0].get('document', '')
            #print(document)
            # 从 \n 后开始取
            document_parts = document.split('>>', 1)
            if len(document_parts) > 1:
                extracted_text = document_parts[1]
            else:
                extracted_text = document  # 如果没有 \n，则取完整文本

            # print(extracted_text)
            return extracted_text
        else:
            print("No results found.")
            
if __name__ == "__main__":
    account_manager = AccountManager(filename="config/account.info")
    copyToater_manager = CopyToasterManager(account_manager)
    lexicon_values = "international_media"
    extracted_text = "2024 年巴黎奧運揭幕花都聚集了來自全球各地的運動員和爭睹頂級賽事的觀眾然而這卻讓部分巴黎居民心生怨懟近幾個月來社群媒體可見到部分巴黎民眾對法國首都的狀態抱怨連連有些居民形容巴黎正成為人間地獄警告遊客千萬別來相較於巴黎市政府堅稱奧運取得巨大成功為何巴黎人反而成群結隊地想逃離這座城市訂閱年方案享雙重好禮前100 位加贈電子書 抽日本雙人來回機票還不是會員 馬上註冊  立即搶購巴黎奧運儼然成為巴黎市長伊達戈與總統馬克宏明爭暗鬥的擂臺開幕典禮上馬克宏以東道主身分站C 位開幕前一周伊達戈縱身躍入塞納河證明水質符合奧運標準替巴黎奧運做了最佳宣傳馬克宏不落人後派出體育部長跟進再次掛保證伊達戈究竟是何許人馬克宏為何這麼在意她2024 年巴黎奧運在法國當地時間晚間7 時30 分正式登場開幕式首度搬到塞納河上舉行聖火由法國3 屆奧運柔道金牌得主希內與田徑名將佩雷克共同點燃隨後聖火台藉氫氣球冉冉升空直到閉幕為止巴黎奧運開幕式今晚（台灣時間27 日凌晨1 時30 分）在塞納河登場四度參賽的女子羽球選手戴資穎、首度站上奧運殿堂的霹靂舞選手孫振將共同擔任掌旗官帶領台灣代表團入場24 歲的孫振在取得巴黎奧運霹靂舞資格後不僅成為各界關注焦點也讓霹靂舞（Breaking）這項年輕人熟悉、但對奧運來說相對陌生的新項目映入觀眾眼簾四年一度的奧運在法國巴黎舉行迎接這項全球最大的運動盛會自然也多了許多「一月運動迷」因此衍生出來的商機更不容小覷由於民眾觀看賽事的需求與欲望比平常更為強烈超商、百貨都祭出不少優惠電商也表示有特定商品買氣大漲...法國7 月7 日舉行國會大選選後新國會呈現左中右三派鼎立席次最多的左翼聯盟要求組閣內部卻分裂無法推出總理人選而總統馬克宏上周接受總理艾塔爾帶領的內閣總辭卸任政府繼續看守負責日常事務但無法提出重大政策眼見巴黎奧運即將在7 月26 日開幕法國政局卻陷入癱瘓民眾抱怨生活成本危機但不知道要等到那一天才會有個像樣的新政府提出因應對策...巴黎奧運將於7 月26 日登場但另一場以長壽為主題的「回春奧運」已如火如荼展開主辦者是「健康來得及」曾報導的科技狂人強生（Bryan Johnson）他年砸數百萬美元進行各種療法與長壽飲食想延緩衰老他還積極將此推廣為運動吸引多達8000 名健康狂熱者一同較量比的是用生理年齡檢測看誰身體衰老速度最慢有趣的是花大錢養生的強生沒能稱霸自己的比賽那些贏過他的「民間高手」是怎麼做到的木匠一個看似消失中的行業能引領精彩人生美國木匠席爾佛（Hank Silver）不久前從波士頓機場出境安檢人員起初好奇他如何拿工作簽證出國聽到他的回答卻肅然起敬他是巴黎聖母院重建修復團隊的國際成員席爾佛並非來自傳統木工家庭他的真實人生是在哪一步轉了彎且朝他心目中「千載難逢」的機會邁進邀請您與聯合報數位版攜手走入國際新聞的世界並檢驗您對全球議題的洞察力2024 巴黎奧運的準備已到最後階段4 年一度的體育盛會即將展開開幕式將乘船入場的選手無不摩拳擦掌期待能從塞納河划向最終勝利的頒獎台聯合報每月企畫「新聞時光機」本次將帶領讀者回顧過往奧運中華健兒的精采故事巴黎奧運柔道男子60公斤級賽事我國好手楊勇緯在16 強賽黃金得分賽險勝卡利諾（Andrea Carlino）後8 強賽則是遭遇強敵哈薩克好手斯梅托夫（Yeldos Smetov）的挑戰最終斯梅托夫以半勝優勢取得4 強門票楊勇緯則落入敗部復活賽仍有機會挑戰銅牌"
    response_data = copyToater_manager.getCopyToasterResult(
        lexicon_values, extracted_text, 1)
    print(response_data)
    similarity_documents = copyToater_manager.extract_category_documents(
        response_data)
    print(f"\nsimilarity_documents: {similarity_documents}")    