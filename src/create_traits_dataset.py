'''
Author: Kartheek Surampudi (k4rth33k)
This file is for creating a dataset to train the model.
For the information on the model, check README.md

'''
import pandas as pd
import numpy as np
import re

def make_df(csv, drop, text_col, _=True):
    print(f'Adding {csv} Dataset...')

    df = pd.read_csv(f'./data/{csv}.csv', engine='python')

    df.drop(drop, axis=1, inplace=True)

    clean_texts = []

    for i, row in df.iterrows():
        text = row[text_col]
        text = re.sub(r' ?\([^)]+\)', '', text)
        text = re.sub(r' ?\[[^\]]+\]', '', text)
        text = re.sub(r'speaker\d', '', text)
        text = text.strip()

        clean_texts.append(text)
        # break

    df['text'] = clean_texts
    df.drop([text_col], axis=1, inplace=True)

    traits = ['cAGR', 'cCON', 'cEXT', 'cOPN', 'cNEU']
    for trait in traits:
        if _:
            df[trait] = df[trait].values.astype('int')
        else:
            df[trait] = np.where(df[trait].values == 'y', 1, 0)

    return df


df1 = make_df(csv='friends', drop=['characters', 'raw_text', 'scene_id', 'single_text', 'full', 'Unnamed: 0'],
             text_col='single_context')

df2 = make_df(csv='essays', drop=['#AUTHID'], text_col='TEXT', _=False)

df = pd.concat([df1, df2])

df.to_csv('./data/data.csv')