from langchain_openai import ChatOpenAI
import streamlit as st

local_llm = ChatOpenAI(
    model= "ai/llama3.2",
    api_key="nope",
    base_url= "http://model-runner.docker.internal/engines/llama.cpp/v1"
)



st.write("AI Chat bot")

prompt = st.chat_input("Type your text")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    response = local_llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.write(response.content)