import streamlit as st
import time
import random

st.title("AIおみくじ🎴")

# セッションステートで履歴を保持
if "history" not in st.session_state:
    st.session_state.history = []

name = st.text_input("あなたの名前を入力してください")

# くじの結果一覧（当たり1、ハズレ3）
results = ["🎯 当たり", "💥 ハズレ", "💥 ハズレ", "💥 ハズレ"]

if st.button("くじを引く！"):
    if name.strip() == "":
        st.warning("名前を入力してください！")
    else:
        with st.spinner("ドゥルルルル… 🎲 結果をお待ちください！"):
            time.sleep(2)  # 演出のための2秒待機
        result = random.choice(results)
        st.success(f"{name}さんの結果は… {result}！")
        st.session_state.history.append({"name": name, "result": result})

# 抽選履歴の表示
if st.session_state.history:
    st.subheader("📜 過去の結果")
    history = st.session_state.history
    total = len(history)
    for i, entry in enumerate(reversed(history)):
        count = i + 1
        st.write(f"{total - count + 1}回目：{entry['name']} さん → {entry['result']}")