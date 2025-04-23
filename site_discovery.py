# site_discovery.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

def discover_top_finance_sites(query="finance news", max_sites=3):
    """
    Scrape Bing News to discover top finance news domains.

    Args:
        query (str): Search query.
        max_sites (int): Max number of unique domains to return.

    Returns:
        list: List of unique finance news domains.
    """
    try:
        logger.info("Discovering top finance news sites")
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(f"https://www.bing.com/news/search?q={query}", headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.select('a[href^="http"]')
        domains = []

        for link in links:
            href = link.get('href')
            domain = urlparse(href).netloc
            if domain and "bing" not in domain and "microsoft" not in domain:
                domains.append(domain)

        unique_domains = list(dict.fromkeys(domains))
        logger.info(f"Discovered sites: {unique_domains[:max_sites]}")
        return unique_domains[:max_sites]
    except Exception as e:
        logger.error(f"Error discovering sites: {e}")
        return []
