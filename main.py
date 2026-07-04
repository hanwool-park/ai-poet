from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(model="gpt-4o") # 필요에 따라 모델명 지정

st.title("인공지능시인")

content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner("Wait for it...", show_time=True):
        result = chat_model.invoke(content + "에 대한 시를 써줘")
        st.write(result.content)
