from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel , Field
from langchain.schema.runnable import RunnableBranch , RunnableLambda , RunnableParallel
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-1.5-pro")
parser = StrOutputParser()

class Feedback (BaseModel) : 
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")

parser_2 = PydanticOutputParser(pydantic_object=Feedback)

prompt_1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser_2.get_format_instructions()}

)
classifier_chain = prompt_1 | model | parser_2 # output the positive or negative

prompt_2 = PromptTemplate(
    template="Generate a response to the positive feedback of the user\n {feedback}",
    input_variables=['feedback']
)

prompt_3 = PromptTemplate(
    template="Generate a response to the negative feedback of the user \n {feedback}",
    input_variables=['feedback']
)

chain_branch = RunnableBranch (
    (lambda x:x.sentiment == 'positive' , prompt_2 | model | parser),
    (lambda x:x.sentiment == "negative" , prompt_3|model|parser),
    RunnableLambda(lambda x: "Could not find the sentiment of the feedback")

)

chian = classifier_chain | chain_branch

result = chian.invoke({'feedback':'Ronaldo addition shoes is not awesome'})

print(result)