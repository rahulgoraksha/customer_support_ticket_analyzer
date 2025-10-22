"""
Ticket Analyzer Module
Performs sentiment analysis, urgency detection, and category classification
on customer support tickets using NLP techniques.
"""

import re
from typing import Dict, List, Tuple
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class TicketAnalyzer:
    """
    A machine learning-based analyzer for customer support tickets.
    Detects sentiment, urgency, and category of tickets.
    """
    
    # Keywords for urgency detection
    URGENT_KEYWORDS = [
        'urgent', 'asap', 'immediately', 'critical', 'emergency',
        'broken', 'not working', 'down', 'crashed', 'error',
        'cannot', "can't", 'unable', 'failed', 'failure'
    ]
    
    # Keywords for category detection
    CATEGORY_KEYWORDS = {
        'technical': [
            'error', 'bug', 'crash', 'not working', 'broken',
            'issue', 'problem', 'technical', 'code', 'system',
            'software', 'hardware', 'database', 'server'
        ],
        'billing': [
            'payment', 'invoice', 'charge', 'billing', 'refund',
            'subscription', 'price', 'cost', 'fee', 'credit card',
            'transaction', 'paid', 'money'
        ],
        'account': [
            'login', 'password', 'account', 'access', 'sign in',
            'username', 'credential', 'authentication', 'profile',
            'settings', 'email', 'verification'
        ],
        'feature_request': [
            'feature', 'request', 'suggestion', 'improvement',
            'enhancement', 'would like', 'wish', 'could you add',
            'new functionality', 'upgrade'
        ],
        'general_inquiry': [
            'how to', 'how do i', 'question', 'inquiry', 'help',
            'information', 'guide', 'tutorial', 'explain', 'clarify'
        ]
    }
    
    def __init__(self):
        """Initialize the ticket analyzer and download required NLTK data."""
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess the ticket text by converting to lowercase and cleaning.
        
        Args:
            text: Raw ticket text
            
        Returns:
            Preprocessed text
        """
        # Convert to lowercase
        text = text.lower()
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s\.\!\?]', ' ', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def analyze_sentiment(self, text: str) -> Dict[str, any]:
        """
        Analyze the sentiment of the ticket using TextBlob.
        
        Args:
            text: Ticket text
            
        Returns:
            Dictionary containing sentiment analysis results
        """
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Classify sentiment
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3)
        }
    
    def detect_urgency(self, text: str) -> Dict[str, any]:
        """
        Detect the urgency level of the ticket based on keywords and sentiment.
        
        Args:
            text: Ticket text
            
        Returns:
            Dictionary containing urgency detection results
        """
        preprocessed_text = self.preprocess_text(text)
        
        # Count urgent keywords
        urgent_count = sum(1 for keyword in self.URGENT_KEYWORDS 
                          if keyword in preprocessed_text)
        
        # Calculate urgency score
        sentiment_result = self.analyze_sentiment(text)
        
        # Higher urgency if negative sentiment and urgent keywords present
        urgency_score = urgent_count * 10
        if sentiment_result['sentiment'] == 'negative':
            urgency_score += 20
        
        # Classify urgency level
        if urgency_score >= 30:
            urgency_level = 'critical'
        elif urgency_score >= 15:
            urgency_level = 'high'
        elif urgency_score >= 5:
            urgency_level = 'medium'
        else:
            urgency_level = 'low'
        
        return {
            'urgency_level': urgency_level,
            'urgency_score': urgency_score,
            'urgent_keywords_found': urgent_count
        }
    
    def classify_category(self, text: str) -> Dict[str, any]:
        """
        Classify the ticket into a category based on keyword matching.
        
        Args:
            text: Ticket text
            
        Returns:
            Dictionary containing category classification results
        """
        preprocessed_text = self.preprocess_text(text)
        
        # Count keywords for each category
        category_scores = {}
        for category, keywords in self.CATEGORY_KEYWORDS.items():
            score = sum(1 for keyword in keywords 
                       if keyword in preprocessed_text)
            category_scores[category] = score
        
        # Find the category with highest score
        if max(category_scores.values()) > 0:
            primary_category = max(category_scores, key=category_scores.get)
            confidence = category_scores[primary_category]
        else:
            primary_category = 'general_inquiry'
            confidence = 0
        
        return {
            'category': primary_category,
            'confidence': confidence,
            'category_scores': category_scores
        }
    
    def analyze_ticket(self, ticket_text: str) -> Dict[str, any]:
        """
        Perform complete analysis of a support ticket.
        
        Args:
            ticket_text: The text content of the support ticket
            
        Returns:
            Dictionary containing all analysis results
        """
        if not ticket_text or not ticket_text.strip():
            return {
                'error': 'Empty ticket text provided'
            }
        
        sentiment_result = self.analyze_sentiment(ticket_text)
        urgency_result = self.detect_urgency(ticket_text)
        category_result = self.classify_category(ticket_text)
        
        return {
            'ticket_text': ticket_text[:100] + '...' if len(ticket_text) > 100 else ticket_text,
            'sentiment': sentiment_result,
            'urgency': urgency_result,
            'category': category_result,
            'priority_recommendation': self._get_priority_recommendation(
                urgency_result['urgency_level'],
                sentiment_result['sentiment']
            )
        }
    
    def _get_priority_recommendation(self, urgency: str, sentiment: str) -> str:
        """
        Generate a priority recommendation based on urgency and sentiment.
        
        Args:
            urgency: Urgency level
            sentiment: Sentiment classification
            
        Returns:
            Priority recommendation string
        """
        if urgency == 'critical':
            return 'Immediate attention required - escalate to senior support'
        elif urgency == 'high' and sentiment == 'negative':
            return 'High priority - respond within 1 hour'
        elif urgency == 'high':
            return 'High priority - respond within 2 hours'
        elif urgency == 'medium':
            return 'Medium priority - respond within 4 hours'
        else:
            return 'Low priority - respond within 24 hours'
    
    def analyze_batch(self, tickets: List[str]) -> List[Dict[str, any]]:
        """
        Analyze multiple tickets at once.
        
        Args:
            tickets: List of ticket texts
            
        Returns:
            List of analysis results for each ticket
        """
        return [self.analyze_ticket(ticket) for ticket in tickets]
