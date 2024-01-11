from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)
import streamlit as st
from streamlit_chat import message

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import os
os.getenv('OPEN_API_KEY')

st.set_page_config(
    page_title='Your Custom Assistant',
    page_icon='🤖',  # Custom favicon, you can use a URL or an emoji
    layout='wide',   # Choose 'wide' or 'centered' layout
    initial_sidebar_state='expanded'  # Choose 'auto', 'expanded', or 'collapsed'
)




chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.5, openai_api_key= os.getenv('OPEN_API_KEY'))
user_prompt = st.chat_input('Ask a question...')
if 'messages' not in st.session_state:
  st.session_state.messages = []

with st.sidebar:
  st.image('chatbot.png', width=300)
  st.header(' FunnyBot Makes You Laught While Answering Your Questions')
  api_key = st.text_input('OpenAI API Key:', type='password')
  if api_key:
    os.environ['OPENAI_API_KEY']= api_key

  # system_message = st.text_input(label = 'System Role 🤖')
 

  # if system_message:
  #   if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
  #      st.session_state.messages.append(SystemMessage(content=system_message))

  if user_prompt:
    st.session_state.messages.append(HumanMessage(content=user_prompt))

    with st.spinner('working on your request...'):
     response = chat(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

if len(st.session_state.messages) >=1:
  if not isinstance(st.session_state.messages[0], SystemMessage):
    st.session_state.messages.insert(0, SystemMessage(content='You are a funny assistant that like to make you laugh. You try to make a joke in every response'))



for i,msg in enumerate(st.session_state.messages[1:]):
  if i%2 ==0:
    message(msg.content, is_user=True, key=f'{i}+ 😂')
  else:
    message(msg.content, is_user=False, key=f'{i} + 🤖')