from langchain import HuggingFaceHub
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

load_dotenv()


## chain creation

llms_huggingface= HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":1,"max_length":150,})

fact_prompt= PromptTemplate(input_variables=["fruit"],template="tell me the fact value of {nutrition}")
fact_chain= LLMChain(llm=llms_huggingface,prompt=fact_prompt)
sfact_prompt= PromptTemplate(input_variables=["nutrition"],template="give us short information about the {fruit}")
sfact_chain_chain= LLMChain(llm=llms_huggingface,prompt=sfact_prompt)


Just_chains=SimpleSequentialChain(chains=[fact_chain,sfact_chain_chain])


# Streamlit interface

def get_response(fruit):
    response=(Just_chains.run(fruit))
    return response

def main():
    ## css
    st.markdown(
        f"""
        <style>
        .stApp {{background-image: linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
            
          
        </style>
        """,
        unsafe_allow_html=True
    )

custom_css = """
<style>
body {
    font-family: Georgia, serif;
    background-color: #f5f5f5;
}
.stButton button {
    background-color: #ffe600;
    color: blue;
    border: none;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 25px;
    margin: 4px 2px;
    font-weight: bold;
    transition-duration: 0.4s;
    cursor: pointer;
}
.stButton button:hover {
    background-color: white;
    color: black;
    border: 4px solid #4CAF50;
}
.bold-text {
    font-family: cursive, serif;
    font-size: 20px;  /* Font size */
    font-weight: bold;  /* Bold text */
    color: #333;  /* Text color */
}

</style>
"""

# Inject CSS with markdown

st.markdown(custom_css, unsafe_allow_html=True)
st.header("Fruit Facts")
input= st.text_input("Enter the Fruit: ",key=["nutrition"])
submit= st.button("Get Fact")


if submit:
    st.markdown(f'<div class="bold-text">{get_response(input)}</div>', unsafe_allow_html=True)
   

if __name__ == "__main__":
    main()