import os
import time
from google import genai
from google.genai import errors

# 1. 設定環境變數 (請在 Terminal 先執行 export GEMINI_API_KEY='你的KEY')
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("❌ 錯誤：找不到環境變數 GEMINI_API_KEY")
    exit(1)

client = genai.Client(api_key=api_key, http_options={'api_version': 'v1'})

def local_test():
    # 測試用的簡單內容
    prompt = "這是一個測試指令。請回覆：'AI 代理已就緒'。"
    
    # 測試模型列表 (由輕量到重型)
    test_models = [
        'models/gemini-2.0-flash-lite',
        'models/gemini-1.5-flash',
        'models/gemini-2.0-flash'
    ]
    for m in client.models.list():

    # for model_name in test_models:
        model_name = m.name
        print(f"\n🔍 正在嘗試模型: {model_name}...")
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            print(f"✅ 成功！AI 回應: {response.text}")
            # return # 只要有一個成功就停止
            
        except errors.ClientError as e:
            if "429" in str(e):
                print(f"⚠️ {model_name} 觸發限流 (429)。")
            elif "404" in str(e):
                print(f"❓ {model_name} 找不到 (404)。")
            else:
                print(f"❌ 其他錯誤: {e}")
        
        print("等待 5 秒後嘗試下一個模型...")
        time.sleep(5)

if __name__ == "__main__":
    local_test()