# Climate Project Awards Data Analysis

This repository contains Python scripts for extracting and analyzing SBIR awards data.

## Installation

1. Clone this repository.
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment:
    - On Windows: `.\env\Scripts\activate`
    - On macOS and Linux: `source env/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Download the spaCy language model: `python -m spacy download en_core_web_sm`

## Running the Scripts

1. Run `api_data_fetcher.py` to fetch data from the SBIR API and save it to a CSV file.
2. Run `web_scraper.py` to scrape data from the ARPA-E website. [Does not currently work]
3. Run `NLP_model.py` to analyze the abstracts from the SBIR awards data and save the word frequencies, noun chunk frequencies, and n-gram frequencies to CSV files.
4. Run `phrase_clustering.py` to cluster the abstracts from the SBIR awards data and save the clusters to a CSV file.


## Requirements

- Python 3.6 or higher
- `requests`
- `beautifulsoup4`
- `pandas`
- `spacy`
- `en_core_web_sm`
- `scikit-learn`
