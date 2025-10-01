from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain.output_parsers import OutputFixingParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it" ,
    task = "text-generation",
    max_new_tokens=512
    )       
model = ChatHuggingFace(llm=llm, temperature=0) 

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18, description="The person's age")
    city: str = Field(discription="The city where the person lives")
    
    
parser = PydanticOutputParser(pydantic_object=Person)
# parser = OutputFixingParser.from_llm(parser=base_parser, llm=model)
template = PromptTemplate(
    template = "Generate the name age and city of a fictional {place}person \n {format_instruction}" ,
    input_variables = ["place"],
    partial_variables = {"format_instruction": parser.get_format_instructions()}
)
# prompt = template.format(place="india")
# print(prompt)
chain = template | model | parser

final_result = chain.invoke({"place":"india"})
print(final_result)