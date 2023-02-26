import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

url = "https://www.theonion.com/breaking-news/news-in-photos"
while True:
    response = requests.get(url)

    data = response.text

    soup = BeautifulSoup(data, 'html.parser')

    div_elements = soup.find_all("div", {"class": "sc-11qwj9y-0 TCDpD"})
    
    data = [] # Create an empty list to store the scraped data

    for div in div_elements:
        a_elements = div.find_all("a")
        for picture in a_elements:
                    img_elements = picture.find_all("img")
                    for img in img_elements:
                        img_url = img['data-src'] # Extract the image URL
                        headline = img['alt']   # Extract the headline
                        data.append([headline, img_url]) # Append the data to the list
                        with open('theonion.csv', 'a', newline='',encoding="utf-8") as file:
                            writer = csv.writer(file)
                            # writer.writerow(['Headline', 'Image URL'])

                            writer.writerows(data)
    next_page = soup.select_one('a[rel="next"]')
    if next_page:
          next_url = next_page.get('href')
          url = urljoin(url, next_url) # Construct the absolute URL
    else:
          break
    # print(data)
print(url)
# with open('theonion.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Headline', 'Image URL'])
#     writer.writerows(data)
