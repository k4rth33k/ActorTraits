"""
Author: Kartheek Surampudi (k4rth33k)
This file is for scraping the names of top 200 Indian Actors/Actresses

"""
# python scrape_names.py > names.txt

from bs4 import BeautifulSoup
import requests


url_1 = 'https://www.brainyquote.com/category/indian_actor'  # Actors Page
url_2 = 'https://www.brainyquote.com/category/indian_actress'  # Actresses Page

for url in [url_1, url_2]:

    html = requests.get(url).content.decode('utf-8')

    soup = BeautifulSoup(html, "html.parser")

    for td_tag in soup.find_all('td'):
        a_s = td_tag.find_all('a', href=True)
        if len(a_s) != 0:
            elem = a_s.pop()
            print(elem.string, '--', elem['href'])
