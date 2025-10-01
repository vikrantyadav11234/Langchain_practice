from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


# 1. 1st iteration
# while True:
#     user_input = input('You:')
    
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input) 
#     print("AI:", result.content)
    
    
    
## Problems in 1st iteration  Chatbot
# """
# 1. this chatbot does not have context of previous questions.
# 2. We have to maintain a chat history.
# 3. So that if we ask again regarding previous information it will understand 
#    what is being asked?
# """

2. 2nd iteration

chat_history = []

while True:
    user_input = input('You:')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history) 
    chat_history.append(result.content)
    print("AI:", result.content)
print(chat_history)

### Problems with 2nd iterations
# 1. In above example chat we are saving chat history but we are not 
#   saving that which msg is sent by whom. No information of user or AI.
# 2.  it should be like this:
#     {user: "",
#     AI : "",}
# #. This will be done by the builtin classes of Langchain

# 3. 3rd iteration

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_history = [
    SystemMessage(content = 'You are an helpful AI Assistant')
]

while True:
    user_input = input('You:')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history) 
    chat_history.append(AIMessage(content = result.content))
    print("AI:", result.content)
print(chat_history)

