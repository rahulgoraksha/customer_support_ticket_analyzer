# Contributing to Customer Support Ticket Analyzer

Thank you for your interest in contributing to the Customer Support Ticket Analyzer! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/custome_support_ticket_analyzer.git
   cd custome_support_ticket_analyzer
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure they follow the project's coding style

3. Run the tests to make sure everything works:
   ```bash
   python -m unittest discover tests
   ```

4. Commit your changes with a descriptive commit message:
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request from your fork to the main repository

## Running Tests

Run all tests:
```bash
python -m unittest discover tests -v
```

Run a specific test file:
```bash
python -m unittest tests.test_ticket_analyzer
```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise
- Add comments for complex logic

## Adding New Features

When adding new features:

1. **Add tests**: Write unit tests for your new functionality
2. **Update documentation**: Update the README.md if needed
3. **Add examples**: If applicable, add usage examples
4. **Maintain backward compatibility**: Don't break existing functionality

## Reporting Bugs

If you find a bug, please create an issue with:

- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Python version and OS
- Any relevant error messages

## Suggesting Enhancements

For feature requests:

- Explain the use case clearly
- Describe the expected behavior
- Provide examples if possible

## Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Write clear commit messages
- Update tests as needed
- Ensure all tests pass
- Update documentation
- Respond to review feedback promptly

## Project Structure

```
custome_support_ticket_analyzer/
├── src/
│   └── analyzer/          # Core analyzer modules
├── tests/                 # Unit tests
├── data/                  # Sample data and datasets
├── main.py               # Demo script
├── example.py            # Usage examples
└── README.md             # Project documentation
```

## Questions?

If you have questions, feel free to:
- Open an issue for discussion
- Contact the maintainers

Thank you for contributing!
