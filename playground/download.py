import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://www.rapidtables.com"

#If there is no such folder, the script will create one automatically
folder_location = 'webscraping'
if not os.path.exists(folder_location): os.mkdir(folder_location)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):
   filename = os.path.join(folder_location, link['href'].split('/')[-1])
   with open(filename, 'wb') as f:
      f.write(requests.get(urljoin(url, link['href'])).content)

