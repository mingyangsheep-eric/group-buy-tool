import streamlit as st
import datetime

# --- 網頁設定 ---
st.set_page_config(page_title="團購文案生成助手", page_icon="🛍️")

# --- 標題區 ---
st.title("🛍️ 團購文案生成助手")
st.markdown("只要填寫下方資訊，就能一鍵生成精美的 LINE/FB 揪團文案！")

# --- 輸入區 ---
col1, col2 = st.columns(2)
with col1:
    product_name = st.text_input("商品名稱", placeholder="例如：Dyson 吹風機")
    original_price = st.number_input("原價 (元)", min_value=0)
with col2:
    group_price = st.number_input("團購價 (元)", min_value=0)

product_desc = st.text_area("商品特色", placeholder="為什麼要買這個？")
product_link = st.text_input("下單連結", placeholder="https://...")

# --- 按鈕與邏輯 ---
if st.button("✨ 生成揪團文案", type="primary"):
    if not product_name:
        st.error("請輸入商品名稱！")
    else:
        # 這裡就是把資料組裝起來的地方
        result = f"🔥 【限時團購】{product_name} 開團啦！\n"
        if original_price > 0:
            result += f"💰 原價：${original_price}\n"
        result += f"🏷️ 團購價：${group_price}\n"
        result += f"\n✨ 商品特色：\n{product_desc}\n"
        result += f"\n👉 下單傳送門：{product_link}"
        
        st.success("生成成功！請複製下方文字：")
        st.code(result)
