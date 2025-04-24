# site_discovery.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

# Define known reliable finance news domains
VALID_FINANCE_DOMAINS = {
    "finance.yahoo.com",
    "www.cnbc.com",
    "www.marketwatch.com",
    "www.bloomberg.com",
    "www.reuters.com",
    "www.investing.com",
    "www.ft.com",
    "www.wsj.com",
}

def discover_top_finance_sites(query="finance news", max_sites=3):
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
            # Only include if it's one of the known good domains
            if domain in VALID_FINANCE_DOMAINS and domain not in domains:
                domains.append(domain)

        logger.info(f"Discovered sites: {domains[:max_sites]}")
        return domains[:max_sites]

    except Exception as e:
        logger.error(f"Error discovering sites: {e}")
        return []
