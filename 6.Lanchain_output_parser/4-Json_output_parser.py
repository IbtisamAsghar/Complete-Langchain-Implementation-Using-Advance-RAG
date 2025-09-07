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

prompt = template.format() # This replaces {format_instruction} with actual JSON formatting instructions.
#t(prompt)
result = model.invoke(prompt)

final_result = parser.parse(result) 
print(final_result)
print(type(final_result))
print(final_result['name'])