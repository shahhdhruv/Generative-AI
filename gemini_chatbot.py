import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("G_KEY")

# Configure genai with the API key
genai.configure(api_key=api_key)

# Create the GenerativeModel (llm)
model = genai.GenerativeModel('gemini-pro')

# Streamlit interface
st.title("Chatbot with Gemini-Pro")
user_input = st.text_input("You:", "")

if st.button("Send"):
    response = model.generate_content(user_input)
    st.text_area("Bot:", response.text)
