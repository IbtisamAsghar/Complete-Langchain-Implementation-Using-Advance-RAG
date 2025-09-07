from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')

schema = [
    ResponseSchema(name="fact_1",description='fact 1 about the topic'),
    ResponseSchema(name="fact_2",description='fact 2 about the topic'),
    ResponseSchema(name="fact_3",description='fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate (
    template="Give 3 fact about the {topic}. \n {format_instruction}",
    input_variables=['topic'],
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke ({'topic' : 'Black Hole'})

print (result)