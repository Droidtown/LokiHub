#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from .common import AccountManager, CrawledDataManager
from pprint import pprint
import aiohttp
import json
from time import sleep
import asyncio

url = "https://api.droidtown.co/Loki/Call/"  # 線上版 URL
POST_INTERVAL_SEC = 5

"""
功能：負責與NeuroKumoko分類模型的交互，處理文本數據並生成分類結果。
主要內容：
1. 加載轉換後的文本。
2. 調用NeuroKumoko模型，傳遞文本數據並接收分類結果。
3. 生成文本的分類標簽和大綱。
"""

class NeuroKumokoManager:
    def __init__(self, account_manager, url=None):
        self._account_manager = account_manager
        self.url = url or "https://api.droidtown.co/Loki/Call/"
        self.crawled_data_manager = CrawledDataManager(
            directory="data",
            parser=self
        )
        self.loki_key = None  # 存儲生成的 loki_key

    # Handle the HTTP POST requests. Shared by all other functions to communicate with NeuroKumoko API
    async def _make_request(self, func, data, loki_key=None, use_loki_key=True):
        payload = {
            "username": self._account_manager.username,
            "func": func,
            "data": data
        }
        
        print(f"\npayload: {payload}")

        if use_loki_key:
            loki_key = loki_key or self.loki_key or self._account_manager.loki_key
            if isinstance(loki_key, str) and loki_key:
                payload["loki_key"] = loki_key
            else:
                raise ValueError("Invalid or missing loki_key.")

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as response:
                return await response.json()

    # Create a NeuroKumoko project using the API
    async def create_project(self, project_name, loki_key=None):
        data = {
            "name": project_name,
            "type": "neuro_kumoko"
        }
        response = await self._make_request(
            "create_project", data, loki_key=loki_key, use_loki_key=False)
        loki_key = response.get("loki_key")
        if isinstance(loki_key, str) and loki_key:
            # Update loki_key in account.info
            self._account_manager.update_key("loki_key", loki_key)
            self.loki_key = loki_key  # 存儲生成的 loki_key
            print(f"Updated loki_key: {self.loki_key}")
        else:
            raise ValueError(
                "Failed to retrieve a valid loki_key from the response.")        
        pprint(response)
        return response

    # Add documents to the NeuroKumoko project
    async def add_documents(self, filename=None):
        # Get parsed content from CrawledDataManager
        documents = self.crawled_data_manager.parse_content(
            filename=filename)

        print(f"document type: {type(documents)}")

        data = {"document": documents}

        print("Data start from here: \n")
        # print(data)
        # Check if data is properly formatted
        response = await self._make_request("insert_document", data)
        # pprint(response)
        return response

    # Deploy the model for the NeuroKumoko project
    async def deploy_model(self):
        response = await self._make_request("deploy_model", {})
        pprint(response)
        return response

    # Check the deployment status of the model
    async def check_model_status(self):
        response = await self._make_request("check_model", {})
        pprint(response)
        return response

    # Retrieve detailed information about the deployed model
    async def get_model_info(self):
        response = await self._make_request("get_info", {})

        # test
        #response = {
            #"msg": "Model is deploying...",
            #"progress_status": "processing",
            #"status": "true"
        #}
        
        # pprint(response)
        return response

    # Get text similarity using the Loki API
    async def get_loki_text_sim(self, input_str, loki_key=None, keyword_list=[], feature_list=["feature_time", "feature_unit", "feature_noun",
            "feature_verb", "feature_location", "feature_person"], count=1):
        payload = {
            "username": self._account_manager.username,
            "loki_key": loki_key,
            "input_str": input_str,
            "keyword": keyword_list,
            "feature": feature_list,
            "count": count
        }

        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post("https://api.droidtown.co/Loki/API/", json=payload) as response:
                    if response.status == 200:
                        try:
                            result = await response.json()
                            if result["status"]:
                                if result["progress_status"] == "processing":
                                    await asyncio.sleep(POST_INTERVAL_SEC)
                                    continue
                            return result
                        except Exception as e:
                            return {"status": False, "msg": str(e)}
                    else:
                        return {"status": False, "msg": "HTTP {}".format(response.status)}

    async def build_model(self, project_name):
        await self.create_project(project_name)
        await self.add_documents()
        await self.deploy_model()
        await self.check_model_status()
        await self.get_model_info()

    async def poll_model_status(self, project_name, delay=5, max_retries=10):
        retries = 0

        label_dict = (await self.get_model_info()).get("result", {}).get("label", {})

        # Print the label_dict for debugging
        print("Label dictionary:", label_dict)
        
        label_count = len(label_dict)
        if label_count < 2:
            print("Build Model! document_count should larger than 2!")
            await self.build_model(project_name)
            return False

        progress_status = (await self.check_model_status()).get("progress_status")
        while progress_status != "completed" and retries < max_retries:
            retries += 1
            await asyncio.sleep(delay)
            
            progress_status = (await self.check_model_status()).get("progress_status")

            if retries == max_retries:
                print("Max retries reached. Exiting poll.")
                return False

        return True

    def extract_lexicon_values(self, response_data):
        # Check 'results' if exists and is list
        if 'results' in response_data and isinstance(response_data['results'], list):
            for item in response_data['results']:
                # check each item if contains 'lexicon'
                if 'lexicon' in item:
                    return item['lexicon']
        return None

async def main():
    account_manager = AccountManager(filename="config/account.info")
    neurokumoko_manager = NeuroKumokoManager(account_manager)
    
    await neurokumoko_manager.create_project("PDF_classfication")
    
    print(f"neurokumoko_manager.loki_key: {neurokumoko_manager.loki_key}")
    
    extracted_text = "2024 年巴黎奧運揭幕花都聚集了來自全球各地的運動員和爭睹頂級賽事的觀眾然而這卻讓部分巴黎居民心生怨懟近幾個月來社群媒體可見到部分巴黎民眾對法國首都的狀態抱怨連連有些居民形容巴黎正成為人間地獄警告遊客千萬別來相較於巴黎市政府堅稱奧運取得巨大成功為何巴黎人反而成群結隊地想逃離這座城市"
    res = await neurokumoko_manager.get_loki_text_sim(
        extracted_text, loki_key=neurokumoko_manager.loki_key)
    flag = await neurokumoko_manager.poll_model_status("PDF_classfication")
    if flag:
        print(f"neurokumoko_manager.loki_key: {
              neurokumoko_manager.loki_key}")
        res = await neurokumoko_manager.get_loki_text_sim(extracted_text, loki_key=neurokumoko_manager.loki_key)
        print(res)
    print(res)
    if res:
        print(f'Extracted Text from {attachment.filename}:')
        lexicon_values = neurokumoko_manager.extract_lexicon_values(res)
        print(lexicon_values)


if __name__ == "__main__":
    asyncio.run(main())



