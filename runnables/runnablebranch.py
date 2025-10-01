from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',    
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0) 

  
prompt1 = PromptTemplate(
    template ='Write a detail report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "summarize the following text \n {text}",
    input_variables = ['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic': 'Technology'})

print(result) 


