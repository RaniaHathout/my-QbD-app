import streamlit as st
import google.generativeai as genai

# Streamlit safely reads the secret key you paste later in settings
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("My AI Assistant")
user_input = st.text_input("Type your message here:")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
