from altair import Url
import streamlit as st
from scrape import (
    scrape_website 
    ,split_dom_content 
    ,clean_body_content 
    ,extraxt_body_content
    )
from Model import parse_with_ollama

st.title("AI Web Scraper")

url = st.text_input("Enter a Website URL : ")

if st.button("Scrape Site") and url:
    st.write("Scraping Started")
    
    result = scrape_website(url) 
    print("Scraped result:", result)  # Add this line to check the scraped result

    body_content = extraxt_body_content(result)
    clean_content =  clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View Dom content") :
        st.text_area("Dom content " , clean_content , height=500)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)