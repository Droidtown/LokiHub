import os
import json
import hashlib
import logging
from glob import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from .recorder import CrawledLinksLogger

logger = logging.getLogger(__name__)

# 特殊符號列表
splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";", "｜", "▸"]

class Locator:
    def __init__(self):
        self.locators = {
            "default": {
                "title_xpath": '//h1[@class="article-content__title"] | //h1[@class="story_art_title"] | //h1[@id="story_art_title"] | //h1[@class="story-title"]',
                "content_xpath": '//section[@class="article-content__editor"]/p | //section[@class="article-content__editor "]/p | //p',
                "time_xpath": '//time[@class="article-content__time"] | //div[@id="story_bady_info"] | //time[@class="article-body__time"] | //time[@class="article-content__time"]'
            },
            # Add more locator sets as needed
        }

class NewsParser:
    def __init__(self, driver):
        self.__driver = driver
        self.locator = Locator()  # Initialize Locator instance

    def _get_elements_text(self, xpath, multiple=False):
        try:
            if multiple:
                elements = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath))
                )
                return [element.text for element in elements]
            else:
                element = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                return element.text
        except (TimeoutException, WebDriverException) as e:
            logger.error(f"Error locating elements with XPath '{xpath}': {str(e)}")
            return None if not multiple else []

    def get_page_with_retries(self, url, retries=5, delay=5):
        for attempt in range(retries):
            try:
                self.__driver.get(url)
                return True
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed to load {url}: {str(e)}")
                time.sleep(delay)
        logger.error(f"Failed to load {url} after {retries} attempts")
        return False
    
    def clean_text(self, text):
        for char in splitLIST:
            text = text.replace(char, '')
        return text    

    def parse(self, url, locator_key="default"):
        if not self.get_page_with_retries(url):
            return None
    
        if locator_key not in self.locator.locators:
            logger.error(f"Locator key '{locator_key}' not found.")
            return None
    
        locators = self.locator.locators[locator_key]
    
        title = self._get_elements_text(locators["title_xpath"])
        content_elements = self._get_elements_text(
            locators["content_xpath"], multiple=True)
        time_element = self._get_elements_text(locators["time_xpath"])
    
        if not title or not content_elements or not time_element:
            logger.error(f"Failed to parse content from URL: {url}")
            return None
    
        title_hash = hashlib.sha256(title.encode('utf-8')).hexdigest()
    
        # Pass title and title_hash here
        if self.is_duplicate_title(title, title_hash):
            logger.info(f"Duplicate content found for title: {title}")
            return None
    
        content = self.clean_text("".join(content_elements))
    
        return {
            'title': title,
            'content': content,
            'time': time_element,
            'title_hash': title_hash
        }

    def is_duplicate_title(self, title, title_hash, directory='data', filename='parsed_news'):
        full_path = os.path.join(directory, f"{filename}.json")

        if not os.path.exists(full_path):
            return False

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)

            # Create a dictionary with hash as key and list of titles as values
            hash_to_titles = {}
            for item in existing_data:
                hash_value = item.get('title_hash')
                if hash_value:
                    if hash_value in hash_to_titles:
                        hash_to_titles[hash_value].append(item.get('title'))
                    else:
                        hash_to_titles[hash_value] = [item.get('title')]

            # Check if the hash exists in the dictionary and if the title matches
            return title_hash in hash_to_titles and title in hash_to_titles[title_hash]
        except Exception as e:
            logger.error(f"Error checking for duplicate title: {str(e)}")
            return False

    def save_results_to_json(self, results, filename, directory='data'):
            try:
                os.makedirs(directory, exist_ok=True)
                full_path = os.path.join(directory, f"{filename}.json")

                if os.path.exists(full_path):
                    with open(full_path, 'r', encoding='utf-8') as file:
                        existing_data = json.load(file)
                else:
                    existing_data = []

                new_results = []
                for result in results:
                    if not self.is_duplicate_title(result['title'], result['title_hash'], directory, filename):
                        new_results.append(result)

                existing_data.extend(new_results)

                with open(full_path, 'w', encoding='utf-8') as file:
                    json.dump(existing_data, file,
                              ensure_ascii=False, indent=4)

                logger.info(f"Results saved to {full_path}")
                return full_path
            except Exception as e:
                logger.error(f"Failed to save results to JSON: {str(e)}")
                return None

if __name__ == "__main__":
    from selenium import webdriver

    # Set up WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Initialize Locator and NewsParser
    locator = Locator()
    news_parser = NewsParser(driver)

    # Parse a specific URL
    url = 'https://tech.udn.com/tech/story/123154/8100016?from=redpush'
    parsed_data = news_parser.parse(url, locator_key="default")

    if parsed_data:
        news_parser.save_results_to_json(
            [parsed_data], 'house', 'data')
    else:
        logger.error("Failed to parse the news article.")

    driver.quit()
