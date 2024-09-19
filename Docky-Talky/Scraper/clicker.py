#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .recorder import CrawledLinksLogger

import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class WebDriverInitializer:
    def __init__(self, browser_type='chrome', url=None):
        self.browser_type = browser_type
        self.url = url
        self.driver = None

    def initialize(self):
        if self.browser_type.lower() != 'chrome':
            raise ValueError(f"Unsupported browser_type: {
                             self.browser_type}")
        if self.url is None:
            raise ValueError("URL cannot be None.")

        options = webdriver.ChromeOptions()
        options.add_argument("--port=4444")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)

        return self.driver

class ClickerGenerator:
    def __init__(self, driver, locator_type='xpath', locator=None):
        self.driver = driver
        self.locator_type = locator_type
        # checking link_locator before initializing ClickerGenerator
        self.locator = locator or '//a[@data-content_level="開放閱讀"]'

    def generate(self, limit=None):
        if not isinstance(self.driver, webdriver.Chrome):
            raise ValueError(
                "Unsupported webdriver instance: Only Chrome webdriver is supported.")

        try:
            print("Attempting to find elements...")

            if self.locator_type.lower() == "xpath":
                elements = self.driver.find_elements(By.XPATH, self.locator)
                logger.info(f"Generating links using locator: {
                            self.locator}")
            elif self.locator_type.lower() == "css":
                elements = self.driver.find_elements(
                    By.CSS_SELECTOR, self.locator)
            else:
                raise ValueError(f"Unsupported locator_type: {
                                 self.locator_type}")

            # Use set to remove duplicated links to keep links unique
            links = list(set(element.get_attribute('href')
                         for element in elements))

            # Initialize CrawledLinksLogger to check if links already clicked
            crawled_links_logger = CrawledLinksLogger()

            # Update the original 'links' list
            links = crawled_links_logger.find_new_uncrawled_links(links)
            
            # check if any duplicated links
            for link in links[:limit]:
                print(link, end="\n")

            # check IndexError of limit
            limit = len(links) if limit > len(links) else limit
            
            print(f"Found {len(links)} links to click.")
            links = links[:limit]
            return links
        except Exception as e:
            raise ValueError(f"Operation failed: {str(e)}")

    def quit_driver(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    target_url = "https://house.udn.com/house/index"

    target_initializer = WebDriverInitializer(url=target_url)
    target_driver = target_initializer.initialize()

    if target_driver is None:
        logger.error(
            "Failed to initialize WebDriver for target URL. Exiting.")
        exit()

    # Create ClickerGenerator without specifying a locator (uses default)
    clicker = ClickerGenerator(driver=target_driver)

    links = clicker.generate(limit=3)
    logger.info(f"Found {len(links)} links to click")

    clicker.quit_driver()
