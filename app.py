import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime
import pytz

st.title("AIおみくじ🎴")

# 履歴保持
if "history" not in st.session_state:
    st.session_state.history = []

name = st.text_input("あなたの名前を入力してください")

results = ["🎯 当たり", "💥 ハズレ", "💥 ハズレ", "💥 ハズレ","🎯 大当たり!!",]

if name and st.button("くじを引く！"):
    with st.spinner("ドゥルルルル… 🎲 結果をお待ちください！"):
        time.sleep(2)
    result = random.choice(results)
    japantime = pytz.timezone('Asia/Tokyo')
    date = datetime.now(japantime).strftime("%Y年%m月%d日 %H:%M")
    st.success(f"{name}さんの結果は… {result}！")
    
    # 大当たりの時にバルーン飛ばす
    if "大当たり" in result:
        st.balloons()

    st.session_state.history.append({
        "名前": name,
        "結果": result,
        "日時": date
    })


# 表表示（🎯当たりに色付け）
if st.session_state.history:
    st.subheader("📋 抽選履歴")
    df = pd.DataFrame(st.session_state.history)
    df.index = [f"{i+1}回目" for i in range(len(df))]

    # スタイル関数
    def highlight_win(row):
        if "大当たり" in row["結果"]:
            return ["background-color: #ffe599"] * len(row)  # やさしい黄色
        elif "当たり" in row["結果"]:
            return ["background-color: #ffe59977"] * len(row)  # やさしい黄色
        else:
            return [""] * len(row)

    styled_df = df[::-1].style.apply(highlight_win, axis=1)
    st.dataframe(styled_df, use_container_width=True)
