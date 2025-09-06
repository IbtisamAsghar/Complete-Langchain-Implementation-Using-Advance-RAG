from langchain_core.messages import HumanMessage , SystemMessage , AIMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content= "Tell me about the langchain")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result))
print(result)