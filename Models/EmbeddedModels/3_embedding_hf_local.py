from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name =" sentence_transformer/all-MiniLM-l6-v2" )

# text = ' Delhi is the capital of india.'

documents = [
    "Delhi is the capital of India."
    "Kolkata is the capital of west bengal."
    "Paris is the capital of france."
]

# result = embeddings.embed_query(text)
result = embeddings.embed_documents(documents)

print(str(result))