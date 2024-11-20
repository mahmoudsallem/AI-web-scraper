from os import sep
import traceback#-
from selenium import webdriver#-
from selenium.webdriver.chrome.service import Service as ChromeService#-
from selenium.webdriver.firefox.service import Service as FirefoxService#-
from webdriver_manager.chrome import ChromeDriverManager#-
from webdriver_manager.firefox import GeckoDriverManager#-
from selenium.webdriver import Remote, ChromeOptions#-
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection#-
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#-
AUTH = 'brd-customer-hl_76c70359-zone-kabtsh_solver:kx8hlcr555kp'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(WebsiteURL):
    print("Starting the web scraping function.")
    driver = "/drivers/debian-binary"  # Initialize the driver variable

    try:
        # Attempt to use Chrome browser first
        try:
            print("Trying to initialize Chrome browser...")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            print("Chrome browser successfully initialized.")
        except Exception as e:
            print("Failed to initialize Chrome browser.")
            print("Error:", str(e))
            print("Attempting to initialize Firefox browser...")

            # Attempt to use Firefox if Chrome fails
            try:
                service = FirefoxService(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=service)
                print("Firefox browser successfully initialized.")
            except Exception as e:
                print("Failed to initialize Firefox browser.")
                print("Error:", str(e))
                traceback.print_exc()
                raise Exception("No supported browser found. Please install Chrome or Firefox.")

        print('Connecting to Scraping Browser...')
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
        with Remote(sbr_connection, options=ChromeOptions()) as remote_driver:
            print('Connected! Navigating...')
            remote_driver.get(WebsiteURL)
            print('Taking page screenshot to file page.png')
            remote_driver.get_screenshot_as_file('./page.png')
            print('Navigated! Scraping page content...')
            html = remote_driver.page_source
            print("Page source retrieved successfully.")
            return html

    except Exception as e:
        print("An unexpected error occurred during the scraping process.")
        print("Error:", str(e))
        traceback.print_exc()

    finally:
        if driver:
            print("Closing the browser.")
            driver.quit()
        else:
            print("No browser was initialized; nothing to close.")

def extraxt_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_contet = soup.body  
    if body_contet:
        return str(body_contet)
    return ""

def clean_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    for script_or_style  in soup("script" ,"style"):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]