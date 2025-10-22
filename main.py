"""
Main script to demonstrate the Customer Support Ticket Analyzer
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analyzer import TicketAnalyzer
from data.sample_tickets import SAMPLE_TICKETS


def print_separator():
    """Print a visual separator."""
    print("\n" + "=" * 80 + "\n")


def print_analysis_result(ticket_id: int, analysis: dict):
    """
    Pretty print the analysis result.
    
    Args:
        ticket_id: ID of the ticket
        analysis: Analysis result dictionary
    """
    print(f"TICKET #{ticket_id}")
    print("-" * 80)
    print(f"Text: {analysis['ticket_text']}")
    print()
    
    # Sentiment
    print("SENTIMENT ANALYSIS:")
    sentiment = analysis['sentiment']
    print(f"  • Sentiment: {sentiment['sentiment'].upper()}")
    print(f"  • Polarity: {sentiment['polarity']} (range: -1 to 1)")
    print(f"  • Subjectivity: {sentiment['subjectivity']} (range: 0 to 1)")
    print()
    
    # Urgency
    print("URGENCY DETECTION:")
    urgency = analysis['urgency']
    print(f"  • Urgency Level: {urgency['urgency_level'].upper()}")
    print(f"  • Urgency Score: {urgency['urgency_score']}")
    print(f"  • Urgent Keywords Found: {urgency['urgent_keywords_found']}")
    print()
    
    # Category
    print("CATEGORY CLASSIFICATION:")
    category = analysis['category']
    print(f"  • Primary Category: {category['category'].upper()}")
    print(f"  • Confidence: {category['confidence']}")
    print(f"  • Category Scores: {category['category_scores']}")
    print()
    
    # Priority Recommendation
    print("PRIORITY RECOMMENDATION:")
    print(f"  • {analysis['priority_recommendation']}")
    print()


def main():
    """Main function to run the ticket analyzer."""
    print_separator()
    print("CUSTOMER SUPPORT TICKET ANALYZER")
    print("Powered by Natural Language Processing (NLP)")
    print_separator()
    
    # Initialize the analyzer
    print("Initializing Ticket Analyzer...")
    analyzer = TicketAnalyzer()
    print("✓ Analyzer initialized successfully!")
    print_separator()
    
    # Analyze sample tickets
    print(f"Analyzing {len(SAMPLE_TICKETS)} sample tickets...")
    print_separator()
    
    for ticket in SAMPLE_TICKETS:
        result = analyzer.analyze_ticket(ticket['text'])
        print_analysis_result(ticket['id'], result)
        print_separator()
    
    # Summary statistics
    print("SUMMARY STATISTICS")
    print("-" * 80)
    
    all_results = [analyzer.analyze_ticket(t['text']) for t in SAMPLE_TICKETS]
    
    # Count by urgency
    urgency_counts = {}
    for result in all_results:
        urgency = result['urgency']['urgency_level']
        urgency_counts[urgency] = urgency_counts.get(urgency, 0) + 1
    
    print("\nTickets by Urgency Level:")
    for level, count in sorted(urgency_counts.items(), 
                               key=lambda x: ['low', 'medium', 'high', 'critical'].index(x[0])):
        print(f"  • {level.upper()}: {count}")
    
    # Count by sentiment
    sentiment_counts = {}
    for result in all_results:
        sentiment = result['sentiment']['sentiment']
        sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
    
    print("\nTickets by Sentiment:")
    for sentiment, count in sorted(sentiment_counts.items()):
        print(f"  • {sentiment.upper()}: {count}")
    
    # Count by category
    category_counts = {}
    for result in all_results:
        category = result['category']['category']
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print("\nTickets by Category:")
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {category.upper()}: {count}")
    
    print_separator()
    print("Analysis complete! ✓")
    print_separator()


if __name__ == "__main__":
    main()
