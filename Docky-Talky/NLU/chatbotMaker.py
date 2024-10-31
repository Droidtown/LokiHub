#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import aiohttp
import logging
from .common import AccountManager

# API_KEY = "your_openai_api_key"  # Replace with your actual API key
API_URL = "https://api.openai.com/v1/chat/completions"  # OpenAI API endpoint

class ConversationManager:
    def __init__(self, account_manager):
        self.conversation_history = []
        self._account_manager = account_manager
        self.similarity_documents = None
        self.extracted_text = None       
        self.query = None

    def insert_data(self, similarity_documents=None, extracted_text=None):
        self.similarity_documents = similarity_documents
        self.extracted_text = extracted_text

    async def generate_response(self, query):
        if self.similarity_documents:
            user_input = f"{self.similarity_documents}\n + Q：{
                query}? + \nAccording to the provided data below, please answer the question in traditional Chinese used in Taiwan."
        else:
            # Use extracted_text if similarity_documents is not available
            user_input = f"{self.extracted_text}\n + Q：{query}? + \nAccording to the provided data below, please answer the question in traditional Chinese used in Taiwan."        
        # Update the conversation history with user input
        self.conversation_history.append(
            {"role": "user", "content": user_input})
    
        # Prepare payload with conversation history and query
        payload = {
            "model": "gpt-4o",
            "messages": self.conversation_history
        }
    
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._account_manager.openAI_api_key}"
        }
    
        # Make the API request to OpenAI using aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    bot_response = data["choices"][0]["message"]["content"]
    
                    # Append the assistant's response to the conversation history
                    self.conversation_history.append(
                        {"role": "assistant", "content": bot_response})
    
                    # Extract token usage information
                    total_tokens = data["usage"]["total_tokens"]
                    completion_tokens = data["usage"]["completion_tokens"]
    
                    # Check token usage and warn the user if necessary
                    if total_tokens <= completion_tokens:
                        print("Warning: Your total tokens are equal to or less than the completion tokens. You might not have enough tokens for the next request.")
    
                    return bot_response
    
                else:
                    logging.error(f"API request failed with status code {response.status}: {await response.text()}")
                    return "Sorry, I couldn't process that request."

    def get_conversation_history(self):
        return self.conversation_history

if __name__ == "__main__":
    account_manager = AccountManager(filename="config/account.info")
    conversation_manager = ConversationManager(account_manager)
    
    dummy_similarity_documents = "2024年巴黎奧運揭幕花都聚集了來自全球各地的運動員和爭睹頂級賽事的觀眾然而這卻讓部分巴黎居民心生怨懟近幾個月來社群媒體可見到部分巴黎民眾對法國首都的狀態抱怨連連有些居民形容巴黎正成為人間地獄警告遊客千萬別來相較於巴黎市政府堅稱奧運取得巨大成功為何巴黎人反而成群結隊地想逃離這座城市訂閱年方案享雙重好禮 前100位加贈電子書 抽日本雙人來回機票還不是會員"
    conversation_manager.insert_data(
        similarity_documents=dummy_similarity_documents)
    test_query = "巴黎市政府做了甚麼?"
    response = conversation_manager.generate_response(query=test_query)
    print(response)