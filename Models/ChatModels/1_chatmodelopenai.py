from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model = "gpt-4o")
model = ChatOpenAI(model = "gpt-4o", temperature = 0.3, max_completion_tokens = 128)

result = model.invoke("What is the capital of India.")

# print(result)

print(result.content)
