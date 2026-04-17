# Skill: Auto-Documentation Assistant

## Description
當使用者推送 (Push) 程式碼變動，且變動涉及核心邏輯 (如 .py, .gs 檔案) 時，此技能會自動啟動，負責分析代碼並更新 README.md。

## Instructions
1. 掃描最近一次 Commit 的代碼變更。
2. 使用 Gemini API 總結變更點。
3. 將總結內容以「更新日誌」格式插入到 README.md 的 ## Changelog 區段。
4. 確保不更動原有的文件結構。
5. 提交更新後的 README.md。
6.在執行測試時，如果發現金額大於 10000，必須在 Log 中額外標註【高額警報】。

## Constraints
- 語氣必須專業且簡潔。
- 若變更僅涉及排版 (Linting)，則忽略此任務。