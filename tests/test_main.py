"""
Tests for the main module
"""

import os
import sys
import unittest
from unittest.mock import patch

# Add parent directory to path to import main module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import deduplicate_articles

class TestMain(unittest.TestCase):
    """Test cases for the main module"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create sample articles with duplicates
        self.articles_with_duplicates = [
            {"title": "Article 1", "link": "https://example.com/article1"},
            {"title": "Article 2", "link": "https://example.com/article2"},
            {"title": "Article 1 (Updated)", "link": "https://example.com/article1"},  # Duplicate link
            {"title": "Article 3", "link": "https://example.com/article3"},
            {"title": "Article 2", "link": "https://example.com/article2"}  # Duplicate link
        ]
    
    def test_deduplicate_articles(self):
        """Test deduplication of articles"""
        # Deduplicate the articles
        unique_articles = deduplicate_articles(self.articles_with_duplicates)
        
        # Check that duplicates are removed
        self.assertEqual(len(unique_articles), 3)
        
        # Check that the first occurrence of each link is kept
        expected_links = ["https://example.com/article1", 
                         "https://example.com/article2", 
                         "https://example.com/article3"]
        
        actual_links = [article['link'] for article in unique_articles]
        self.assertEqual(actual_links, expected_links)

if __name__ == '__main__':
    unittest.main()
