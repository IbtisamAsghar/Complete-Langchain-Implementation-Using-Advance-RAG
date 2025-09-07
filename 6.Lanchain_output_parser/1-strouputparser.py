from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint (
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

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

prompt2 = template2.invoke({'text' : result.content})
result1 =  model.invoke(prompt2)

print(result1.content)
