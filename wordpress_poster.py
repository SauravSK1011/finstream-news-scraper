"""
FinStream WordPress Poster

This module handles preparing and posting content to WordPress via the REST API.
For now, it's stubbed to just print the payload instead of making actual API calls.
"""

import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# WordPress API credentials from environment variables
WP_SITE = os.getenv('WP_SITE')
WP_USER = os.getenv('WP_USER')
WP_APP_PASS = os.getenv('WP_APP_PASS')

def post_to_wp(title, link, content=None):
    """
    Prepare a post for WordPress (stubbed version).
    
    Args:
        title (str): The title of the post
        link (str): The link to the original article
        content (str, optional): Additional content for the post. Defaults to None.
        
    Returns:
        bool: True if the post preparation was successful
    """
    # Create a timestamp for the post
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # If no content is provided, create a simple one with the link
    if not content:
        content = f'<p>Check out this financial news article: <a href="{link}" target="_blank">{title}</a></p>'
        content += f'<p>Source: <a href="{link}" target="_blank">{link}</a></p>'
    
    # Prepare the payload as WordPress REST API would expect
    payload = {
        "title": title,
        "content": content,
        "status": "draft",  # Set as draft by default
        "format": "standard",
        "date": timestamp,
        "meta": {
            "original_source": link
        }
    }
    
    # In a real implementation, this would make an API call to WordPress
    # For now, just print the payload
    logger.info(f"Prepared WordPress post: {title}")
    logger.debug(f"Post payload: {json.dumps(payload, indent=2)}")
    
    print(f"\nPrepared WordPress post:")
    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Status: draft")
    print(f"Payload structure: {json.dumps(payload, indent=2)}")
    
    return True

def post_multiple_articles(articles):
    """
    Prepare multiple articles for posting to WordPress.
    
    Args:
        articles (list): List of article dictionaries with 'title' and 'link'
        
    Returns:
        int: Number of successfully prepared posts
    """
    successful_posts = 0
    
    for article in articles:
        title = article['title']
        link = article['link']
        
        if post_to_wp(title, link):
            successful_posts += 1
    
    return successful_posts

if __name__ == "__main__":
    # Test the WordPress poster
    test_articles = [
        {"title": "Stock Market Hits New High", "link": "https://example.com/article1"},
        {"title": "Fed Announces Interest Rate Decision", "link": "https://example.com/article2"}
    ]
    
    post_multiple_articles(test_articles)
