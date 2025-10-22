"""
Simple example demonstrating how to use the Ticket Analyzer in your own code
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analyzer import TicketAnalyzer


def main():
    # Initialize the analyzer
    analyzer = TicketAnalyzer()
    
    # Example 1: Analyze a single ticket
    print("=" * 60)
    print("Example 1: Single Ticket Analysis")
    print("=" * 60)
    
    ticket = "URGENT: Cannot login to my account! This is critical!"
    result = analyzer.analyze_ticket(ticket)
    
    print(f"\nTicket: {ticket}")
    print(f"Sentiment: {result['sentiment']['sentiment']}")
    print(f"Urgency: {result['urgency']['urgency_level']}")
    print(f"Category: {result['category']['category']}")
    print(f"Recommendation: {result['priority_recommendation']}")
    
    # Example 2: Batch analysis
    print("\n\n" + "=" * 60)
    print("Example 2: Batch Analysis")
    print("=" * 60)
    
    tickets = [
        "How do I reset my password?",
        "The system crashed - EMERGENCY!",
        "I was charged twice for my subscription"
    ]
    
    results = analyzer.analyze_batch(tickets)
    
    for i, (ticket, result) in enumerate(zip(tickets, results), 1):
        print(f"\n{i}. {ticket}")
        print(f"   → {result['urgency']['urgency_level']} urgency | "
              f"{result['category']['category']} category")
    
    # Example 3: Filter critical tickets
    print("\n\n" + "=" * 60)
    print("Example 3: Filter Critical Tickets")
    print("=" * 60)
    
    critical_tickets = [result for result in results 
                       if result['urgency']['urgency_level'] in ['critical', 'high']]
    
    print(f"\nFound {len(critical_tickets)} critical/high priority ticket(s)")
    for ticket in critical_tickets:
        print(f"  • {ticket['ticket_text']}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
