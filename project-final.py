import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from google.api_core.exceptions import GoogleAPIError

st.title("ChatBot-Project")
st.write("ChatBot Buatan Kholil")
   
def get_api_key_input():
    st.write("Input Google API Key")

    if "GOOGLE_API_KEY" not in st.session_state:
        st.session_state["GOOGLE_API_KEY"] = ""

    col1, col2 = st.columns((80,20))

    with col1:
        API_KEY = st.text_input("Google API Key", label_visibility="collapsed", type="password")

    with col2:
        is_submit_pressed = st.button("Submit")
        if is_submit_pressed:
            st.session_state["GOOGLE_API_KEY"] = API_KEY

    os.environ["GOOGLE_API_KEY"] = st.session_state["GOOGLE_API_KEY"]

def load_llm():
    if "llm" not in st.session_state:
        st.session_state["llm"] = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    return st.session_state["llm"]

def get_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    return st.session_state["chat_history"]

def display_chat_message(message):
    if type(message) is HumanMessage:
        role = "User"
    elif type(message) is AIMessage:
        role = "AI"
    else:
        role ="unknown"
    
    with st.chat_message(role):
        st.markdown(message.content)

def user_query_to_llm(chat_history):
    prompt = st.chat_input("Chat with AI")
    if not prompt:
        st.stop()
    chat_history.append(HumanMessage(content=prompt))
    display_chat_message(chat_history[-1])
    response = llm.invoke(chat_history)
    chat_history.append(response)
    display_chat_message(chat_history[-1]) 


get_api_key_input()

if not os.environ["GOOGLE_API_KEY"]:
    st.stop()
llm = load_llm()
chat_history = get_chat_history()


for chat in chat_history:
    display_chat_message(chat)
user_query_to_llm(chat_history)




