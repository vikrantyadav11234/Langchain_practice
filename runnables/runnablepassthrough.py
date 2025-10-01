## RunnablePassthrough
# RunnablePassthrough is a special runnable primitive that simply returns the input as output without modifying it.


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',    
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)

prompt1 = PromptTemplate(
    template = "Generate a joke about {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template= "Explain the following joke-{text} ",
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)
explain_chain = RunnableSequence(prompt2, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": explain_chain
}) 


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'Technology'})
print(result)     