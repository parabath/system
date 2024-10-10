import urllib.request

# URL of the page you want to read
url = 'https://www.hirunews.lk/'

# Open the URL and read the HTML content
response = urllib.request.urlopen(url)
html = response.read()

# Print the HTML content
print(html.decode('utf-8'))
