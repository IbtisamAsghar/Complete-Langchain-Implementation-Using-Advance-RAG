from langchain_community.document_loaders import DirectoryLoader ,PyPDFLoader

loader = DirectoryLoader(
    path = 'Books',
    glob = '*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs[3].page_content)