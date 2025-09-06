# chat prompt template is used to multi turn conservation
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert '),
    ('human' , 'Explain in simple terms, what is the {topic}')
])

prompt = chat_template.invoke({'domain':'cricket' ,'topic':'Dusra'})
print(prompt)