from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(model = "gpt-3.5-turbo", temperature=0.7)

#create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a cachy blog title about {topic}."
)

topic = input ("Enter a topic: ")

# format the prompt manually using prompt template
formatted_prompt = prompt.format(topic=topic)

# get the response from the LLM
blog_title = llm.predict(formatted_prompt)

print(f"Suggested blog title: {blog_title}")