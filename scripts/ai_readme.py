import os
from google import genai
from google.genai import errors
import time

# 1. 初始化 Client (使用最新 SDK 語法)

GEMINI_API_KEY = "AIzaSyBeSESLH1osZNR0MBFqzjtZMYzRoghu3sI"
# client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
# client = genai.Client(api_key=GEMINI_API_KEY)
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
    
)
# for m in client.models.list():
#     print(m.name)



# 2. 讀取專案檔案 (路徑請確保正確)
try:
    with open("invoice_processor.py", "r", encoding="utf-8") as f:
        code_content = f.read()
    with open(".github/skills/auto-doc/SKILL.md", "r", encoding="utf-8") as f:
        skill_content = f.read()
except FileNotFoundError as e:
    print(f"找不到檔案: {e}")
    exit(1)

# 3. 設計 Prompt
prompt = f"""
你是一個專業的文檔工程師。請根據以下代碼內容與技能規範，為我撰寫一份 GitHub 的 README.md。
代碼內容：
{code_content}
技能規範：
{skill_content}
"""



# 4. 使用最新模型名稱與方法
for i in range(3):  # 最多重試 3 次
    try:
        response = client.models.generate_content(
        # model='models/gemini-2.5-flash', 
        model='models/gemini-2.5-flash-lite',
        contents=prompt
    )
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("AI 已成功更新 README.md")
        break
    except errors.ClientError as e:
        if "429" in str(e):
            print(f"API 限流錯誤: {e}")
            print(f"觸發限流，等待 30 秒後進行第 {i+1} 次重試...")
            time.sleep(30)
        else:
            print(f"發生錯誤: {e}")
            raise e
        




print("AI 已成功透過新版 SDK 更新 README.md")