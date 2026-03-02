import streamlit as st
import pandas as pd
import os

# 1. 設定網頁標題與分頁圖示
st.set_page_config(page_title="女朋友話術翻譯器", page_icon="💖")
st.title("💖 女朋友話術翻譯器")

# 2. 檢查數據庫檔案是否存在
if os.path.exists("data.csv"):
    # 讀取本地 CSV 數據庫
    df = pd.read_csv("data.csv")
    
    # 使用者輸入框
    user_input = st.text_input("女朋友說了什麼？", placeholder="例如：我沒事、隨便...")

    # 3. 點擊翻譯按鈕
    if st.button("開始翻譯"):
        if user_input:
            # 模糊搜尋邏輯：只要關鍵字包含在 user_input 內，或 user_input 包含在關鍵字內
            # na=False 處理空值，case=False 不分大小寫
            mask = df['keyword'].str.contains(user_input, na=False, case=False)
            match = df[mask]

            if not match.empty:
                # 顯示搜尋到的第一筆匹配結果
                st.error(f"💔 **真正含義：** {match.iloc[0]['real_meaning']}")
                st.success(f"💡 **求生指南：** {match.iloc[0]['action']}")
            else:
                st.warning("⚠️ 數據庫暫時沒有這一題，快去更新 data.csv 吧！")
        else:
            st.info("💡 請先輸入文字喔！")
else:
    st.error("❌ 找不到 data.csv 檔案，請確認檔案名稱是否正確。")

# 註：已依照需求移除「查看完整數據庫」勾選框