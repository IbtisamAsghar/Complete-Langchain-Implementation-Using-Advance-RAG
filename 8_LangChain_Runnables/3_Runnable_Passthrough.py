from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel
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

joke_generator = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'Explanation':RunnableSequence(prompt2,model,parser)
})
final_chian = RunnableSequence(joke_generator,parallel_chain)

result = final_chian.invoke({'topic':'Football'})
print(result['Joke'])
print("=================================")
print(result['Explanation'])