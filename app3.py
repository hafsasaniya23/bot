from langchain import HuggingFaceHub
import streamlit as st
from dotenv import load_dotenv

load_dotenv()



# Streamlit interface
def get_response(joke):
    prompt_chain = HuggingFaceHub(repo_id="naltukhov/joke-generator-rus-t5", model_kwargs={"temperature":0, "max_length": 512})
    response=prompt_chain(joke)
    return response


st.set_page_config(page_title="joke")
st.header("make you self happy  ")
input= st.text_input("enter the word : ",key="joke")
submit= st.button("Check")

if submit:
    st.write(get_response(input))