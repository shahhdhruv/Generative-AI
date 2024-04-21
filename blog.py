import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain.chains.llm import LLMChain

# Load environment variables

## Function To get responses from Gemini Pro LLM model
llm=Ollama(model="llama2")
def getResponse(input_text, no_words, blog_style):
    
    ## Prompt Template

    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )
    
    inputs = {
        'input_text': input_text,
        'no_words': no_words,
        'blog_style': blog_style
    }
    chain = LLMChain(
        prompt=prompt,
        llm=llm
    )
    
    ## Generate the response from the Gemini Pro LLM model
    response = chain.invoke(input=inputs)
    print(response["text"])
    return response["text"]

st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## creating to more columns for additional 2 fields

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')

with col2:
    blog_style = st.selectbox(
        'Writing the blog for',
        ('Researchers', 'Data Scientist', 'Common People'),
        index=0
    )
    
submit = st.button("Generate")

## Final response
if submit:
    st.write(getResponse(input_text, no_words, blog_style))
