import streamlit as st

st.title("AI Web Scraper")

url = st.text_input("Enter a Website URL : ")

if st.button("Scrape Sire") and url:
    st.write("Scraping Started")
