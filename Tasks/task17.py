# Decode A Web Page 2

import requests
from  bs4 import BeautifulSoup
# ptinyt in beautiful format 
from pprint import pprint


url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
pprint(soup.get_text())
