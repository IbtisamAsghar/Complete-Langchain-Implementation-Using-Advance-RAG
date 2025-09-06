from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001' , dimension = 32)

text = "Islamabad is the cpital of the Pakistan"

result = embedding.embed_query(text)



print(str(result))