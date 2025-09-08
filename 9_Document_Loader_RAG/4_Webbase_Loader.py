from langchain_community.document_loaders import WebBaseLoader 
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')
parser = StrOutputParser()



prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text -\n {text}",
    input_variables = ['question','text']
)

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser


print(chain.invoke({"question":"What is the price of the product?" , 'text':docs[0].page_content}))