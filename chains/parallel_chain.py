from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.schema.runnable import RunnableParallel
load_dotenv()


model1 = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            
                            
                                 temperature=0)

# model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
#                             #    api_key=os.getenv("GOOGLE_API_KEY"),
#                                  temperature=0)

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text. \n {text}',
    input_variables = ['text'] 
)   

prompt2 = PromptTemplate(
    template = 'Generate a five short question answers from the following text. \n {text}',
    input_variables = ['text'] 
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n {notes} and {quiz}',
    input_variables = ['notes', 'quiz']
)   

parser = StrOutputParser()



# chain1 = prompt1 | model1 | parser # langchain expression language (LCEL)
# chain2 = prompt2 | model2 | parser
# chain3 = prompt3 | model1 | parser
parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "quiz": prompt2 | model1 | parser,
    }
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'text': 'Machine Learning is a field of artificial intelligence that focuses on the development of algorithms and statistical models that enable computers to perform specific tasks without explicit instructions. It involves the use of data and patterns to make predictions or decisions, allowing systems to learn and improve from experience. Machine learning encompasses various techniques, including supervised learning, unsupervised learning, and reinforcement learning, and is widely used in applications such as image recognition, natural language processing, recommendation systems, and autonomous vehicles.'})
print(result)