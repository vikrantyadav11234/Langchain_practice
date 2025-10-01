from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)   

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template = 'Generate detail report on {topic}',
    input_variables = ['topic'] 
)

prompt2 = PromptTemplate(
    template = 'Generate a five pointer summary from the following text. \n {text}',
    input_variables = ['text'] 
)

chain = prompt1 | model | parser | prompt2 | model | parser # langchain expression language (LCEL)

result = chain.invoke({'topic': 'Machine Learning'})
print(result)


chain.get_graph().print_ascii()  # to visualize the chain