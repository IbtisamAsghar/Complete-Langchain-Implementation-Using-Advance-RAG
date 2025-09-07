from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Write a tweet for a {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Write a post for linked on a {topic}",
    input_variables=['topic']
)

chain_paraller = RunnableParallel ({
    'tweet':RunnableSequence(prompt1 , model , parser) , 
    'linkedin':RunnableSequence(prompt2,model,parser)

})

result = chain_paraller.invoke({'topic':'Football'})
print(result['tweet'])
print("====================================")
print(result['linkedin'])