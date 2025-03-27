import streamlit as st
import os
from dotenv import load_dotenv 

# Langchain and LLM related package inclusion
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

load_dotenv()

## Environment variable
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Please help to answer the user queries" ),
        ("user", "Question:{question}" )
    ]
)

 
st.title("Welcome to NLQ chatbot page")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = []

# The context input
input_data = st.text_input("Input your text here")
submit = st.button("Submit")

if submit:
    #st.session_state["my_input"].append(input_data)

    #for input in st.session_state["my_input"]:
    #    st.write(f"You entered {input}")
    llm=Ollama(model="llama2")
    output_parser=StrOutputParser()

    #Chain
    chain=prompt|llm|output_parser

    st.write(chain.invoke({'question': input_data}))
