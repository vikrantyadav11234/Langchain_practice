from langchain.text_splitter import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/home/ubuntu/Langchain/Text_splitter/Vikrant_june.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    separator='',
    chunk_size=10,
    chunk_overlap=0,
    
)


texts = splitter.split_documents(docs)

print(texts[0])