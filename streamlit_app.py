import streamlit as st
import requests

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎥",
    layout="centered",
)

st.title("Movie Review Sentiment Analysis")
st.write("Enter a movie review and get instant sentiment prediction")

review = st.text_area("Enter your movie review here:", height=150)

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    "https://movie-review-analysis-13.onrender.com/predict",
                    json={"reviews": review}
                )
                result = response.json()
            except:
                st.error("Backend not running or connection failed")
                st.stop()

        sentiment = result.get('prediction', 'Unknown')

        if sentiment.lower() in ["positive", "negative"]:
            st.success(f"Sentiment: {sentiment}")
        else:
            st.error(f"Sentiment: {sentiment}")
