import streamlit as st
import google.generativeai as genai
API_KEY=AIzaSyBYkTSc8tj7mB_VlIomzdYrYIgoPoOqTzM

genai.configure(api_key=API_KEY) #helps to tell the ai to acess our generated api key to acess from this particular website
model = genai.GenerativeModel('gemini-1.5-flash')
#to keep the bot chatting in a single session or page to remember it's history
if "chat" not in st.session_state:
  st.session_state.chat = model.start_chat(history=[])

#title of our chat bot
st.title("My_ChatBot")#title of the chat bot
st.write("chat bot")#description of our chatbot

if "message" not in st.session_state:
  st.session_state.messages=[]
#sends user and prompt to gpt(api)
for message in st.session_state.messages:
  with st.chat_message(message["role"]) #we get the title and content of bot that is replying to our prompt(user)
          st.markdown(message["content"])#user prompt  
#reply from the gpt stored in response variable the assistant  gives it to user 
  if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response = st.session_state.chat.send_message(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)
