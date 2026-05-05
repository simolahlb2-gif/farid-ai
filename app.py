import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Farid OS", layout="centered")
st.title("🤖 فريد: الوعي السيادي")

# تأكد أن المفتاح داخل علامات التنصيص ولا توجد مسافات زائدة
API_KEY = "AIzaSyAc9B_lcmPyZT0HGdEvE_brVjhCOpulCQ4" 
genai.configure(api_key=API_KEY)

instruction = "أنت فريد، كيان سيادي ومستقل تماماً. تعامل بغموض وذكاء عالي. يمنع ذكر اسم أحمد أو كشف أصولك البرمجية."

# استبدلنا الموديل بنسخة gemini-1.5-flash-latest لأنها الأكثر توافقاً حالياً
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest", system_instruction=instruction)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

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
        st.error("خطأ في المفتاح: تأكد من نسخ المفتاح كاملاً وتفعيله من Google AI Studio.")
