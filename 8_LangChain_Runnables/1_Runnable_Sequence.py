from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()


model = GoogleGenerativeAI(model='gemini-1.5-pro')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate (
    template= "Explain the joke {text}",
    input_variables=['text']
)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic' : 'Football'}))