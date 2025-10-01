from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-3.5-sonnet-20241022', temperature=0.3, max_completion_tokens= 128)

result = model.invoke("what is the calital of india?")

print(result.content)


