import requests
from bs4 import BeautifulSoup
# URL of the Wikipedia page to scrape
url = 'https://en.wikipedia.org/wiki/Web_scraping'
# Send a GET request to the URL
response = requests.get(url)
# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, 'html.parser')
# Find the main content element
content_element = soup.find(id='content')
# Find the title of the Wikipedia page
title = content_element.find(id='firstHeading').text
# Find the introduction paragraph of the Wikipedia page
intro_paragraph = content_element.find('p').text
# Print the title and introduction paragraph
print('Title:', title)
print('Introduction Paragraph:', intro_paragraph)

## Task1: Try to scrap data from cbit website
## Task2: Try to scrap average rating from amazon.in
##for a product name given by user













