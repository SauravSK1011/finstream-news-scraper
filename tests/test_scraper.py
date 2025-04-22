"""
Tests for the scraper module
"""

import os
import sys
import unittest
from bs4 import BeautifulSoup

# Add parent directory to path to import scraper module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import filter_by_keywords

class TestScraper(unittest.TestCase):
    """Test cases for the scraper module"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Load the sample HTML file
        with open(os.path.join(os.path.dirname(__file__), 'sample_finance_page.html'), 'r') as f:
            self.sample_html = f.read()
        
        # Parse the HTML
        self.soup = BeautifulSoup(self.sample_html, 'html.parser')
        
        # Extract articles from the sample HTML
        self.sample_articles = []
        headlines = self.soup.find_all('h2', class_='headline')
        
        for headline in headlines:
            link_tag = headline.find('a')
            if link_tag:
                title = link_tag.get_text().strip()
                link = link_tag.get('href', '')
                self.sample_articles.append({
                    'title': title,
                    'link': link
                })
    
    def test_filter_by_keywords(self):
        """Test filtering articles by keywords"""
        # Define test keywords
        keywords = ['stock', 'interest rate', 'inflation']
        
        # Filter the sample articles
        filtered_articles = filter_by_keywords(self.sample_articles, keywords)
        
        # Check that only articles with keywords are included
        self.assertEqual(len(filtered_articles), 3)
        
        # Check that each filtered article contains at least one keyword
        for article in filtered_articles:
            title = article['title'].lower()
            self.assertTrue(any(keyword.lower() in title for keyword in keywords))
        
        # Check that articles without keywords are excluded
        excluded_titles = ['Major Tech Company Reports Strong Earnings', 
                          'New Restaurant Chain Opening Locations Nationwide']
        
        for article in filtered_articles:
            self.assertNotIn(article['title'], excluded_titles)

if __name__ == '__main__':
    unittest.main()
