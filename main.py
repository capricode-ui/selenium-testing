import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Function to scrape a webpage
def scrape_website(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    title = driver.title  # Get the title of the page
    driver.quit()
    return title

st.title("Selenium on Streamlit Cloud")
url = st.text_input("Enter website URL")

if st.button("Scrape"):
    if url:
        result = scrape_website(url)
        st.success(f"Page Title: {result}")
    else:
        st.warning("Please enter a valid URL")
