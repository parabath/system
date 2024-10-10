import requests
from bs4 import BeautifulSoup

url = ''
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extracting all the links from the page
for link in soup.find_all('a'):
    print(link.get('href'))
