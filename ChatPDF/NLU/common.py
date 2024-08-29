#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import re


# 特殊符號列表
splitLIST = ["！", "，", "。", "？", "!", ",",
    "\n", "；", "\u3000", ";", "｜", "▸", "▪", "#"]

class AccountManager:
    def __init__(self, filename="config/account.info"):
        self._filename = filename
        self._username = None
        self._apikey = None

    def read_account_info(self):
        account_info = {}
        try:
            with open(self._filename, 'r') as file:
                # Load the entire file as a JSON object
                account_info = json.load(file)
        except FileNotFoundError:
            print(f"Error: Account info file '{self._filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{self._filename}'.")
        except Exception as e:
            print(f"Error reading account info: {str(e)}")
        return account_info

    @property
    def username(self):
        if not self._username:
            account_info = self.read_account_info()
            self._username = account_info.get('username', '')
        return self._username

    @property
    def apikey(self):
        if not self._apikey:
            account_info = self.read_account_info()
            self._apikey = account_info.get('api_key', '')
        return self._apikey
    
    @property
    def loki_key(self):
        account_info = self.read_account_info()
        return account_info.get('loki_key', '')
    
    @property
    def copytoaster_key(self):
        account_info = self.read_account_info()
        return account_info.get('copytoaster_key', '')
    
    @property
    def openAI_api_key(self):
        account_info = self.read_account_info()
        return account_info.get('openAI_api_key', '')
    
    def update_key(self, key_type, new_key):
        if not isinstance(new_key, str) or not new_key:
            raise ValueError(
                f"Invalid {key_type}. It must be a non-empty string.")
    
        with open(self._filename, "r+", encoding="utf-8") as file:
            account_data = json.load(file)
            if key_type not in account_data:
                raise KeyError(f"{key_type} not found in account data.")
    
            account_data[key_type] = new_key
            file.seek(0)
            json.dump(account_data, file, indent=4)
            file.truncate()

    def _get_unused_key(self, key_type):
        with open("config/account.info", "r+", encoding="utf-8") as file:
            account_data = json.load(file)
            if key_type in account_data:
                for key_data in account_data[key_type]:
                    if not key_data.get("used", False):
                        # Mark as used
                        key_data["used"] = True
                        file.seek(0)
                        json.dump(account_data, file, indent=4)
                        file.truncate()
                        return key_data["key"]
            raise ValueError(
                f"No unused {key_type} available in account_gs.info")


class CrawledDataManager:
    def __init__(self, directory, parser=None):
        self.directory = directory
        self.parser = parser
    
    def load_crawled_data_from_files(self, directory, filename=None):
        json_files = []
        crawled_data = []

        # Get all file_path of .json files
        for root, _, files in os.walk(self.directory):
            for filename in files:
                if filename.endswith(".json"):
                    json_files.append(os.path.join(root, filename))

        # Load data from each file
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding="utf-8") as file:
                    file_data = json.load(file)
                    # Use filename (without extension) as the label key
                    label = os.path.splitext(
                        os.path.basename(json_file))[0]
                    if label not in crawled_data:
                        crawled_data[label] = []
                    crawled_data[label].extend(file_data)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading JSON file {json_file}: {str(e)}")

        return crawled_data

    # 清理文本，去除特殊符號
    def clean_text(self, text, splitLIST):
        # text = re.sub(r'[a-zA-Z]', '', text)
        for char in splitLIST:
            text = text.replace(char, '')
        return text    
    
    def parse_content(self, filename=None):
        crawled_data = {}
        
        if filename and not filename.endswith(".json"):
            filename += ".json"
        
        # Import here to avoid circular import issues, 根據不同的 parser 做額外的處理
        from classification_manager import NeuroKumokoManager
        from clustering_manager import GreedySlimeManager

        print(f"Parser type: {type(self.parser)}")

        crawled_data = self.parse_crawled_data(filename=filename)

        # Process the loaded data
        parsed_results = []
        for label, data_list in crawled_data.items():
            for data in data_list:
                content = data.get("content", "")
                content = self.clean_text(content, splitLIST)
                title = data.get("title", "Untitled")

                # result_dict = {}
                if content:
                    if isinstance(self.parser, NeuroKumokoManager):
                        print("Parser is NeuroKumokoManager")
                        result_dict = {
                            "label": label,
                            "title": title,
                            "content": content,
                            "keyword": []
                        }
                    elif isinstance(self.parser, GreedySlimeManager):
                        print("Parser is GreedySlimeManager")
                        result_dict = {
                            "title": title,
                            "content": content,
                            "keyword": []
                        }
                    else:
                        # Handle the case when the parser is neither NeuroKumokoManager nor GreedySlimeManager
                        print("Parser is neither NeuroKumokoManager nor GreedySlimeManager")
                        result_dict = {
                            "content": content
                        }

                    parsed_results.append(result_dict)

        return parsed_results
    
    def parse_crawled_data(self, filename=None):
        crawled_data = {}

        def load_json_file(filepath):
            try:
                with open(filepath, 'r', encoding="utf-8") as file:
                    file_data = json.load(file)
                    label = os.path.splitext(os.path.basename(filepath))[0]
                    return label, file_data
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading JSON file {filepath}: {str(e)}")
                return None, None

        if filename:
            filepath = os.path.join(self.directory, filename)
            label, file_data = load_json_file(filepath)
            if label and file_data:
                crawled_data[label] = file_data
        else:
            for root, _, files in os.walk(self.directory):
                for filename in files:
                    if filename.endswith(".json"):
                        filepath = os.path.join(root, filename)
                        label, file_data = load_json_file(filepath)
                        if label and file_data:
                            crawled_data[label] = file_data
        return crawled_data

