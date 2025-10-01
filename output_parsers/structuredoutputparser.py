from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.2-3B-Instruct" ,
    task = "text-generation",
    max_new_tokens=512 
    )       
model = ChatHuggingFace(llm=llm, temperature=0)

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template = "Give me three facts about {topic} \n {format_instruction}" ,
    input_variables = ["topic"],        
    partial_variables = {"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser       

final_result = chain.invoke({"topic" : "Artificial Intelligence"})
print(final_result)
print(type(final_result))