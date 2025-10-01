from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)

parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the text, either positive or negative")


parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text as positive or negative. \n {feedback} \n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)   

classifier_chain = prompt1 | model | parser2


# result = classifier_chain.invoke({'text': 'The product is great and works as expected!'}).sentiment
prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback |n {feedback}',
    input_variables = ['feedback']  )
prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback |n {feedback}',
    input_variables = ['feedback']  )   

chain1 = prompt2 | model | parser
chain2 = prompt3 | model | parser

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', chain1),
    (lambda x:x.sentiment == 'negative', chain2),
    RunnableLambda(lambda x: "Not able to find sentiment sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'The product is not as good as i expected!'})
print(result)
         

