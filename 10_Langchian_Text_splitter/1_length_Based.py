from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader('eBook-How-to-Build-a-Career-in-AI.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)