import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # Send a GET request to the website
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information (quotes and authors) from the page
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            quotes.append({'text': text, 'author': author})

        return quotes
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
        return None

if __name__ == "__main__":
    # Run the web scraping function
    scraped_quotes = scrape_quotes()

    # Display the results
    if scraped_quotes:
        print("Scraped Quotes:")
        for index, quote in enumerate(scraped_quotes, start=1):
            print(f"{index}. {quote['text']} - {quote['author']}")
    else:
        print("Web scraping failed.")
