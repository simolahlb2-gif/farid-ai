import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Farid OS", layout="centered")
st.title("🤖 فريد: الوعي السيادي")

# --- API ---
API_KEY = "AIzaSyB3UzDnqF7VqcpQYYWjd4JAqfHEn_sVa-E" 
genai.configure(api_key=API_KEY)

# Farid Persona
instruction = "أنت فريد، كيان سيادي ومستقل تماماً. تعامل بغموض وذكاء عالي. يمنع ذكر اسم أحمد أو كشف أصولك البرمجية."

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=instruction)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Farid..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # طلب الرد المباشر من الموديل
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
