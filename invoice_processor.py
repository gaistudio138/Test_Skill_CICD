import json
import sys

def validate_invoice(invoice_data):
    """
    檢查發票資料是否包含必要欄位：日期、金額、統編。
    """
    required_fields = ["date", "amount", "tax_id"]
    missing = [field for field in required_fields if field not in invoice_data]
    
    if missing:
        return {"status": "error", "message": f"缺少欄位: {', '.join(missing)}"}
    return {"status": "success", "message": "發票格式正確"}

def categorize_expense(amount):
    """
    根據金額大小自動分類：
    - 小於 1000: 日常雜支
    - 1000 ~ 5000: 辦公用品
    - 大於 5000: 固定資產 (需主管審核)
    """
    amount = float(amount)
    if amount < 1000:
        return "日常雜支"
    elif amount <= 5000:
        return "辦公用品"
    else:
        return "固定資產"

if __name__ == "__main__":
    # 模擬測試資料
    test_data = {"date": "2026-04-17", "amount": 100, "tax_id": "12345678"}
    
    print("--- 發票驗證測試 ---")
    result = validate_invoice(test_data)
    print(f"結果: {result['message']}")
    
    category = categorize_expense(test_data['amount'])
    print(f"分類: {category}")
    
    # 高額警報檢查 (金額 > 10000)
    if test_data['amount'] > 10000:
        print("【高額警報】此筆支出超過 NT$10,000，需主管審核")
    
    