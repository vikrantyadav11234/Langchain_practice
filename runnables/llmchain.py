from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(model = "gpt-3.5-turbo", temperature=0.7)

#create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a cachy blog title about {topic}."
)

topic = input ("Enter a topic: ")

chain = LLMChain(llm=llm, prompt=prompt)
# get the response from the LLM
topic = input("Enter a topic: ")
output = chain.run(topic=topic)

print(f"Suggested blog title: ", output)