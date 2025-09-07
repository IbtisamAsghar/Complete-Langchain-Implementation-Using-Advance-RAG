from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')

prompt = PromptTemplate(
    template = 'Genreate five interesting topic about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Football'})

print(result)

chain.get_graph().print_ascii()