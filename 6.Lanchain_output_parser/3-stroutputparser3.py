from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')



# 1st prompt -> detailed report
template1 = PromptTemplate (
    template="write a detailed report on {topic}",
    input_variables=['topic']
)
# 2nd prompt 

template2 = PromptTemplate (
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)


parser = StrOutputParser() # convert the ouput of the model to plain string 

# pipeline
# parser → Extracts the plain text output from the AI model.
# This pipeline first generates a detailed report, extracts the text, summarizes it in five lines, and extracts the final summary.
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Black hole'})


print(result)
