import requests

# URL of the text file
url = 'https://ideakidmart.blogspot.com/2024/02/ant-documento.html'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Read the content of the file
    content = response.text
    print(content)
else:
    print(f"Failed to retrieve the file. Status code: {response.status_code}")
