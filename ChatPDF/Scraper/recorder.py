#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import hashlib

class CrawledLinksLogger:
    def __init__(self, filename='config/crawled_links.json'):
        self.filename = filename

    def read_crawled_links(self):
        try:
            with open(self.filename, 'r') as file:
                crawled_links = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            crawled_links = []
        return crawled_links

    def write_crawled_link(self, link):
        crawled_links = self.read_crawled_links()
        if link not in crawled_links:
            crawled_links.append(link)
            with open(self.filename, 'w') as file:
                json.dump(crawled_links, file)

    def hash_link(self, link):
        return hashlib.sha256(link.encode('utf-8')).hexdigest()

    def find_new_uncrawled_links(self, links):
        # Initialize CrawledLinksLogger to check if links already clicked
        crawled_links = self.read_crawled_links()

        # Create a set for hashed crawled links
        crawled_links_set = set(self.hash_link(link)
                                for link in crawled_links)

        new_links = []
        for link in links:
            link_hash = self.hash_link(link)
            if link_hash not in crawled_links_set:
                new_links.append(link)
            else:
                # Check for hash collision by comparing full strings
                if link not in crawled_links:
                    new_links.append(link)

        return new_links


if __name__ == "__main__":
    crawled_links_logger = CrawledLinksLogger()
    new_links = crawled_links_logger.find_new_uncrawled_links(
        ['https://house.udn.com/house/story/123589/8097690?from=udn-indexhotnews_ch1025', 'https://house.udn.com/house/story/123591/8098519?from=udn-indexhotnews_ch1025'])
    print(new_links)    
