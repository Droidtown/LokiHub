import os
import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .clicker import WebDriverInitializer, ClickerGenerator
from .parser import NewsParser, Locator
from .recorder import CrawledLinksLogger

from NLU.common import AccountManager, CrawledDataManager
from NLU.clustering_manager import GreedySlimeManager
from NLU.copyToaster_manager import CopyToasterManager

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def run_scraper(target_url, filename, link_locator=None, limit=None, directory="data"):
    try:
        logger.info(f"Initializing WebDriver for URL: {target_url}")
        target_initializer = WebDriverInitializer(url=target_url)
        target_driver = target_initializer.initialize()

        # Initialize AccountManager
        account_manager = AccountManager(filename="config/account.info")

        # Initialize Locator
        locator = Locator()

        # Initialize CrawledLinksLogger instance
        crawled_links_logger = CrawledLinksLogger()

        if target_driver is None:
            logger.error(
                "Failed to initialize WebDriver for target URL. Exiting.")
            return None, None

        logger.info("WebDriver initialized successfully for target URL")

        # Create ClickerGenerator using the default locator
        clicker = ClickerGenerator(
            driver=target_driver, locator=link_locator)

        # Explicit wait for the presence of links
        # Wait up to 20 seconds (adjust as needed)
        wait = WebDriverWait(target_driver, 20)
        element_present = EC.presence_of_all_elements_located(
            (By.XPATH, clicker.locator))
        wait.until(element_present)

        # Generate links and filter uncrawled ones
        links = clicker.generate(limit=limit)
        logger.info(f"Found {len(links)} links to click")

        # Filter out already crawled links
        links = crawled_links_logger.find_new_uncrawled_links(links)

        # Parse webpage
        news_parser = NewsParser(driver=target_driver)
        results = []
        for link in links:
            try:
                if news_parser.get_page_with_retries(url=link):

                    result = news_parser.parse(
                        url=link, locator_key="default")
                    if result:
                        results.append(result)
                        crawled_links_logger.write_crawled_link(link)
            except Exception as e:
                logger.error(f"Failed to load {
                             link} after multiple attempts: {str(e)}")

        logger.info(f"Results collected for {filename}: {results}")
        full_path = news_parser.save_results_to_json(
            results, filename, directory=directory)

        # GreedySlime Manager
        greedySlime_manager = GreedySlimeManager(account_manager)
        greedySlime_manager.build_model(filename)

        source = greedySlime_manager.extract_and_transform_clusters()

        # CopyToaster Manager
        copyToater_manager = CopyToasterManager(account_manager)
        copyToater_manager.build_model(filename, source)       

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return None, None
    finally:
        if target_driver:
            target_driver.quit()        
