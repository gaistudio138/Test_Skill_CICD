import os
import google.generativeai as genai

# 1. 設定 Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 讀取專案檔案作為上下文
with open("invoice_processor.py", "r", encoding="utf-8") as f:
    code_content = f.read()

with open(".github/skills/invoice-helper/SKILL.md", "r", encoding="utf-8") as f:
    skill_content = f.read()

# 3. 設計給 AI 的 Prompt
prompt = f"""
你是一個專業的文檔工程師。請根據以下代碼內容與技能規範，為我撰寫一份 GitHub 的 README.md。
要求：
1. 包含專案簡介與核心功能。
2. 根據 SKILL.md 說明如何使用此技能。
3. 格式要美觀，使用 Markdown 語法。

代碼內容：
{code_content}

技能規範：
{skill_content}
"""

# 4. 呼叫 AI 並寫入檔案
response = model.generate_content(prompt)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(response.text)

print("AI 已成功更新 README.md")