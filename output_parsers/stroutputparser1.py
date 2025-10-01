from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.2-3B-Instruct" ,
    task = "text-generation", 
    temperature=0,
    max_new_tokens=512 ,
    
)

model = ChatHuggingFace(llm=llm, temperature=0)

# 1st prompt - detailed report
template1 = PromptTemplate(
    template = "Write a detailed report on {topic}" ,
    input_variables = ["topic"]
)

# 2nd prompt - summary
template2 = PromptTemplate(
    template = "Write a five line summary on the following text. /n {text}" ,
    input_variables = ["text"]
)

# string output parser are commonly used to ensure the output is always a string
# string output parsers are commonly used in chains in Lngchain

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic" : "Artificial Intelligence"})

print(result)