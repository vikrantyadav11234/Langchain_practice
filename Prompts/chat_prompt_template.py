from langchain_core.prompts import ChatPromtTemplate
from langchain_core.messages import SystemMessage, HumanMessage


chat_template = ChatPromtTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('user',"Explain in simple terms what is {topic}" )
                                  
    # SystemMessage(content= "You are a helpful {domain} expert"),
    # HumanMessage(content= "Explain in simple terms what is {topic}")
])

prompt = chat_template.invoke({'domain': 'cricket',
                               'topic':'Dusra'})

