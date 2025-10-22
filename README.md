# Customer Support Ticket Analyzer

A machine learning–based project designed to analyze and categorize customer support tickets for faster resolution and better customer experience. This tool leverages Natural Language Processing (NLP) techniques to automatically detect ticket sentiment, urgency, and category, helping support teams prioritize issues efficiently.

## Features

- **Sentiment Analysis**: Detects whether a ticket has positive, negative, or neutral sentiment
- **Urgency Detection**: Automatically identifies critical, high, medium, or low urgency tickets based on keywords and sentiment
- **Category Classification**: Classifies tickets into categories (Technical, Billing, Account, Feature Request, General Inquiry)
- **Priority Recommendations**: Provides actionable priority recommendations for support teams
- **Batch Processing**: Analyze multiple tickets simultaneously

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rahulgoraksha/custome_support_ticket_analyzer.git
cd custome_support_ticket_analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

Run the main script to analyze sample tickets:

```bash
python main.py
```

This will analyze 10 sample support tickets and display detailed results including sentiment, urgency, category, and priority recommendations.

### Using the Analyzer in Your Code

```python
from src.analyzer import TicketAnalyzer

# Initialize the analyzer
analyzer = TicketAnalyzer()

# Analyze a single ticket
ticket_text = "URGENT: Cannot login to my account!"
result = analyzer.analyze_ticket(ticket_text)

print(f"Sentiment: {result['sentiment']['sentiment']}")
print(f"Urgency: {result['urgency']['urgency_level']}")
print(f"Category: {result['category']['category']}")
print(f"Priority: {result['priority_recommendation']}")

# Analyze multiple tickets
tickets = [
    "Payment failed during checkout",
    "How do I reset my password?",
    "System is down - emergency!"
]
results = analyzer.analyze_batch(tickets)
```

## Project Structure

```
custome_support_ticket_analyzer/
├── src/
│   ├── __init__.py
│   └── analyzer/
│       ├── __init__.py
│       └── ticket_analyzer.py    # Core analyzer module
├── data/
│   ├── __init__.py
│   └── sample_tickets.py          # Sample tickets for testing
├── tests/
│   ├── __init__.py
│   └── test_ticket_analyzer.py    # Unit tests
├── main.py                         # Demo script
├── requirements.txt                # Project dependencies
└── README.md                       # This file
```

## How It Works

### Sentiment Analysis
Uses TextBlob to analyze the sentiment polarity of ticket text:
- **Positive**: Polarity > 0.1 (e.g., "Thank you for the great service!")
- **Negative**: Polarity < -0.1 (e.g., "This is terrible and not working")
- **Neutral**: Polarity between -0.1 and 0.1 (e.g., "How do I reset my password?")

### Urgency Detection
Analyzes tickets using:
- Urgent keywords (urgent, critical, emergency, broken, crashed, etc.)
- Sentiment analysis (negative sentiment increases urgency)
- Scoring system to classify as critical, high, medium, or low urgency

### Category Classification
Uses keyword matching to classify tickets into:
- **Technical**: Errors, bugs, system issues
- **Billing**: Payments, invoices, refunds
- **Account**: Login, password, access issues
- **Feature Request**: New features, suggestions, improvements
- **General Inquiry**: Questions, how-to, information requests

## Testing

Run the unit tests:

```bash
python -m unittest discover tests
```

Or run a specific test:

```bash
python -m unittest tests.test_ticket_analyzer
```

## Example Output

```
TICKET #1
--------------------------------------------------------------------------------
Text: URGENT: My account is locked and I cannot access the system. This is cri...

SENTIMENT ANALYSIS:
  • Sentiment: NEGATIVE
  • Polarity: -0.35 (range: -1 to 1)
  • Subjectivity: 0.6 (range: 0 to 1)

URGENCY DETECTION:
  • Urgency Level: CRITICAL
  • Urgency Score: 40
  • Urgent Keywords Found: 2

CATEGORY CLASSIFICATION:
  • Primary Category: ACCOUNT
  • Confidence: 2
  • Category Scores: {'technical': 0, 'billing': 0, 'account': 2, ...}

PRIORITY RECOMMENDATION:
  • Immediate attention required - escalate to senior support
```

## Dependencies

- `nltk==3.8.1` - Natural Language Toolkit for text processing
- `scikit-learn==1.3.2` - Machine learning library
- `numpy==1.26.2` - Numerical computing
- `pandas==2.1.3` - Data manipulation
- `textblob==0.17.1` - Simplified text processing and sentiment analysis

## Future Enhancements

- Integration with ML models trained on actual support ticket data
- Multi-language support
- Custom category definitions
- Real-time ticket monitoring dashboard
- Integration with ticketing systems (Zendesk, Jira, etc.)
- Advanced NLP models (BERT, transformers)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Rahul Goraksha
