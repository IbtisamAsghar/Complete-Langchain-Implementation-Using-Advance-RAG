from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings (model_name = 'sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Islamabad is the capital of Pakistan",
    "Madrid is the capital of the Spain",
    "Paris the capital of the France"
]

vector = embedding.embed_documents(docs)

print(str(vector))