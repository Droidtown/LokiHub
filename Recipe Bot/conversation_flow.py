#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Conversation Flow Manager
    專門處理料理機器人的對話流程控制
"""

import logging
from main import askLoki
from response_manager import add_response_to_result
from recipe_recommender import RecipeRecommender

class RecipeConversationFlow:
    # 定義對話狀態
    STATES = {
        "COLLECT_INGREDIENTS": "收集食材階段",
        "COLLECT_SERVINGS": "收集份數階段", 
        "COLLECT_TIME": "收集時間限制階段",
        "RECOMMEND_RECIPE": "推薦食譜階段",
        "RECIPE_FEEDBACK": "等待用戶反饋階段"
    }
    
    # 換食譜的關鍵字
    CHANGE_KEYWORDS = ["換", "改", "不要這個", "不喜歡", "重新", "其他", "別的", "換一個", "不要", "再來一個"]
    
    def __init__(self):
        self.recipe_recommender = RecipeRecommender()
    
    def process_user_input(self, user_input, user_session_data):
        """
        處理用戶輸入並管理對話流程
        
        Args:
            user_input (str): 用戶輸入的訊息
            user_session_data (dict): 用戶的會話資料
            
        Returns:
            tuple: (new_state, response_messages, updated_session_data)
        """
        current_state = user_session_data.get("state", "COLLECT_INGREDIENTS")
        collected_data = user_session_data.get("collected_data", {
            "ingredients": [],
            "servings": {},
            "time_limit": {}
        })
        
        logging.debug(f"當前狀態: {current_state}")
        logging.debug(f"已收集資料: {collected_data}")
        
        try:
            if current_state == "COLLECT_INGREDIENTS":
                return self._handle_ingredients_stage(user_input, user_session_data, collected_data)
                
            elif current_state == "COLLECT_SERVINGS":
                return self._handle_servings_stage(user_input, user_session_data, collected_data)
                
            elif current_state == "COLLECT_TIME":
                return self._handle_time_stage(user_input, user_session_data, collected_data)
                
            elif current_state == "RECOMMEND_RECIPE":
                return self._handle_recipe_recommendation(user_input, user_session_data, collected_data)
                
            elif current_state == "RECIPE_FEEDBACK":
                return self._handle_recipe_feedback(user_input, user_session_data, collected_data)
                
            else:
                # 未知狀態，重置到初始階段
                return self._reset_conversation(user_session_data)
                
        except Exception as e:
            logging.error(f"對話流程處理錯誤: {e}")
            # 發生錯誤時提供友善回應但保持狀態
            return current_state, ["抱歉，系統發生了一些問題，請再試一次。"], user_session_data

    def _handle_ingredients_stage(self, user_input, session_data, collected_data):
        """處理食材收集階段"""
        # 使用 Loki 分析用戶輸入
        resultDICT = askLoki(user_input)
        
        # 檢查是否識別到食材
        if "ingredients" in resultDICT and resultDICT["ingredients"]:
            # 更新收集的資料
            collected_data["ingredients"] = resultDICT["ingredients"]
            
            # 使用 response_manager 生成回覆
            resultDICT["intent"] = "ingredient_input"
            response_result = add_response_to_result(resultDICT)
            response_message = response_result.get("response", "好的，已記錄食材。請問要做幾人份？")
            
            # 確保 response_message 是字串格式
            if isinstance(response_message, list):
                response_message = response_message[0] if response_message else "好的，已記錄食材。請問要做幾人份？"
            
            logging.debug(f"生成的回覆訊息: {response_message}")
            logging.debug(f"回覆訊息類型: {type(response_message)}")
            
            # 轉到下一階段
            new_state = "COLLECT_SERVINGS"
            updated_session = session_data.copy()
            updated_session["collected_data"] = collected_data
            updated_session["latestQuest"] = response_message
            
            return new_state, [response_message], updated_session
            
        else:
            # 沒有識別到有效食材
            response_message = "不好意思，我不太理解你的意思，可以換句話說嗎？"
            return "COLLECT_INGREDIENTS", [response_message], session_data

    def _handle_servings_stage(self, user_input, session_data, collected_data):
        """處理份數收集階段"""
        # 預處理：檢查是否包含服務單位關鍵字
        serving_keywords = ["人", "個人", "人份", "份", "口"]
        has_serving_keyword = any(keyword in user_input for keyword in serving_keywords)
        
        # 使用 Loki 分析用戶輸入
        resultDICT = askLoki(user_input)
        logging.debug(f"Loki 完整結果: {resultDICT}")
        
        # 檢查是否識別到份數
        if "servings" in resultDICT and resultDICT["servings"]:
            logging.debug(f"Loki 識別到份數: {resultDICT['servings']}")
            
            # 檢查 servings 資料是否有效
            servings_data = resultDICT["servings"]
            valid_serving = None
            
            if isinstance(servings_data, list) and len(servings_data) > 0:
                for serving_item in servings_data:
                    if isinstance(serving_item, dict) and "count" in serving_item:
                        valid_serving = serving_item
                        break
            elif isinstance(servings_data, dict) and "count" in servings_data:
                valid_serving = servings_data
            
            if valid_serving and valid_serving.get("count"):
                # 找到有效的份數資料
                collected_data["servings"] = valid_serving
                
                # 構建正確的 resultDICT 給 response_manager
                clean_resultDICT = {
                    "intent": "serving_input",
                    "servings": valid_serving
                }
                response_result = add_response_to_result(clean_resultDICT)
                response_message = response_result.get("response", "好的，已記錄份數。預計多久上菜呢？")
                
                # 確保 response_message 是字串格式
                if isinstance(response_message, list):
                    response_message = response_message[0] if response_message else "好的，已記錄份數。預計多久上菜呢？"
                
                logging.debug(f"使用 Loki 資料生成回覆: {response_message}")
                
                # 轉到下一階段
                new_state = "COLLECT_TIME"
                updated_session = session_data.copy()
                updated_session["collected_data"] = collected_data
                updated_session["latestQuest"] = response_message
                
                return new_state, [response_message], updated_session
            else:
                logging.debug(f"Loki 份數資料無效，轉為手動解析")
                # Loki 識別到 servings 但資料無效，轉到手動解析
            
        elif has_serving_keyword:
            # Loki 沒有識別到份數，但有服務單位關鍵字，嘗試手動解析
            logging.debug(f"Loki 未識別到有效份數，但檢測到服務單位關鍵字")
            logging.debug(f"has_serving_keyword: {has_serving_keyword}")
            logging.debug(f"嘗試手動解析: {user_input}")
            
            manual_serving = self._manual_parse_serving(user_input)
            logging.debug(f"手動解析結果: {manual_serving}")
            
            if manual_serving:
                collected_data["servings"] = {"count": manual_serving}
                
                # 手動構建正確的 resultDICT 給 response_manager
                manual_resultDICT = {
                    "intent": "serving_input",
                    "servings": {"count": manual_serving}
                }
                logging.debug(f"手動構建的 resultDICT: {manual_resultDICT}")
                
                response_result = add_response_to_result(manual_resultDICT)
                logging.debug(f"response_manager 回傳結果: {response_result}")
                
                response_message = response_result.get("response", f"{manual_serving}人份，沒問題！預計多久上菜呢？")
                logging.debug(f"提取的回覆訊息: {response_message}")
                
                # 確保 response_message 是字串格式
                if isinstance(response_message, list):
                    response_message = response_message[0] if response_message else f"{manual_serving}人份，沒問題！預計多久上菜呢？"
                
                # 轉到下一階段
                new_state = "COLLECT_TIME"
                updated_session = session_data.copy()
                updated_session["collected_data"] = collected_data
                updated_session["latestQuest"] = response_message
                
                logging.debug(f"手動解析成功: {manual_serving}人份，最終回覆: {response_message}")
                return new_state, [response_message], updated_session
            else:
                # 有關鍵字但無法解析出數量
                response_message = "請告訴我具體要做幾人份呢？例如：2人份、三人份"
                return "COLLECT_SERVINGS", [response_message], session_data
        else:
            # 沒有識別到份數也沒有關鍵字
            logging.debug(f"未檢測到服務單位關鍵字，且 Loki 未識別到份數")
            response_message = "不好意思，我不太理解你的意思，可以換句話說嗎？"
            return "COLLECT_SERVINGS", [response_message], session_data

    def _handle_time_stage(self, user_input, session_data, collected_data):
        """處理時間限制收集階段"""
        # 使用 Loki 分析用戶輸入
        resultDICT = askLoki(user_input)
        
        # 檢查是否識別到時間限制
        if "time_limit" in resultDICT and resultDICT["time_limit"]:
            # 更新收集的資料 - 確保格式正確
            if isinstance(resultDICT["time_limit"], list) and len(resultDICT["time_limit"]) > 0:
                collected_data["time_limit"] = resultDICT["time_limit"][0]  # 取第一個元素
            else:
                collected_data["time_limit"] = resultDICT["time_limit"]
            
            # 收集完所有資料，直接生成 LLM 食譜推薦
            new_state = "RECIPE_FEEDBACK"  # 直接進入反饋階段
            updated_session = session_data.copy()
            updated_session["collected_data"] = collected_data
            
            # 生成食譜推薦
            return self._generate_recipe_recommendation(new_state, updated_session, collected_data)
            
        else:
            # 沒有識別到有效時間限制
            response_message = "不好意思，我不太理解你的意思，可以換句話說嗎？"
            return "COLLECT_TIME", [response_message], session_data

    def _handle_recipe_recommendation(self, user_input, session_data, collected_data):
        """處理食譜推薦階段（重定向到反饋階段）"""
        # 這個階段現在不應該被調用，因為我們直接跳到 RECIPE_FEEDBACK
        # 如果到達這裡，重新生成推薦
        return self._generate_recipe_recommendation("RECIPE_FEEDBACK", session_data, collected_data)

    def _handle_recipe_feedback(self, user_input, session_data, collected_data):
        """處理用戶對食譜的反饋"""
        user_input_lower = user_input.lower().strip()
        
        # 檢查是否要換食譜
        wants_change = self._check_wants_change_recipe(user_input_lower)
        
        if wants_change:
            # 用戶要換食譜，生成新的推薦
            logging.debug("用戶要求換食譜")
            
            # 將當前推薦的食譜加入排除清單
            current_recipe = session_data.get("last_recipe")
            excluded_recipes = session_data.get("excluded_recipes", [])
            if current_recipe and current_recipe not in excluded_recipes:
                excluded_recipes.append(current_recipe)
            
            # 生成新的食譜推薦
            try:
                recipe_messages = self.recipe_recommender.generate_recipe(
                    ingredients=collected_data["ingredients"],
                    servings=collected_data["servings"],
                    time_limit=collected_data["time_limit"],
                    excluded_recipes=excluded_recipes
                )
                
                # 更新會話資料
                updated_session = session_data.copy()
                updated_session["excluded_recipes"] = excluded_recipes
                
                # 從第一條訊息中提取食譜名稱（簡單方式：取第一行的【】內容）
                if recipe_messages:
                    first_line = recipe_messages[0].split('\n')[0]
                    if '【' in first_line and '】' in first_line:
                        recipe_name = first_line.split('【')[1].split('】')[0]
                        updated_session["last_recipe"] = recipe_name
                
                # 保持在反饋階段，等待用戶再次反饋
                return "RECIPE_FEEDBACK", recipe_messages, updated_session
                
            except Exception as e:
                logging.error(f"生成新食譜時發生錯誤: {e}")
                return "RECIPE_FEEDBACK", ["抱歉，無法生成新的食譜推薦，請稍後再試。"], session_data
                
        else:
            # 用戶接受食譜，結束對話
            logging.debug("用戶接受食譜，結束對話")
            end_message = "很高興幫上你的忙！"
            
            # 重置會話狀態
            updated_session = self._create_fresh_session(session_data["id"])
            
            return "COLLECT_INGREDIENTS", [end_message], updated_session

    def _generate_recipe_recommendation(self, target_state, session_data, collected_data):
        """生成食譜推薦 - 直接使用 LLM，不使用預設模板"""
        try:
            excluded_recipes = session_data.get("excluded_recipes", [])
            
            recipe_messages = self.recipe_recommender.generate_recipe(
                ingredients=collected_data["ingredients"],
                servings=collected_data["servings"],
                time_limit=collected_data["time_limit"],
                excluded_recipes=excluded_recipes
            )
            
            # 更新會話資料
            updated_session = session_data.copy()
            updated_session["collected_data"] = collected_data
            
            # 從第一條訊息中提取食譜名稱
            if recipe_messages:
                first_line = recipe_messages[0].split('\n')[0]
                if '【' in first_line and '】' in first_line:
                    recipe_name = first_line.split('【')[1].split('】')[0]
                    updated_session["last_recipe"] = recipe_name
                    logging.debug(f"記錄食譜名稱: {recipe_name}")
            
            # 直接轉到反饋階段
            return "RECIPE_FEEDBACK", recipe_messages, updated_session
            
        except Exception as e:
            logging.error(f"生成食譜推薦時發生錯誤: {e}")
            # 發生錯誤時也不使用模板，而是提供簡單的錯誤回應
            error_message = "抱歉，無法生成食譜推薦，請稍後再試。"
            return "COLLECT_INGREDIENTS", [error_message], session_data

    def _check_wants_change_recipe(self, user_input_lower):
        """檢查用戶是否想要換食譜"""
        for keyword in self.CHANGE_KEYWORDS:
            if keyword in user_input_lower:
                return True
        return False

    def _reset_conversation(self, session_data):
        """重置對話到初始狀態"""
        reset_message = "讓我們重新開始吧！請告訴我你有什麼食材？"
        updated_session = self._create_fresh_session(session_data["id"])
        return "COLLECT_INGREDIENTS", [reset_message], updated_session

    def _create_fresh_session(self, user_id):
        """創建全新的會話資料"""
        from datetime import datetime
        return {
            "id": user_id,
            "updatetime": datetime.now(),
            "latestQuest": "",
            "false_count": 0,
            "state": "COLLECT_INGREDIENTS",
            "collected_data": {
                "ingredients": [],
                "servings": {},
                "time_limit": {}
            },
            "last_recipe": None,
            "excluded_recipes": []
        }

    def _manual_parse_serving(self, user_input):
        """手動解析份數，作為 Loki 識別失敗的備援"""
        import re
        
        # 移除空白字符，轉小寫
        text = user_input.strip().lower()
        
        # 中文數字對應
        chinese_numbers = {
            '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
            '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
            '兩': 2, '倆': 2
        }
        
        # 嘗試匹配各種份數格式
        patterns = [
            r'(\d+)\s*人份?',        # "2人份", "3人份"
            r'([一二三四五六七八九十兩倆])\s*人份?',  # "兩人份", "三人份"
            r'(\d+)\s*份',           # "2份", "3份"
            r'([一二三四五六七八九十兩倆])\s*份',      # "兩份", "三份"
            r'(\d+)',                # 純數字
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                num_str = match.group(1)
                
                # 如果是數字
                if num_str.isdigit():
                    return int(num_str)
                
                # 如果是中文數字
                elif num_str in chinese_numbers:
                    return chinese_numbers[num_str]
        
        return None

    def get_state_description(self, state):
        """獲取狀態的中文描述"""
        return self.STATES.get(state, "未知狀態")


if __name__ == "__main__":
    """測試 RecipeConversationFlow"""
    import logging
    from datetime import datetime
    logging.basicConfig(level=logging.DEBUG)
    
    # 模擬用戶會話資料
    mock_session = {
        "id": "test_user_123",
        "updatetime": datetime.now(),
        "latestQuest": "",
        "false_count": 0,
        "state": "COLLECT_INGREDIENTS",
        "collected_data": {
            "ingredients": [],
            "servings": {},
            "time_limit": {}
        },
        "last_recipe": None,
        "excluded_recipes": []
    }
    
    # 創建對話流程管理器
    flow = RecipeConversationFlow()
    
    # 模擬對話流程
    test_inputs = [
        "我有番茄和雞蛋",
        "兩人份",
        "30分鐘",
        "換一個",
        "好的"
    ]
    
    print("=== 測試對話流程 ===")
    current_session = mock_session.copy()
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\n--- 第 {i} 輪對話 ---")
        print(f"用戶輸入: {user_input}")
        print(f"當前狀態: {flow.get_state_description(current_session.get('state'))}")
        
        # 處理用戶輸入
        new_state, responses, updated_session = flow.process_user_input(user_input, current_session)
        
        print(f"新狀態: {flow.get_state_description(new_state)}")
        print("機器人回應:")
        for response in responses:
            print(f"  {response}")
        
        # 更新會話資料
        current_session = updated_session.copy()
        current_session["state"] = new_state
        
        print(f"已收集資料: {current_session.get('collected_data', {})}")