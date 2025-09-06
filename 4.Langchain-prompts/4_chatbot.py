from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')

# mantaing the history of the chat to create a context
chat_history = [
    SystemMessage(content="You are a Helpful AI assistant")
]

while True : 
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit" :
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI: ",result)

print(chat_history)