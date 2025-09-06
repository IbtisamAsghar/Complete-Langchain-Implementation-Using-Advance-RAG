from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

docs = [
    "Babar Azam ,Pakistan’s batting backbone, known for his elegant stroke play and consistency across all formats.",

    "Shaheen Afridi ,A lethal left-arm pacer, capable of swinging the new ball and delivering deadly yorkers in the death overs.",

    "Mohammad Rizwan  ,A dependable wicketkeeper-batsman, excelling in anchoring innings and accelerating when needed.",

    "Haris Rauf , One of the fastest bowlers in world cricket, famous for his raw pace and ability to bowl under pressure.",

    "Shadab Khan ,A dynamic all-rounder, providing crucial middle-order runs and key breakthroughs with his leg-spin."
]

query = "tell me about Rizwan"

doc_embedding = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding] , doc_embedding)[0] # must be a 2d vector

# now we want to fetch the relevent document 

# 1.sort thr scores basis on the similarity score
index , score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]

print(docs[index])
print('similarity score is :',score)