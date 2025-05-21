import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Real Estate Insights", layout="wide")

# Title and Introduction
st.title("🏡 Real Estate Price Prediction")
st.markdown("""
Welcome to the Real Estate Insights Platform! This powerful tool empowers you to estimate property values, track market trends, and receive tailored recommendations based on location, property features, and current market conditions. Whether you're buying, selling, or investing, gain in-depth insights to make smart and confident real estate decisions. 🚀
""")

st.header("📌 Key Features")
st.markdown("""
    - *Price Prediction:* Get an estimated price range for properties based on various features.
    - *Market Analytics:* Visualize sector-wise trends, price distributions, and more.
    - *Property Recommendations:* Get personalized apartment recommendations based on key property features and market trends.
    """)