from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed report on the topic \n {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)
text_generator = prompt1 | model | parser

parallel_chain = RunnableBranch(
    (lambda x:len(x.split())>250 , prompt2 | model | parser ),
    RunnablePassthrough()
    
)

final_chain = text_generator | parallel_chain

result = final_chain.invoke({'topic':'Netflix'})

print(result)