from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("/home/ubuntu/Langchain/data_loaders/Vikrant_june.pdf")

docs = loader.load()

print(len(docs))

# print(docs[0].metadata)
print(docs[0].page_content) 