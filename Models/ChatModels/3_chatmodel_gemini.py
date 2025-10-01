from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-xyz", temperature= 0.3, max_completion_tokens= 128)

result= model.invoke("What is the capital of india?")

print(result.content)