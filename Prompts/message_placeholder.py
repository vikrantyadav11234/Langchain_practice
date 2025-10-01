from langchain_core.prompts import ChatPromtTemplate, MessagePlaceholder


# chat template 
chat_template = ChatPromtTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagePlaceholder(variable_name = 'chat_history')
    ('user', '{query}')
])

# load chat history
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt

prompt = chat_template.invoke({'chat_history': chat_history,
                              'query': "Where is my order?"})

print(prompt )