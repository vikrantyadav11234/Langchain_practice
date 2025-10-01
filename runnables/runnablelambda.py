# RunnableLambda
# RunnableLambda is runnable premitive that allows you to apply custom python functions within an AI pipeline.
# It acts as middleware between different AI components, enabling preprocessing, transformation, API calls, filtering, and post processing in Langchain workflow.

# see notes as well for example explaination 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',    
                            #    api_key=os.getenv("GOOGLE_API_KEY"),
                            #    transport="rest",
                               temperature=0)


def word_counter(text):
    """Counts the number of words in the input text."""
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)
prompt = PromptTemplate(
    template = "Generate a joke about {topic}",
    input_variables = ['topic']
)

parser= StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": runnable_word_counter
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'Technology'})
print(result)