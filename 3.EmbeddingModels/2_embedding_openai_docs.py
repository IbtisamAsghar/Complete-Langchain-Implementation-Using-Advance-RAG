from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model= OpenAIEmbeddings(model='text-embedding-3-large' ,dimensions=32)


docs = [
    "Islamabad is the capital of Pakistan",
    "Madrid is the capital of the Spain",
    "Paris the capital of the France"
]


result = embedding_model.embed_documents(docs)

print(str(result))