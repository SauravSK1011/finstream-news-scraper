"""
FinStream Main Module

This is the main entry point for the FinStream application.
It orchestrates the scraping, filtering, and posting processes.
"""

import logging
from scraper import get_financial_news
from wordpress_poster import post_multiple_articles

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def deduplicate_articles(articles):
    """
    Remove duplicate articles based on their URLs.
    
    Args:
        articles (list): List of article dictionaries with 'title' and 'link'
        
    Returns:
        list: Deduplicated list of articles
    """
    unique_articles = []
    seen_links = set()
    
    for article in articles:
        link = article['link']
        if link not in seen_links:
            unique_articles.append(article)
            seen_links.add(link)
    
    logger.info(f"Deduplicated from {len(articles)} to {len(unique_articles)} articles")
    return unique_articles

def main():
    """
    Main function to run the FinStream application.
    """
    logger.info("Starting FinStream news scraper")
    
    # Get financial news articles
    articles = get_financial_news()
    logger.info(f"Found {len(articles)} articles matching keywords")
    
    # Deduplicate articles
    unique_articles = deduplicate_articles(articles)
    
    # Prepare posts for WordPress
    if unique_articles:
        successful_posts = post_multiple_articles(unique_articles)
        logger.info(f"Successfully prepared {successful_posts} posts for WordPress")
        
        # Print summary
        print(f"\nSummary: Found {len(articles)} new articles, prepared {successful_posts} posts.")
    else:
        logger.info("No articles found matching the criteria")
        print("\nSummary: No articles found matching the criteria.")

if __name__ == "__main__":
    main()
