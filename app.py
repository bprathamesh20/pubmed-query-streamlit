import os 


import streamlit as st 
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

st.title("PubMed APP")
llm = OpenAI()
tool = PubmedQueryRun()

query_prompt = PromptTemplate(input_variables=['article', 'query'], template='Your are helpful medical bot . Respond to below user query {query} with reference to these articles {article}. Also provide references included in the answer')

input = st.text_input("Enter your query")
article = tool.run(input)
query_chain = LLMChain(prompt=query_prompt, llm=llm)

response = query_chain.run({"article": article, "query": input})


if st.button('Search'):
    st.write(response)