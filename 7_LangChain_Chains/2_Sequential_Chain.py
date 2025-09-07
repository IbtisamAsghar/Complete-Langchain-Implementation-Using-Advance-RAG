from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI (model='gemini-1.5-pro')
parser = StrOutputParser()

prompt_1 = PromptTemplate(
    template="Generate a detailed report on the {topic}",
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {text}",
    input_variables=['text'] 
)

chain = prompt_1 | model | parser | prompt_2 | model | parser

result = chain.invoke({'topic':'Nepotism in Pakistan'})

print(result)

chain.get_graph().print_ascii()