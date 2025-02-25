import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Configure Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run without UI

# Use Geckodriver (already available on Streamlit Cloud)
service = Service("/usr/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=firefox_options)

# Streamlit UI
st.title("Selenium Test on Streamlit (Using Firefox)")

st.write("Opening Google Homepage...")
driver.get("https://www.google.com")
time.sleep(2)  # Allow page to load

# Get the title of the page
title = driver.title
st.write(f"Page title: {title}")

# Close driver
driver.quit()
