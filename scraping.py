import requests
from bs4 import BeautifulSoup 

url = "https://qiita.com/Octoparse_Japan/items/3a766a5615d82674b873"
response = requests.get(url)
html = response.text

# print(response.status_code)
# print(response.text[:500])

soup = BeautifulSoup(html, "html.parser")
title = soup.find("h1").text
