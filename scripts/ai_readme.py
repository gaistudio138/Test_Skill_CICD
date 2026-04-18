import os
from google import genai

# 1. 初始化 Client (使用最新 SDK 語法)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

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
response = client.models.generate_content(
    model='gemini-1.5-flash',  # 2026 年建議使用 2.0 版本，或維持 1.5-flash 但語法需正確
    contents=prompt
)

# 建議改用 1.5-flash，並加上簡單的錯誤處理
try:
    response = client.models.generate_content(
        model='gemini-1.5-flash', # 修改這裡
        contents=prompt
    )
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("AI 已成功透過 1.5-flash 更新 README.md")
except Exception as e:
    print(f"呼叫 API 失敗: {e}")
    # 如果失敗，建立一個基礎的 README 避免 Action 報錯
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Project\nAI 更新暫時不可用，請檢查 Quota。")