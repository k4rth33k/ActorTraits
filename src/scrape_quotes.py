"""
Author: Kartheek Surampudi (k4rth33k)
This file is for scraping the quotes of actors/actresses

"""

from bs4 import BeautifulSoup
import pandas as pd
import requests

df = pd.DataFrame(columns=['Actor', 'Quotes'])

with open('names.txt', 'r') as fp:
    for actor_link in fp:
        
        actor_link = actor_link.strip('\n')
        actor, link = actor_link.split('--')
        
        actor = actor.strip()
        link = link.strip()

        print(f'Scraping {actor}\'s quotes')

        url = f'https://www.brainyquote.com{link}'

        html = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")

        quotes = []
        
        for a_tag in soup.find_all('a', class_='b-qt'):
            
            if len(quotes) == 10:
                break
            
            quotes.append(a_tag.string)

        _ = pd.DataFrame([[actor, ''.join(quote for quote in quotes)]], columns=['Actor', 'Quotes'])
        df = df.append(_, ignore_index=True)

        # break

df.to_csv('Actor quotes.csv')