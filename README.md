# AI Web Scraper

This is a web scraper application built using Python, Streamlit, and Altair. It allows users to scrape a website and extract specific content based on their input.

## Project Process

1. Design: Define the project requirements, including the desired functionality and user interface.

2. Set up the development environment: Install Docker, Python, and any necessary dependencies.

3. Create a Dockerfile: Define the Docker image for the application, including the base image, dependencies, and runtime configuration.

4. Build the Docker image: Use the Dockerfile to build a Docker image of the application.

5. Create a Streamlit app: Develop the main Streamlit application file (`main.py`) that handles user input, scraping, and parsing.

6. Implement web scraping logic: Write functions to scrape the website, extract specific content, and clean the data.

7. Implement parsing logic: Integrate a language model (e.g., Ollama) to parse the scraped content based on user input.

8. Test and debug: Test the application locally to ensure it functions correctly and handles edge cases.


## User Documentation

### Getting Started

``` 
1. Clone the repository:

 git clone https://github.com/your-username/ai-web-scraper.git

 cd ai-web-scraper

 streamlit run main.py