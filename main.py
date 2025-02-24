import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

def scrape_website(url):
    service = Service()  # No need to specify executable_path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    title = driver.title
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
