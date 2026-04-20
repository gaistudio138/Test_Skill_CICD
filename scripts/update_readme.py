# 檔案路徑: scripts/update_readme.py
import datetime

content = f"""# 發票處理專案 (自動更新)

## 專案狀態
最後更新時間: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 技能規範 (來自 SKILL.md)
此文件由 Agent Skill 自動維護。每當程式碼更新，本文件將同步更新驗證邏輯說明。

## 核心邏輯
目前系統支援：金額分類、統編驗證。
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README.md 已成功產生！")