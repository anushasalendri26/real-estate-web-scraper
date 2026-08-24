# Real Estate Web Scraper

## Project Description

This project is a Python-based web scraper that extracts publicly available real estate property information from websites.

The scraper collects:

* Property Title
* Price
* Location

The extracted data is cleaned and exported into a CSV file.

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* CSV

## Features

* Scrapes public real estate property data
* Extracts property titles, prices, and locations
* Cleans unnecessary spaces and unwanted characters
* Exports the collected data into a CSV file
* Simple and easy to use

## Installation

Install the required Python libraries using:

```bash
pip install requests beautifulsoup4
```

## How to Run

Run the Python script using:

```bash
python scraper.py
```

After successful execution, the scraped data will be saved in:

```text
properties.csv
```

## Output

The CSV file contains the following columns:

| Property Title   | Price      | Location  |
| ---------------- | ---------- | --------- |
| Example Property | ₹45,00,000 | Hyderabad |

## Project Structure

```text
Real-Estate-Scraper/
│
├── scraper.py
├── properties.csv
├── README.md
└── requirements.txt
```

## Conclusion

This project demonstrates how Python can be used with Requests and BeautifulSoup4 to collect and organize publicly available real estate data and export it into a structured CSV file.
