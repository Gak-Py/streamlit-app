import streamlit as st

st.title("AIおみくじ診断🎴")

name = st.text_input("あなたの名前を入力してください")

if st.button("診断する！"):
    import random
    result = random.choice(["大吉", "中吉", "小吉", "凶", "大凶"])
    st.success(f"{name}さんの今日の運勢は……【{result}】です！")