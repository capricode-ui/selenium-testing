import os
import subprocess
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import streamlit as st

# Install Google Chrome manually
def install_chrome():
    if not os.path.exists("/usr/bin/google-chrome"):
        subprocess.run(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && "
            "apt-get update && "
            "apt-get install -y ./google-chrome-stable_current_amd64.deb",
            shell=True, check=True
        )

# Run Chrome installation
install_chrome()

# Set Chrome binary path
os.environ["CHROME_BIN"] = "/usr/bin/google-chrome"

# Install and get the path to ChromeDriver
chromedriver_path = chromedriver_autoinstaller.install()

# Configure Selenium WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ["CHROME_BIN"]
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Streamlit UI
st.title("Selenium Test on Streamlit")

st.write("Opening Google Homepage...")
driver.get("https://www.google.com")
time.sleep(2)  # Allow page to load

# Get the title of the page
title = driver.title
st.write(f"Page title: {title}")

# Close driver
driver.quit()
