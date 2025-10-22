"""
Unit tests for the Ticket Analyzer
"""

import unittest
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from analyzer import TicketAnalyzer


class TestTicketAnalyzer(unittest.TestCase):
    """Test cases for TicketAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = TicketAnalyzer()
    
    def test_preprocess_text(self):
        """Test text preprocessing."""
        text = "URGENT: Cannot Login!!!"
        result = self.analyzer.preprocess_text(text)
        self.assertEqual(result, "urgent cannot login!!!")
    
    def test_sentiment_positive(self):
        """Test positive sentiment detection."""
        text = "Thank you for the excellent service! Everything works great."
        result = self.analyzer.analyze_sentiment(text)
        self.assertEqual(result['sentiment'], 'positive')
        self.assertGreater(result['polarity'], 0)
    
    def test_sentiment_negative(self):
        """Test negative sentiment detection."""
        text = "This is terrible! Nothing works and I'm very upset."
        result = self.analyzer.analyze_sentiment(text)
        self.assertEqual(result['sentiment'], 'negative')
        self.assertLess(result['polarity'], 0)
    
    def test_sentiment_neutral(self):
        """Test neutral sentiment detection."""
        text = "I need to reset my password."
        result = self.analyzer.analyze_sentiment(text)
        self.assertEqual(result['sentiment'], 'neutral')
    
    def test_urgency_critical(self):
        """Test critical urgency detection."""
        text = "URGENT! System crashed and not working. This is a critical emergency!"
        result = self.analyzer.detect_urgency(text)
        self.assertIn(result['urgency_level'], ['critical', 'high'])
        self.assertGreater(result['urgent_keywords_found'], 0)
    
    def test_urgency_low(self):
        """Test low urgency detection."""
        text = "I have a question about your product features."
        result = self.analyzer.detect_urgency(text)
        self.assertEqual(result['urgency_level'], 'low')
    
    def test_category_technical(self):
        """Test technical category classification."""
        text = "Getting error code 500 when accessing the database. System crash."
        result = self.analyzer.classify_category(text)
        self.assertEqual(result['category'], 'technical')
        self.assertGreater(result['confidence'], 0)
    
    def test_category_billing(self):
        """Test billing category classification."""
        text = "I was charged twice for my subscription. Need a refund on my invoice."
        result = self.analyzer.classify_category(text)
        self.assertEqual(result['category'], 'billing')
    
    def test_category_account(self):
        """Test account category classification."""
        text = "Cannot login to my account. Forgot my password and username."
        result = self.analyzer.classify_category(text)
        self.assertEqual(result['category'], 'account')
    
    def test_category_feature_request(self):
        """Test feature request category classification."""
        text = "Would like to request a new feature. Can you add export functionality?"
        result = self.analyzer.classify_category(text)
        self.assertEqual(result['category'], 'feature_request')
    
    def test_analyze_ticket_complete(self):
        """Test complete ticket analysis."""
        text = "URGENT: Payment system is down and customers cannot checkout!"
        result = self.analyzer.analyze_ticket(text)
        
        self.assertIn('sentiment', result)
        self.assertIn('urgency', result)
        self.assertIn('category', result)
        self.assertIn('priority_recommendation', result)
        
        # Should be negative sentiment
        self.assertEqual(result['sentiment']['sentiment'], 'negative')
        
        # Should be high/critical urgency
        self.assertIn(result['urgency']['urgency_level'], ['high', 'critical'])
    
    def test_analyze_empty_ticket(self):
        """Test handling of empty ticket."""
        result = self.analyzer.analyze_ticket("")
        self.assertIn('error', result)
    
    def test_analyze_batch(self):
        """Test batch analysis of multiple tickets."""
        tickets = [
            "Technical issue with login",
            "Request for refund",
            "How do I change my settings?"
        ]
        results = self.analyzer.analyze_batch(tickets)
        
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertIn('sentiment', result)
            self.assertIn('urgency', result)
            self.assertIn('category', result)
    
    def test_priority_recommendation(self):
        """Test priority recommendation generation."""
        # Critical urgency
        rec = self.analyzer._get_priority_recommendation('critical', 'negative')
        self.assertIn('Immediate', rec)
        
        # High urgency with negative sentiment
        rec = self.analyzer._get_priority_recommendation('high', 'negative')
        self.assertIn('1 hour', rec)
        
        # Low urgency
        rec = self.analyzer._get_priority_recommendation('low', 'neutral')
        self.assertIn('24 hours', rec)


if __name__ == '__main__':
    unittest.main()
