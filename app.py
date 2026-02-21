import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="女朋友翻譯器", page_icon="💖")
st.title("💖 女朋友話術翻譯器")

# 檢查檔案是否存在
if os.path.exists("data.csv"):
    # 讀取本地的 CSV 數據庫
    df = pd.read_csv("data.csv")
    
    user_input = st.text_input("女朋友說了什麼？", placeholder="例如：我沒事...")

    if st.button("開始翻譯"):
        if user_input:
            # 搜尋關鍵字
            match = df[df['keyword'].str.contains(user_input, na=False, case=False)]
            
            if not match.empty:
                st.error(f"🔍 **真正含義：** {match.iloc[0]['real_meaning']}")
                st.success(f"💡 **求生指南：** {match.iloc[0]['action']}")
            else:
                st.warning("⚠️ 數據庫暫時沒有這一題，請去 data.csv 增加內容！")
        else:
            st.info("請先輸入文字喔！")
else:
    st.error("找不到 data.csv 檔案，請確認檔案名稱是否正確。")