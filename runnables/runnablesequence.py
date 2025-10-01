## Runnable Sequence:
# RunnableSequence is a sequential chain of runnables in Langchain that executes each step one after another, passing the output of one step as the input of the next.
# It is useful when you need to compose multiple runnables together in a structured workflow.

# R1----> R2 can be sequentially connected as RunnableSequence([R1, R2])

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ['topic'] 
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)
prompt2 = PromptTemplate(
    
    template= "Explain the following joke-{text} ",
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({'topic': 'Technology'})

print(result)






