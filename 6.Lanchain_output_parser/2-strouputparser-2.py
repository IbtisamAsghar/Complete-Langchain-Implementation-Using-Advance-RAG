# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFaceEndpoint (
#     repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation"
# )

model = GoogleGenerativeAI(model='gemini-1.5-pro')

# model = ChatHuggingFace(llm = llm)

# 1st prompt -> detailed report
template1 = PromptTemplate (
    template="write a detailed report on {topic}",
    input_variables=['topic']
)
# 2nd prompt 

template2 = PromptTemplate (
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'Black Hole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text' : result})
result1 =  model.invoke(prompt2)

print(result1)
