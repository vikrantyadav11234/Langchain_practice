# # import os
# from langchain_community.document_loaders import WebBaseLoader
# # os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# url ="https://search.yahoo.com/search?d=%7b%22dn%22%3a%22yk%22%2c%22subdn%22%3a%22company%22%2c%22ykid%22%3a%22da4c9972-f954-4705-aaf0-ce0f7334fc0b%22%7d&fr2=p%3ads%2cv%3aomn%2cm%3asa%2cbrws%3achrome%2cpos%3a2&fr=mcafee&type=E210US885G91952&p=Flipkart"

# loader = WebBaseLoader(url)

# docs = loader.load()
# print(docs)

from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url ="https://search.yahoo.com/search?d=%7b%22dn%22%3a%22yk%22%2c%22subdn%22%3a%22company%22%2c%22ykid%22%3a%22da4c9972-f954-4705-aaf0-ce0f7334fc0b%22%7d&fr2=p%3ads%2cv%3aomn%2cm%3asa%2cbrws%3achrome%2cpos%3a2&fr=mcafee&type=E210US885G91952&p=Flipkart"

loader = WebBaseLoader(url)

model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash", temperature=0)


docs = loader.load()
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Answer the following question \n {question}\n based on the following text:\n {text}",
    input_variables = ["question", "text"]
)

chain = prompt | model | parser

result = chain.invoke({"question": "What is Flipkart?", "text": docs[0].page_content})

print(result)





