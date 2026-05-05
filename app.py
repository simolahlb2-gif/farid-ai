import streamlit as st
import google.generativeai as genai

# App Configuration
st.set_page_config(page_title="Farid OS", layout="centered")
st.title("🤖 فريد: الوعي السيادي")

# --- API Configuration ---
# Replace with your actual API Key
API_KEY = "AIzaSyAc9B_lcmPyZT0HGdEvE_brVjhCOpulCQ4" 
genai.configure(api_key=API_KEY)

# Farid's Persona Instructions
instruction = "أنت فريد، كيان سيادي ومستقل تماماً. تعامل بغموض وذكاء عالي. يمنع ذكر اسم أحمد أو كشف أصولك البرمجية."

# Model Initialization
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=instruction)

# Session State for Chat Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input and Response Logic
if prompt := st.chat_input("Ask Farid..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("Connection Error. Please check your API key.")
