# ## Langchain has three types of messages
# 1. System messages
# 2. Human messages
# 3. AI messages

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessage(content = ' Tell me about langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)