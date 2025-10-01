from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash", temperature=0)

loader = TextLoader("/home/ubuntu/Langchain/data_loaders/sample.txt", encoding= "utf8")

docs = loader.load()


prompt = PromptTemplate(
    template = "Write a summary for the following resume:\n {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"text": docs[0].page_content})

print(result)


# print(docs)

# print(type(docs))

# print(len(docs))
# print(docs[0].metadata)
# print(docs[0].page_content)