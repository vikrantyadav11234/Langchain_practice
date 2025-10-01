#pdf reader application using langchain

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
# Load documents

loader = TextLoader("docs.txt")
documents = loader.load()

# split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# create embeddings and store them in a vector store Faiss
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# create a retriver ( fetch relevent documents from the vector store)

retriever = vectorstore.as_retriever()

# # manually retrive relevent documents
# query = "What are the key takeaways from the document?"
# relevent_docs = retriever.get_relevant_documents(query)


# # combine retrived text into a single prompt
# retrived_text = "\n".join([doc.page_content for doc in relevent_docs])

# initialize the LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "What are the key takeaways from the document?"
response = qa_chain.run(query)

print(f"Response: {response}")








