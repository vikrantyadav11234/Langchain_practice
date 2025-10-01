from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = "/home/ubuntu/Langchain/data_loaders", glob ="*.pdf", 
    loader_cls=PyPDFLoader
    )

# docs = loader.load()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
    print("\n\n")
