# RunnableParallel
## Runnable parallel is a runnable primitive that allows multiple runnables to execute in parallel.
## Each number recieves the same input and process it independently, producing a dictionary of outputs.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',    
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)

prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a blog post about {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "blog_post": RunnableSequence(prompt2, model, parser)   
}
)

result = parallel_chain.invoke({'topic': 'Technology'})

print(result['tweet'])