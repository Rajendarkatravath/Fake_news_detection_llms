import streamlit as st
from fake_news_detection import classify_article
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up Streamlit UI with a wide layout
st.set_page_config(page_title="Fake News Detection System", layout="wide")

# Main content
st.markdown("""
    <style>
        .main-text {
            font-size: 2em;
            text-align: center;
            margin-top: 2em;
        }
        .input-section {
            margin-left: auto;
            margin-right: auto;
            width: 80%;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-text">Fake News Detection System</p>', unsafe_allow_html=True)
st.markdown('<p class="main-text">Enter the news article below to classify it as real or fake.</p>', unsafe_allow_html=True)

# News Article Input section with centered alignment and full-width style
st.markdown('<div class="input-section">', unsafe_allow_html=True)
news_article = st.text_area("", height=300)
st.markdown('</div>', unsafe_allow_html=True)

if st.button('Classify'):
    if news_article:
        with st.spinner("Classifying the news article..."):
            result = classify_article(news_article)
            st.subheader("Classification Result")
            st.write(result)
    else:
        st.write("Please enter a news article.")
