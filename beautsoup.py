import requests
from bs4 import BeautifulSoup
import json

page= requests.get("https://getlatka.com/")
print(page.text)

soup= BeautifulSoup(page.content,'html.parser')
print(soup)

script= soup.find('script').text.strip()
data = json.loads(script)
print(data)
