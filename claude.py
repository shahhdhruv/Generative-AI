from langchain_anthropic import ChatAnthropic
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("A_KEY")
 
llm = ChatAnthropic(model="claude-1.3",api_key=api_key)

#INITIALISING BUFFER MEMORY
memory =  ConversationBufferMemory(
    memory_key = "messages",
    return_messages = True,
    chat_memory= FileChatMessageHistory("claude.json")
)


#PROMPTS
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages=[
        MessagesPlaceholder(variable_name = "messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

#CHAINS
chain = LLMChain(
    llm=llm,
    prompt = prompt,
    memory = memory
)
st.title("Conversational Chatbot with Claude API")
user_input = st.text_input("You:", "")

if st.button("Send"):
    response = chain.invoke({"content": user_input})
    st.text_area("Bot:", response["text"])
