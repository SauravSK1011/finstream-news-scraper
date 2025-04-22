"""
Tests for the wordpress_poster module
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import json

# Add parent directory to path to import wordpress_poster module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wordpress_poster import post_to_wp, post_multiple_articles

class TestWordPressPoster(unittest.TestCase):
    """Test cases for the wordpress_poster module"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_title = "Test Article Title"
        self.test_link = "https://example.com/test-article"
        self.test_content = "<p>This is test content</p>"
    
    @patch('builtins.print')
    def test_post_to_wp(self, mock_print):
        """Test post_to_wp function"""
        # Call the function
        result = post_to_wp(self.test_title, self.test_link)
        
        # Check that the function returns True
        self.assertTrue(result)
        
        # Check that print was called with the expected arguments
        mock_print.assert_any_call(f"\nPrepared WordPress post:")
        mock_print.assert_any_call(f"Title: {self.test_title}")
        mock_print.assert_any_call(f"Link: {self.test_link}")
    
    @patch('wordpress_poster.post_to_wp')
    def test_post_multiple_articles(self, mock_post_to_wp):
        """Test post_multiple_articles function"""
        # Set up the mock
        mock_post_to_wp.return_value = True
        
        # Create test articles
        test_articles = [
            {"title": "Article 1", "link": "https://example.com/article1"},
            {"title": "Article 2", "link": "https://example.com/article2"},
            {"title": "Article 3", "link": "https://example.com/article3"}
        ]
        
        # Call the function
        result = post_multiple_articles(test_articles)
        
        # Check that post_to_wp was called for each article
        self.assertEqual(mock_post_to_wp.call_count, len(test_articles))
        
        # Check that the function returns the correct number of successful posts
        self.assertEqual(result, len(test_articles))
        
        # Check that post_to_wp was called with the correct arguments
        for article in test_articles:
            mock_post_to_wp.assert_any_call(article['title'], article['link'])

if __name__ == '__main__':
    unittest.main()
