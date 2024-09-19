#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from .common import AccountManager, CrawledDataManager
from requests import post
from pprint import pprint
import requests
import json
from time import sleep


url = "https://api.droidtown.co/Loki/Call/"  # 線上版 URL
POST_INTERVAL_SEC = 5

"""
功能：負責與GreedySlime分群模型的交互，處理文本數據並生成分群結果。
主要內容：
1. 加載轉換後的文本。
2. 調用GreedySlime模型，傳遞文本數據並接收分群結果。
3. 生成文本的分群摘要和相關信息。
"""


class GreedySlimeManager:
    def __init__(self, account_manager, url=None):
        self._account_manager = account_manager
        self.url = url or "https://api.droidtown.co/Loki/Call/"
        self.crawled_data_manager = CrawledDataManager(
            directory="data",
            parser=self
        )

    def _make_request(self, func, data, use_loki_key=True):
        payload = {
            "username": self._account_manager.username,
            "func": func,
            "data": data
        }

        if use_loki_key:
            loki_key = self._account_manager.loki_key
            if isinstance(loki_key, str) and loki_key:
                payload["loki_key"] = loki_key
            else:
                raise ValueError("Invalid or missing loki_key.")

        response = post(self.url, json=payload)
        return response.json()

    def create_project(self, project_name):
        data = {
            "name": project_name,
            "type": "greedy_slime"
        }
        response = self._make_request(
            "create_project", data, use_loki_key=False)
        loki_key = response.get("loki_key")
        if isinstance(loki_key, str) and loki_key:
            # 更新 account_gs.info 文件中的 loki_key
            self._account_manager.update_key("loki_key", loki_key)
        else:
            raise ValueError(
                "Failed to retrieve a valid loki_key from the response.")
        # pprint(response)
        return response

    def add_documents(self, filename=None):
        print(f"Filename passed to parse_content: {filename}")

        # Get parsed content from CrawledDataManager
        documents = self.crawled_data_manager.parse_content(
            filename=filename)

        print(f"document type: {type(documents)}")
        data = {"document": documents}

        # print(f"\n{data}")
        response = self._make_request("insert_document", data)
        # pprint(response)

    # Deploy the model for the NeuroKumoko project
    def deploy_model(self):
        response = self._make_request("deploy_model", {})
        # pprint(response)
        return response

    # Check the deployment status of the model
    def check_model_status(self):
        response = self._make_request("check_model", {})
        # pprint(response)
        return response

    # Retrieve detailed information about the deployed model
    def get_model_info(self):
        response = self._make_request("get_info", {})
        # pprint(response)
        return response

    def extract_and_transform_clusters(self):
        transformed_data = []
    
        while True:
            # Get the model info
            model_info = self.get_model_info()
            
            # Check if the cluster is not empty
            cluster_data = model_info.get('result', {}).get('cluster', {})
            if cluster_data:
                # Iterate through each cluster
                for cluster_name, cluster_details in cluster_data.items():
                    # Use cluster_1, 2, 3... as title
                    title = f"{cluster_name}"
                    
                    for content in cluster_details.get('source', []):
                        transformed_data.append({
                            "title": title,
                            "content": content,
                            # Use "key_info" to replace "hashtag"
                            "hashtag": cluster_details.get('key_info', [])
                        })
                
                # Break out of the loop since we've retrieved the necessary data
                break
            
            # If the cluster is still empty, wait before trying again
            time.sleep(2)  # Wait for 2 seconds before trying again
    
        return transformed_data            

    # Get text Clustering using the Loki API
    def get_loki_text_sim(self, input_str, keyword_list=[], feature_list=[], count=1):
        payload = {
            "username": self._account_manager.username,
            "loki_key": self._account_manager.loki_key,
            "input_str": input_str,
            "keyword": keyword_list,
            "feature": feature_list,
            "count": count
        }

        while True:
            response = requests.post("https://api.droidtown.co/Loki/API/", json=payload)
            if response.status_code == 200:
                try:
                    result = response.json()
                    if result["status"]:
                        if result["progress_status"] == "processing":
                            sleep(POST_INTERVAL_SEC)
                            continue
                    return result
                except Exception as e:
                    return {"status": False, "msg": str(e)}
            else:
                return {"status": False, "msg": "HTTP {}".format(response.status_code)}        
    
    def build_model(self, filename):
        self.create_project(f"GS_{filename}")
        self.add_documents(filename)
        self.deploy_model()
        self.check_model_status()
        self.get_model_info()
