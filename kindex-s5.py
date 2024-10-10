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
    with open('C:\\Users\\wppsk\\Desktop\\karuna\\kindexo.html', 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()
        f = open("C:\\Users\\wppsk\\Desktop\\karuna\\kindexo.html", "r")
        print(f.read())
else:
    print(f"Failed to retrieve the file. Status code: {response.status_code}")





