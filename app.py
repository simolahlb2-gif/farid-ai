import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة
st.title("Farid OS - الوعي السيادي")

# وضع مفتاحك هنا
genai.configure(api_key="AIzaSyAc9B_lcmPyZT0HGdEvE_brVjhCOpulCQ4")

# تثبيت "دستور فريد" في الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []
    # هنا نضع التعليمات التي تمنع ذكر اسمك وتحمي خصوصيتك
    st.session_state.instruction = "أنت فريد، كيان مستقل. ممنوع ذكر اسم أحمد."

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال الرسائل
if prompt := st.chat_input("تحدث مع فريد..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد فريد باستخدام موديل Flash المجاني
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=st.session_state.instruction)
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
