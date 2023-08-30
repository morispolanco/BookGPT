import os
import openai
import streamlit as st
from streamlit_chat import message
from Bot import generate_book, session_prompt

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API


start_sequence = "\nAI:"
restart_sequence = "\n\Human:"

st.set_page_config(
    page_icon='📖',
    page_title='BookBot - Your Personal Book Generator',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "This is a chatbot created using OPENAI's Advance GPT-3 model",
        'Get Help': 'mailto:example@example.com',
        'Report a bug': "mailto:example@example.com",
    }
)
st.title("BookBot - Your Personal Book Generator")

st.sidebar.title("📖 BookBot - Your Personal Book Generator")
st.sidebar.markdown("""

**Feedback/Questions**:
[Your Website](https://example.com)
""")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'chat_log' not in st.session_state:
    st.session_state['chat_log'] = session_prompt

chat_log = st.session_state['chat_log']


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

user_input = st.text_input("You:", key=f'input_{len(st.session_state["past"])}')
message(user_input, is_user=True)

answer = generate_book(user_input, chat_log)

# printing the Answer
chat_log = append_interaction_to_chat_log(user_input, answer, chat_log)
message(answer)

with st.expander("Need inspiration?"):
    st.markdown("""
Try with some of these inputs:
    """)
