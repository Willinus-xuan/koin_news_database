from keyphrasetransformer import KeyPhraseTransformer
import pandas as pd
import os
import numpy as np
df = pd.read_csv('./stock_news/news_content.csv')
kp = KeyPhraseTransformer()

output_list = []
for doc in df['news_content'].iloc[[0,50,200]]:
    phrases = kp.get_key_phrases(doc)
    output_list.append(phrases)

output_list[2]
