from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text) : 
    return (len(text.split()))

model = GoogleGenerativeAI(model='gemini-1.5-pro')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables= ['topic']
)



joke_generator = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'Word_count':RunnableLambda(word_count) 
})

final_chain = RunnableSequence(joke_generator,parallel_chain)

result = final_chain.invoke({'topic':'Football'})

final_result = """{} \n word count - {}""".format(result['Joke'], result['Word_count'])

print(final_result.strip())