from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model = 'gemini-1.5-pro')
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Give me all references link mention in pdf-\n {text}",
    input_variables=['text']
)

loader = PyPDFLoader('Agentic And GenAI AWS GCP.pdf')
docs = loader.load()

print(len(docs))

chain = prompt | model | parser
print(chain.invoke({'text':docs}))