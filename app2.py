from langchain import HuggingFaceHub
import streamlit as st
from dotenv import load_dotenv

load_dotenv()



# Streamlit interface
def get_response(product):
    prompt_chain = HuggingFaceHub(repo_id="declare-lab/flan-alpaca-large", model_kwargs={"temperature":0, "max_length": 512})
    response=prompt_chain(product)
    return response


st.set_page_config(page_title="Product Information")
st.header("Get Product Information ")
input= st.text_input("enter the Product name: ",key="product")
submit= st.button("Check")

if submit:
    st.write(get_response(input))