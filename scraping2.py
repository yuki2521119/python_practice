import requests
from bs4 import BeautifulSoup 

url = "https://www.python.org"
response = requests.get(url)
html = response.text

print(response.status_code)
print(response.text[:500])

soup = BeautifulSoup(html, "html.parser")
num = 0
result = soup.find_all("h2")[num]

print(result)