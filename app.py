import streamlit as st
from Fact_Check import check_fact
from openai import OpenAI

# Set up OpenAI GPT-4 API key (this should be kept secret, and you should consider using Streamlit's Secrets Management for production)
client = OpenAI(
            api_key=os.environ.get('OPEN_AI_API_KEY')
        )

st.title("Welcome to Dr. Eagle's Fact Checking Service")

st.write("Hello! I'm Dr. Eagle, your fact-checking assistant. What do you want me to fact check?")

# Create a text area for user input
user_input = st.text_area("Enter your query below:", height=200)

# Create a button for submitting the fact check request
if st.button("Submit"):
    with st.spinner('Dr. Eagle is busy fact-checking your claim. Please wait...'):
        fact_check_result = check_fact(user_input, client)
        st.write(fact_check_result)
