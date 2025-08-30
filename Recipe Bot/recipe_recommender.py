#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Recipe Recommender
    專門處理食譜推薦邏輯
"""

import json
import logging
from main import askLLM

class RecipeRecommender:
    def __init__(self):
        self.base_system_prompt = (
            "你是一位專業的料理助手，專門根據現有食材推薦實用的料理，可適量添加基礎調料。"
            "請提供具體的食譜，包含材料用量、步驟說明、烹飪時間。"
            "回應格式要清楚易讀，適合一般家庭料理。回應請用繁體中文。"
        )
        
        self.json_format_example = {
            "recipe_name": "食譜名稱",
            "cooking_time": "烹飪時間", 
            "difficulty": "難度等級",
            "ingredients": [{"name": "食材名稱", "amount": "用量"}],
            "steps": [{"step": 1, "description": "步驟說明"}]
        }
        
        self.default_recipe_template = {
            "recipe_name": "簡單家常料理",
            "cooking_time": "30分鐘",
            "difficulty": "簡單", 
            "ingredients": [],
            "steps": [
                {"step": 1, "description": "將所有食材清洗乾淨"},
                {"step": 2, "description": "依個人喜好調味烹煮"},
                {"step": 3, "description": "完成後即可享用"}
            ]
        }

    def generate_recipe(self, ingredients, servings, time_limit, excluded_recipes=[]):
        """
        生成食譜推薦
        
        Args:
            ingredients (list): 食材列表
            servings (dict): 份數資訊，如 {"count": 2}
            time_limit (dict): 時間限制資訊
            excluded_recipes (list): 要避免的食譜名稱列表
            
        Returns:
            list: 格式化的Discord訊息列表
        """
        try:
            # 構建完整的 system prompt
            system_prompt = self._build_complete_prompt(ingredients, servings, time_limit, excluded_recipes)
            
            # 調用 LLM
            user_prompt = f"請推薦一道使用 {', '.join(ingredients)} 的料理食譜。"
            llm_response = askLLM(system=system_prompt, user=user_prompt)
            
            logging.debug(f"LLM 原始回應: {llm_response}")
            
            # 優先嘗試解析 JSON 格式
            recipe_data = self._parse_llm_response(llm_response)
            
            if recipe_data:
                # JSON 解析成功，使用結構化格式
                logging.info("使用 JSON 格式化食譜")
                messages = self._format_for_discord(recipe_data)
            else:
                # JSON 解析失敗，但不使用預設模板，而是直接使用 LLM 的文字回應
                logging.info("JSON 解析失敗，使用 LLM 原始文字回應")
                
                # 清理 LLM 回應，移除 JSON 部分，只保留文字部分
                cleaned_text = self._extract_text_from_llm_response(llm_response)
                
                if cleaned_text:
                    # 將長文字適當分割
                    messages = self._split_long_message(cleaned_text)
                else:
                    # 最後的 fallback：簡單的文字回應
                    messages = [f"根據你的食材（{', '.join(ingredients)}），我推薦製作簡單的家常料理。請將這些食材依個人喜好調味烹煮即可。"]
            
            return messages
            
        except Exception as e:
            logging.error(f"食譜生成過程發生錯誤: {e}")
            # 發生任何錯誤時，返回簡單的建議而非預設模板
            error_message = f"抱歉，系統暫時無法生成詳細食譜。建議你可以用{', '.join(ingredients)}製作簡單的家常料理。"
            return [error_message]

    def _build_complete_prompt(self, ingredients, servings, time_limit, excluded_recipes):
        """動態構建包含所有條件的完整 system prompt"""
        prompt = self.base_system_prompt + "\n\n"
        
        # 添加具體條件
        prompt += "請根據以下條件設計食譜：\n"
        prompt += f"- 主要食材：{', '.join(ingredients)}\n"
        prompt += f"- 份數：{servings.get('count', 1)}人份\n"
        
        # 時間條件
        if 'value' in time_limit:
            prompt += f"- 時間限制：{time_limit['value']}{time_limit.get('unit', '分鐘')}\n"
        elif 'description' in time_limit:
            prompt += f"- 時間需求：{time_limit['description']}\n"
        
        # 排除的食譜
        if excluded_recipes:
            prompt += f"- 請勿推薦：{', '.join(excluded_recipes)}\n"
        
        # JSON 格式要求
        prompt += "\n請嚴格按照以下JSON格式回應：\n"
        prompt += json.dumps(self.json_format_example, ensure_ascii=False, indent=2)
        
        return prompt

    def _parse_llm_response(self, llm_response):
        """解析 LLM 的 JSON 回應"""
        try:
            # 清理回應字串，移除可能的 markdown 標記
            cleaned_response = llm_response.strip()
            
            # 處理 markdown 格式的 JSON
            if "```json" in cleaned_response:
                # 提取 ```json 和 ``` 之間的內容
                json_start = cleaned_response.find("```json") + 7
                json_end = cleaned_response.find("```", json_start)
                if json_end != -1:
                    cleaned_response = cleaned_response[json_start:json_end].strip()
                else:
                    # 如果沒有結束標記，從 ```json 後取到字符串結尾
                    cleaned_response = cleaned_response[json_start:].strip()
            elif cleaned_response.startswith("```") and cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[3:-3].strip()
            
            # 如果還有多餘內容，只取JSON部分
            # 尋找第一個 { 和最後一個 } 來提取JSON
            first_brace = cleaned_response.find('{')
            last_brace = cleaned_response.rfind('}')
            
            if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
                json_content = cleaned_response[first_brace:last_brace+1]
                
                # 解析 JSON
                recipe_data = json.loads(json_content)
                
                # 驗證和補齊缺失欄位
                recipe_data = self._validate_and_complete_recipe(recipe_data)
                
                return recipe_data
            else:
                logging.warning("無法找到有效的JSON結構")
                return None
                
        except json.JSONDecodeError as e:
            logging.warning(f"JSON 解析失敗: {e}")
            return None
        except Exception as e:
            logging.warning(f"回應解析發生錯誤: {e}")
            return None

    def _validate_and_complete_recipe(self, recipe_data):
        """驗證和補齊食譜資料的缺失欄位"""
        # 必要欄位的預設值
        defaults = {
            "recipe_name": "美味料理",
            "cooking_time": "30分鐘",
            "difficulty": "簡單",
            "ingredients": [],
            "steps": []
        }
        
        # 補齊缺失欄位
        for key, default_value in defaults.items():
            if key not in recipe_data or not recipe_data[key]:
                recipe_data[key] = default_value
        
        # 確保 ingredients 格式正確
        if recipe_data["ingredients"]:
            formatted_ingredients = []
            for ing in recipe_data["ingredients"]:
                if isinstance(ing, dict) and "name" in ing and "amount" in ing:
                    formatted_ingredients.append(ing)
                elif isinstance(ing, str):
                    # 如果是字串，嘗試轉換為字典格式
                    formatted_ingredients.append({"name": ing, "amount": "適量"})
            recipe_data["ingredients"] = formatted_ingredients
        
        # 確保 steps 格式正確
        if recipe_data["steps"]:
            formatted_steps = []
            for i, step in enumerate(recipe_data["steps"]):
                if isinstance(step, dict) and "step" in step and "description" in step:
                    formatted_steps.append(step)
                elif isinstance(step, str):
                    formatted_steps.append({"step": i + 1, "description": step})
            recipe_data["steps"] = formatted_steps
        
        return recipe_data

    def _get_default_recipe(self, ingredients):
        """生成基於食材的預設食譜"""
        default = self.default_recipe_template.copy()
        
        # 將用戶食材添加到預設食譜中
        default["ingredients"] = [{"name": ing, "amount": "適量"} for ing in ingredients]
        
        return default

    def extract_recipe_name(self, recipe_data):
        """提取食譜名稱，用於避免重複推薦"""
        return recipe_data.get("recipe_name", "未知食譜")

    def _format_for_discord(self, recipe_data):
        """按內容邏輯分割為多條 Discord 訊息（無表情符號版本）"""
        messages = []
        
        # 訊息1：食譜名稱 + 基本資訊 + 食材清單
        msg1 = f"【{recipe_data['recipe_name']}】\n"
        msg1 += f"烹飪時間：{recipe_data['cooking_time']}\n"
        msg1 += f"難度：{recipe_data['difficulty']}\n\n"
        msg1 += "= 食材清單 =\n"
        
        for ingredient in recipe_data['ingredients']:
            if isinstance(ingredient, dict):
                msg1 += f"• {ingredient['name']}：{ingredient['amount']}\n"
            else:
                msg1 += f"• {ingredient}\n"
        
        messages.append(msg1.strip())
        
        # 訊息2：烹飪步驟
        if recipe_data['steps']:
            msg2 = "= 烹飪步驟 =\n"
            for step in recipe_data['steps']:
                if isinstance(step, dict):
                    msg2 += f"{step['step']}. {step['description']}\n"
                else:
                    msg2 += f"• {step}\n"
            
            messages.append(msg2.strip())
        
        return messages

    def _extract_text_from_llm_response(self, llm_response):
        """從 LLM 回應中提取純文字部分，移除 JSON"""
        try:
            # 如果包含 ```json 標記，提取 JSON 後面的文字
            if "```json" in llm_response:
                # 找到第二個 ``` 的位置
                json_start = llm_response.find("```json")
                json_end = llm_response.find("```", json_start + 7)
                
                if json_end != -1:
                    # 提取 JSON 後面的文字
                    text_content = llm_response[json_end + 3:].strip()
                    if text_content:
                        return text_content
            
            # 如果沒有明確的 JSON 分隔，嘗試找到純文字部分
            # 通常 JSON 會在前面，文字在後面
            lines = llm_response.split('\n')
            text_lines = []
            json_ended = False
            
            for line in lines:
                if line.strip() == '```' or '}' in line:
                    json_ended = True
                    continue
                elif json_ended and line.strip():
                    text_lines.append(line)
            
            if text_lines:
                return '\n'.join(text_lines).strip()
            
            # 如果都找不到，返回整個回應（移除明顯的 JSON 標記）
            cleaned = llm_response.replace('```json', '').replace('```', '').strip()
            
            # 如果開頭是 {，嘗試移除 JSON 部分
            if cleaned.startswith('{'):
                brace_count = 0
                json_end_pos = -1
                
                for i, char in enumerate(cleaned):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            json_end_pos = i
                            break
                
                if json_end_pos != -1 and json_end_pos < len(cleaned) - 1:
                    return cleaned[json_end_pos + 1:].strip()
            
            return cleaned
            
        except Exception as e:
            logging.warning(f"提取文字內容時發生錯誤: {e}")
            return None

    def _split_long_message(self, message, max_length=2000):
        """如果訊息過長，按字數分割"""
        if len(message) <= max_length:
            return [message]
        
        # 簡單的字數分割
        messages = []
        while len(message) > max_length:
            # 找到適合的分割點（避免在句子中間分割）
            split_pos = max_length
            for i in range(max_length - 100, max_length):
                if i < len(message) and message[i] in ['\n', '。', '！', '？']:
                    split_pos = i + 1
                    break
            
            messages.append(message[:split_pos].strip())
            message = message[split_pos:].strip()
        
        if message:
            messages.append(message)
        
        return messages


if __name__ == "__main__":
    """測試 RecipeRecommender"""
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    # 模擬測試資料
    test_ingredients = ["番茄", "雞蛋", "蔥"]
    test_servings = {"count": 2}
    test_time_limit = {"value": 20, "unit": "分鐘", "display": "20分鐘"}
    test_excluded = ["番茄炒蛋"]
    
    # 創建推薦器實例
    recommender = RecipeRecommender()
    
    print("=== 測試食譜推薦 ===")
    
    try:
        # 測試 prompt 構建
        prompt = recommender._build_complete_prompt(test_ingredients, test_servings, test_time_limit, test_excluded)
        print("構建的 System Prompt:")
        print(prompt)
        print("\n" + "="*50 + "\n")
        
        # 測試預設食譜
        default_recipe = recommender._get_default_recipe(test_ingredients)
        print("預設食譜:")
        print(json.dumps(default_recipe, ensure_ascii=False, indent=2))
        print("\n" + "="*50 + "\n")
        
        # 測試格式化
        messages = recommender._format_for_discord(default_recipe)
        print("格式化的Discord訊息:")
        for i, msg in enumerate(messages, 1):
            print(f"訊息 {i}:")
            print(msg)
            print("-" * 30)
            
    except Exception as e:
        print(f"測試過程發生錯誤: {e}")