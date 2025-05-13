# Decode A Web Page

import requests
from  bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
# find all p tags from url
for title in soup.findAll('p'):
#  extracting all the text from a page
 print(title.get_text())
