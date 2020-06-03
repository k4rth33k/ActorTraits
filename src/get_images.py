import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json
import time
import os
import pandas as pd

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

headers = {"Ocp-Apim-Subscription-Key": 'INSERT_YOUR_KEY'}
# I've saved my free BING Search API key as an environment variable

params = {"q": "", "imageType": "photo", "count": "100"}

df = pd.DataFrame(columns=['image_link', 'actor'])

with open('names.txt', 'r') as fp:
    for ind, line in enumerate(fp):

        links = []
        actor_name = line[:-1]
        params["q"] = actor_name + ' actor'  # Hard choice, not misogyny!!

        print(f'Getting {actor_name}\'s photos')

        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        for i, val in enumerate(data['value'], start=1):
            links.append([val['contentUrl'], actor_name])

        df_ = pd.DataFrame(links, columns=['image_link', 'actor'])
        df = df.append(df_, ignore_index=True)

        time.sleep(1)
        # break

print(df.head())
df.to_csv('Actor Images.csv')
