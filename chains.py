from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="Python")
args = parser.parse_args()

llm = ChatAnthropic(model_name="claude-1.3", anthropic_api_key="#your_key_here")

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language","task"]
)

code_prompt2 = PromptTemplate(
    template="Write a test for the following {language} code:\n{code}",
    input_variables=["language","code"]
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt, 
    output_key="code"
)
code_chain2 = LLMChain(
    llm=llm,
    prompt = code_prompt2,
    output_key="test"
    
)
chain = SequentialChain(
    chains = [code_chain, code_chain2],
    input_variables = ["task","language"],
    output_variables = ["test","code"]   
)
result = chain.invoke({"language": args.language,
                            "task": args.task })
print(">>>>>>> GENERATED CODE: ")
print(result["code"])

print(">>>>>>> GENERATED TEST: ")
print(result["test"])
# #streamlit framework
# st.title("Custom Chatbot")

# name = st.text_area("Enter the prompt")
# clicked = st.button("Generate Prompt")
# if clicked:
#         result = code_chain.invoke({"language": "python",
#                                     "task": "write a code to print a pyramid pattern with (*)"})
#         st.write(result["text"])
