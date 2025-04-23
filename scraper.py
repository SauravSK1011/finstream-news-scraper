"""
FinStream News Scraper

This module handles fetching and filtering financial news articles from various sources.
"""

import requests
from bs4 import BeautifulSoup
import logging
from site_discovery import discover_top_finance_sites

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Keywords to filter headlines by
KEYWORDS = [
    "stock", "market", "invest", "trading", "nasdaq", "dow", "s&p", "finance", "Trump", "Gold", "Crude Oil", "Business", "BSE", "NSE", "Nifty", "Sensex",
    "economy", "fed", "interest rate", "inflation", "earnings", "dividend"
]

def fetch_articles(url):
    """
    Fetch articles from a given URL.
    
    Args:
        url (str): The URL to fetch articles from
        
    Returns:
        list: A list of dictionaries containing article title and link
    """
    articles = []
    
    try:
        logger.info(f"Fetching articles from {url}")
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }, timeout=10)
        
        if response.status_code != 200:
            logger.error(f"Failed to fetch {url}: Status code {response.status_code}")
            return articles
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for headlines in common HTML patterns
        # This is a simplified approach and might need adjustment for specific sites
        headlines = soup.find_all(['h1', 'h2', 'h3', 'a'], class_=lambda c: c and any(x in str(c).lower() for x in ['headline', 'title', 'story', 'article']))
        
        for headline in headlines:
            title = headline.get_text().strip()
            
            # Get the link - either from the headline itself if it's an <a> tag
            # or from a child <a> tag
            if headline.name == 'a':
                link = headline.get('href', '')
            else:
                link_tag = headline.find('a')
                link = link_tag.get('href', '') if link_tag else ''
            
            # Handle relative URLs
            if link and link.startswith('/'):
                # Extract domain from the source URL
                from urllib.parse import urlparse
                parsed_url = urlparse(url)
                base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                link = base_url + link
            
            if title and link:
                articles.append({
                    'title': title,
                    'link': link
                })
        
        logger.info(f"Found {len(articles)} articles from {url}")
        
    except Exception as e:
        logger.error(f"Error fetching articles from {url}: {str(e)}")
    
    return articles

def filter_by_keywords(articles, keywords=None):
    """
    Filter articles by keywords in their titles.
    
    Args:
        articles (list): List of article dictionaries with 'title' and 'link'
        keywords (list, optional): List of keywords to filter by. Defaults to KEYWORDS.
        
    Returns:
        list: Filtered list of articles
    """
    if keywords is None:
        keywords = KEYWORDS
    
    filtered_articles = []
    
    for article in articles:
        title = article['title'].lower()
        if any(keyword.lower() in title for keyword in keywords):
            filtered_articles.append(article)
    
    logger.info(f"Filtered down to {len(filtered_articles)} articles containing keywords")
    return filtered_articles

def get_financial_news():
    """
    Fetch and filter financial news from discovered sources.
    """
    discovered_domains = discover_top_finance_sites()
    if not discovered_domains:
        logger.warning("Falling back to default sources.")
        discovered_domains = [
            "finance.yahoo.com",
            "www.cnbc.com",
            "www.marketwatch.com",
            "www.bloomberg.com",
            "www.reuters.com",
            "www.investing.com"
        ]
        
    all_articles = []

    for domain in discovered_domains:
        url = f"https://{domain}"
        articles = fetch_articles(url)
        all_articles.extend(articles)

    return filter_by_keywords(all_articles)

if __name__ == "__main__":
    # Test the scraper
    articles = get_financial_news()
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print("-" * 50)
