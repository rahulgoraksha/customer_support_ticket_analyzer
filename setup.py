"""
Setup configuration for the Customer Support Ticket Analyzer
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="customer-support-ticket-analyzer",
    version="1.0.0",
    author="Rahul Goraksha",
    description="A machine learning-based project for analyzing and categorizing customer support tickets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahulgoraksha/custome_support_ticket_analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="nlp machine-learning support-tickets sentiment-analysis text-classification",
    project_urls={
        "Bug Reports": "https://github.com/rahulgoraksha/custome_support_ticket_analyzer/issues",
        "Source": "https://github.com/rahulgoraksha/custome_support_ticket_analyzer",
    },
)
