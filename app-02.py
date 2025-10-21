import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("ChatBot-Project")
st.write("ChatBot buatan kholil")

def get_api_key_input():
    st.write("Input Google API Key")

    if "GOOGLE_API_KEY" not in st.session_state:
        st.session_state["GOOGLE_API_KEY"] = ""
    #st.session_state["GOOGLE_API_KEY"] = ""
    #GOOGLE_API_KEY = ""

    col1, col2 = st.columns((80,20))

    with col1:
        API_KEY = st.text_input("Google API Key", label_visibility="collapsed", type="password")
    #st.write(f"Keya Anda adalah {GOOGLE_API_KEY}")
    with col2:
        is_submit_pressed = st.button("Submit")
        if is_submit_pressed:
            st.session_state["GOOGLE_API_KEY"] = API_KEY
            #GOOGLE_API_KEY = API_KEY
            #st.write("Key Anda adalah", GOOGLE_API_KEY)
            
    #return st.session_state["GOOGLE_API_KEY"]
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
        #st.write(prompt)
        st.markdown(message.content)


#GOOGLE_API_KEY = st.session_state["GOOGLE_API_KEY"]
#GOOGLE_API_KEY = get_api_key_input()
get_api_key_input()

if not os.environ["GOOGLE_API_KEY"]:
    st.stop()
llm = load_llm()
chat_history = get_chat_history()

#if GOOGLE_API_KEY != "":
#    st.write("API Key Anda adalah", GOOGLE_API_KEY)

#st.button("Random Button")
for chat in chat_history:
    #with st.chat_message("User"):
        #st.write(prompt)
    #    st.markdown(chat.content)
    display_chat_message(chat)

prompt = st.chat_input("Chat with AI")

if prompt:
    chat_history.append(HumanMessage(content=prompt))
    #with st.chat_message("User"):
        #st.write(prompt)
    #    st.markdown(prompt)
    display_chat_message(chat_history[-1])
    response = llm.invoke(chat_history)
    #with st.chat_message("User"):
        #st.write(prompt)
    #    st.markdown(response.content)
    chat_history.append(response)
    display_chat_message(chat_history[-1]) 
    



