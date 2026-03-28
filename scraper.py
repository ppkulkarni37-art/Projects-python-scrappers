import requests
from bs4 import BeautifulSoup

# The website we're going to scrape
url = "https://news.ycombinator.com"

# Visit the website and download its HTML
response = requests.get(url)

# Parse the HTML so we can search through it
soup = BeautifulSoup(response.text, "html.parser")

# Find all the headlines
headlines = soup.find_all("span", class_="titleline")

# Print each headline
for i, headline in enumerate(headlines, start=1):
    title = headline.get_text()
    link = headline.find("a")["href"] if headline.find("a") else "no link"
    print(f"{i}. {title}")
    print(f"   {link}\n")