from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate five interesting facts about {topic}',
    input_variables = ['topic'] 
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)   

parser = StrOutputParser()

chain = prompt | model | parser # langchain expression language (LCEL)

result = chain.invoke({'topic': 'Machine Learning'})
print(result)


chain.get_graph().print_ascii()  # to visualize the chain