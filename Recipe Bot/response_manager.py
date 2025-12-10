#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Response Manager
    專門處理 intent 的回覆邏輯
"""

def format_ingredients_chinese(ingredients):
    """繁體中文友善的食材連接"""
    if len(ingredients) == 1:
        return ingredients[0]
    elif len(ingredients) == 2:
        return f"{ingredients[0]}和{ingredients[1]}"
    else:
        return "、".join(ingredients[:-1]) + f"和{ingredients[-1]}"

def generate_ingredient_response(resultDICT):
    """生成食材相關的回覆"""
    intent = resultDICT.get("intent", "unknown")
    
    if intent == "ingredient_input":
        ingredients = resultDICT.get("ingredients", [])
        if ingredients:
            ingredients_str = format_ingredients_chinese(ingredients)
            return f"好的，現在我們有{ingredients_str}，請問要做幾人份的料理呢？"
    
    # 預設回覆（unknown 或其他情況）
    return "不好意思，我不太理解你的意思，可以換句話說嗎？"

def generate_serving_response(resultDICT):
    """生成份數相關的回覆"""
    intent = resultDICT.get("intent", "unknown")
    
    if intent == "serving_input":
        # 情況1: 成功提取數字
        servings = resultDICT.get("servings", {})
        print(servings)
        count = servings.get("count")
        print(count)
        if count:
            return f"{count}人份，沒問題！預計多久上菜呢？"
    elif intent == "serving_clarification":
        # 情況2: 需要詢問具體人數
        return "請問具體要做幾人份呢？"
    elif intent == "unknown":
        # 情況3: 無關輸入
        return "不好意思，我不太理解你的意思，可以換句話說嗎？"
    
    # 預設回覆
    return "請問要做幾人份的料理呢？"
def generate_serving_response(resultDICT):
    """生成份數相關的回覆"""
    intent = resultDICT.get("intent", "unknown")
    
    if intent == "serving_input":
        # 情況1: 成功提取數字
        servings = resultDICT.get("servings", {})
        print(servings)  # <-- 這裡
        count = servings.get("count")
        print(count)     # <-- 這裡
        if count:
            return f"{count}人份，沒問題！預計多久上菜呢？"

def generate_time_limit_response(resultDICT):
    """生成時間限制相關的回覆"""
    intent = resultDICT.get("intent", "unknown")
    
    if intent == "time_input":
        time_limit = resultDICT.get("time_limit", {})
        
        # 明確時間
        if "value" in time_limit:
            display = time_limit.get("display", "指定時間")
            return f"{display}內上菜，收到！開始推薦料理..."
        
        # 模糊時間  
        elif "description" in time_limit:
            description = time_limit.get("description", "")
            return f"了解，要{description}！讓我推薦適合的食譜..."
    
    elif intent == "time_clarification":
        return "請問您希望多久時間內完成料理呢？"
    
    elif intent == "unknown":
        return "請調整一下您的時間需求，比如說「30分鐘」或「快速料理」。"
    
    # 預設回覆
    return "請問預計多久上菜呢？"

def add_response_to_result(resultDICT):
    """為 resultDICT 加上 response 欄位"""
    if "response" not in resultDICT:
        intent = resultDICT.get("intent", "unknown")
        
        if intent in ["ingredient_input"]:
            resultDICT["response"] = generate_ingredient_response(resultDICT)
        elif intent in ["serving_input", "serving_clarification"]:
            resultDICT["response"] = generate_serving_response(resultDICT)
        elif intent in ["time_input", "time_clarification"]:
            resultDICT["response"] = generate_time_limit_response(resultDICT)
        else:
            # unknown 或其他情況的預設回覆
            resultDICT["response"] = "不好意思，我不太理解你的意思，可以重複一遍嗎？"
    
    return resultDICT

if __name__ == "__main__":
    """測試 response_manager"""
    from pprint import pprint

    
    test_cases = [
        # ingredient 測試
        {
            "name": "ingredient_input - 成功",
            "input": {
                "intent": "ingredient_input",
                "ingredients": ["番茄", "雞蛋", "蔥"]
            },
            "expected": "好的，現在我們有番茄、雞蛋和蔥，請問要做幾人份的料理呢？"
        },
        {
            "name": "ingredient_input - 單一食材",
            "input": {
                "intent": "ingredient_input", 
                "ingredients": ["番茄"]
            },
            "expected": "好的，現在我們有番茄，請問要做幾人份的料理呢？"
        },
        
        # serving 測試
        {
            "name": "serving_input - 成功",
            "input": {
                "intent": "serving_input",
                "servings": {"count": 3}
            },
            "expected": "3人份，沒問題！預計多久上菜呢？"
        },
        {
            "name": "serving_clarification",
            "input": {
                "intent": "serving_clarification"
            },
            "expected": "請問具體要做幾人份呢？"
        },
        
        # time_limit 測試
        {
            "name": "time_input - 明確時間",
            "input": {
                "intent": "time_input",
                "time_limit": {
                    "value": 30,
                    "unit": "分鐘",
                    "display": "30分鐘",
                    "original": "30分鐘"
                }
            },
            "expected": "30分鐘內上菜，收到！開始推薦料理..."
        },
        {
            "name": "time_input - 模糊時間",
            "input": {
                "intent": "time_input",
                "time_limit": {
                    "type": "vague",
                    "description": "快速料理"
                }
            },
            "expected": "了解，要快速料理！讓我推薦適合的食譜..."
        },
        {
            "name": "time_clarification",
            "input": {
                "intent": "time_clarification"
            },
            "expected": "請問您希望多久時間內完成料理呢？"
        },
        {
            "name": "time_unknown",
            "input": {
                "intent": "unknown"
            },
            "expected": "不好意思，我不太理解你的意思，可以重複一遍嗎？"
        },
        
        # 邊界情況
        {
            "name": "空的 ingredients",
            "input": {
                "intent": "ingredient_input",
                "ingredients": []
            },
            "expected": "不好意思，我不太理解你的意思，可以換句話說嗎？"
        },
        {
            "name": "缺少 servings count",
            "input": {
                "intent": "serving_input",
                "servings": {}
            },
            "expected": "請問要做幾人份的料理呢？"
        },
        {
            "name": "time_limit 缺少 display",
            "input": {
                "intent": "time_input",
                "time_limit": {
                    "value": 45,
                    "unit": "分鐘"
                }
            },
            "expected": "指定時間內上菜，收到！開始推薦料理..."
        }
    ]
    
    print("=== Response Manager 測試 ===")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n測試 {i}: {test_case['name']}")
        print(f"輸入: {test_case['input']}")
        
        # 執行測試
        result = add_response_to_result(test_case['input'].copy())
        actual_response = result.get("response", "")
        expected_response = test_case['expected']
        
        # 檢查結果
        if actual_response == expected_response:
            print("通過")
        else:
            print("失敗")
            print(f"  預期: {expected_response}")
            print(f"  實際: {actual_response}")
        
        print(f"完整結果: {result}")
    
    # 綜合測試：測試從空 resultDICT 開始
    print("\n=== 綜合流程測試 ===")
    
    flow_tests = [
        {
            "name": "ingredient → serving → time 完整流程",
            "steps": [
                {"intent": "ingredient_input", "ingredients": ["番茄", "雞蛋"]},
                {"intent": "serving_input", "servings": {"count": 2}},
                {"intent": "time_input", "time_limit": {"value": 20, "unit": "分鐘", "display": "20分鐘"}}
            ]
        }
    ]
    
    for flow_test in flow_tests:
        print(f"\n{flow_test['name']}:")
        for step_num, step in enumerate(flow_test['steps'], 1):
            result = add_response_to_result(step.copy())
            print(f"  步驟 {step_num}: {result.get('response', 'No response')}")