import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

def get_quotes():
    """Scrapes quotes and authors from the website."""
    response = requests.get(URL)
    response.raise_for_status()  # Raise an error if the request failed

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    results = []

    for quote, author in zip(quotes, authors):
        results.append({
            "quote": quote.get_text(strip=True),
            "author": author.get_text(strip=True)
        })

    return results  

def main():
    print("Scraping quotes...")

    quotes = get_quotes()

    for item in quotes:
        print(f'"{item["quote"]}" — {item["author"]}')

    print(f"\nTotal quotes found: {len(quotes)}")


if __name__ == "__main__":
    main()
