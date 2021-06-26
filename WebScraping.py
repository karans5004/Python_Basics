# import required modules
from bs4 import BeautifulSoup
import requests
  
# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
  
htmlContent = page.content

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#get title of page
title = soup.title

#get all paragraphs
paras = soup.find_all('p')
print(soup.get_text())