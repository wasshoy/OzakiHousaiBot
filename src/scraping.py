import requests
import bs4


URL = 'https://www.aozora.gr.jp/cards/000195/files/974_318.html'
response = requests.get(URL)
response.encoding = response.apparent_encoding
soup = bs4.BeautifulSoup(response.text, 'html.parser')

for tag in soup(['head', 'a', 'b', 'br', 'hr']):
    tag.decompose()

with open('../data/interim/aozora-ozaki.txt', 'w') as f:
    f.write(soup.get_text())
