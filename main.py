import os
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Install Chrome
CHROME_URL = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
os.system(f"wget {CHROME_URL} -O chrome.deb")
os.system("dpkg -i chrome.deb || apt-get -fy install")

# Install Chromedriver
CHROMEDRIVER_URL = "https://chromedriver.storage.googleapis.com/119.0.6045.105/chromedriver_linux64.zip"
os.system(f"wget {CHROMEDRIVER_URL} -O chromedriver.zip")
os.system("unzip chromedriver.zip -d /usr/local/bin/")
os.system("chmod +x /usr/local/bin/chromedriver")

# Configure Selenium Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start Chrome WebDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Streamlit UI
st.title("Selenium Test on Streamlit Cloud")

st.write("Opening Google Homepage...")
driver.get("https://www.google.com")
time.sleep(2)  # Allow page to load

# Get the title of the page
title = driver.title
st.write(f"Page title: {title}")

# Close driver
driver.quit()
