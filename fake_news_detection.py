import openai
from langchain import LLMChain, PromptTemplate
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# GROQ API key
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize Llama 3 model using ChatGroq with the GROQ API
llama3_model = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-70b-8192")

# Define the prompt template for fake news detection
fake_news_template = """
You are a fake news detection system. Analyze the following news article and classify it as 'real' or 'fake' based on its content:

Article: {article_text}
"""

# Create prompt using LangChain
fake_news_prompt = PromptTemplate(template=fake_news_template, input_variables=["article_text"])

# Initialize the LangChain LLMChain with the Llama 3 model
fake_news_chain = LLMChain(llm=llama3_model, prompt=fake_news_prompt)

def classify_article(article_text):
    response = fake_news_chain.run({"article_text": article_text})
    return response
