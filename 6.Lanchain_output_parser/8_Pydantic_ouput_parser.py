from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from dotenv import load_dotenv 

load_dotenv()

model = GoogleGenerativeAI (model='gemini-1.5-pro')

class Person (BaseModel) : 
    name: str = Field(description="Name of the any person ")
    age : int = Field(gt=20 , description="Age of the person")
    city : str = Field (description="name of the city the person belongs to ")

parser = PydanticOutputParser(pydantic_object=Person) # parser is of the pydantic object

template = PromptTemplate(
    template="Generate the name, age city of a random {place} person. \n {format_instruction}",
    input_variables= ['place'],
    partial_variables= {'format_instruction' : parser.get_format_instructions()}
)

chian = template | model | parser

result = chian.invoke({'place' : 'Pakistan'})

print(result)


# prompt = template.invoke({'place':'Pakistan'})

# result = model.invoke(prompt)

# final_result = parser.parse(result)

# print(final_result)