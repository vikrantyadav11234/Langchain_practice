from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  
from langchain_core.output_parsers import JsonOutputParser     
load_dotenv()   

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.2-3B-Instruct" ,
    task = "text-generation",
    max_new_tokens=512 
    )

model = ChatHuggingFace(llm=llm, temperature=0)

parser = JsonOutputParser()
# template = PromptTemplate(
#     template = "Give me the name age and city of a fictional person \n {format_instruction}" ,
#     input_variables = [],
#     partial_variables = {"format_instruction": parser.get_format_instructions()}
# )

# prompt = template.format()

# result = model.invoke(prompt)   

# final_result = parser.parse(result.content)




template = PromptTemplate(
    template = "Give me five facts about {topic} \n {format_instruction}" ,
    input_variables = ["topic"],
    partial_variables = {"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser
final_result = chain.invoke({"topic" : "Artificial Intelligence"})
print(final_result)
# print(type(final_result))

