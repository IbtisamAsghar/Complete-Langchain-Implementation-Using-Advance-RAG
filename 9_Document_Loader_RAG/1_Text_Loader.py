from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model = 'gemini-1.5-pro')
parser = StrOutputParser()

prompt = PromptTemplate(
    template="How many soldiers dies in world war ?-\n {text}",
    input_variables=['text']
)

loader = TextLoader('Hitler.txt',encoding='utf-8')
docs = loader.load() # load the list of docoument object

print(type(docs)) # list of Document objects and contains the page_content and metadata
print(docs[0].page_content) # Print the content of the first document
print(docs[0].metadata) # # Print metadata associated with the first document (like file path)

chain = prompt | model | parser

print(chain.invoke({'text':docs[0].page_content}))