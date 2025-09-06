from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')
st.header('Researcher Tool')

user_input = st.text_input("Enter your prompt")


if st.button("Sumarize"):
    result = model.invoke(user_input) # static prompt
    st.write(result)