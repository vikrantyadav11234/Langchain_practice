from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.invoke({"topic" : "Artificial Intelligence"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text" : result.content})
summary = model.invoke(prompt2)

print("=== DETAILED REPORT ===")
print(result.content)
print("\n=== SUMMARY ===")
print(summary.content)