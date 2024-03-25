import pandas as pd
import numpy as np

df = pd.read_csv('text.csv')

text = []
labels = []
for row in df.iterrows():
    text.append(row['text'])
    labels.append(row['labels'])