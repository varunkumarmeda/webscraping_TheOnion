import requests
from bs4 import BeautifulSoup

url = "https://www.theonion.com/breaking-news/news-in-photos"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

div_elements = soup.find_all("div", {"class": "sc-11qwj9y-0 TCDpD"})

for div in div_elements:
    a_elements = div.find_all("a")
    for picture in a_elements:
                img_elements = picture.find_all("img")
                for img in img_elements:
                    print(img['data-src'])