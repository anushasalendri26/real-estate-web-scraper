import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    properties = []

    # Find property information
    property_cards = soup.find_all("div", class_="property-card")

    for card in property_cards:

        title = card.find("h2")
        price = card.find("span", class_="price")
        location = card.find("span", class_="location")

        title = title.get_text(strip=True) if title else "N/A"
        price = price.get_text(strip=True) if price else "N/A"
        location = location.get_text(strip=True) if location else "N/A"

        properties.append([title, price, location])

    # Create CSV file
    with open("properties.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Property Title", "Price", "Location"])

        writer.writerows(properties)

    print("Scraping completed successfully!")
    print("Data saved to properties.csv")

else:
    print("Failed to access website")
