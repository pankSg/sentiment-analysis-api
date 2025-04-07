import streamlit as st
import requests

st.title("Sentiment Analyzer 🧠")
text = st.text_area("Enter text to analyze sentiment:")
if st.button("Analyze"):
    if text:
        # Call the sentiment analysis API
        response = requests.post("http://localhost:5000/analyze", json={"text": text})
        
        if response.status_code == 200:
            sentiment = response.json().get('sentiment')
            st.success(f"Sentiment: {sentiment}")
        else:
            st.error("Error analyzing sentiment.")
    else:
        st.warning("Please enter some text to analyze.")