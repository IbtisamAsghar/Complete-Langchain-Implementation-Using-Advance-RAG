from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load OpenAi Api key

llm = OpenAI(model= 'gpt-3.5-turbo-instruct') # make an object of OpenAI
result = llm.invoke('What is the capital of spain') # calling invoke function with the help of object

print(result)