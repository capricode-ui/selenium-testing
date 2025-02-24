import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import streamlit as st

# Configure Selenium to use Firefox in headless mode
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode

# Start Firefox WebDriver
service = Service("/usr/bin/geckodriver")  # Geckodriver is pre-installed in Streamlit
driver = webdriver.Firefox(service=service, options=firefox_options)

# Streamlit UI
st.title("Selenium Test on Streamlit with Firefox")

st.write("Opening Google Homepage...")
driver.get("https://www.google.com")
time.sleep(2)  # Allow page to load

# Get the title of the page
title = driver.title
st.write(f"Page title: {title}")

# Close driver
driver.quit()
