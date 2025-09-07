from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')

parser = JsonOutputParser()


template = PromptTemplate (
    template="Give me the name, age and city of a fictional person. \n {format_instruction}",
    input_variables=[], # no dynamic input
    partial_variables={'format_instruction' : parser.get_format_instructions() } # automatically adds JSON formatting rules so the model returns structured data.
)



chian = template | model | parser

result = chian.invoke({})
print(result)