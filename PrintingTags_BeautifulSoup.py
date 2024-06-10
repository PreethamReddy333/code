import urllib.request, urllib parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter web page link:')

#Retrieving html content from the url entered by user
htmlcontent = urllib.request.urlopen(url).read()

#creating beautiful soup object for passing html content
soup = BeautifulSoup(htmlcontent, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get("href", None)
