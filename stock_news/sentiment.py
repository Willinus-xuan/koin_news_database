from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
import torch

df = pd.read_csv('./stock_news/news_url.csv')

titles = df['title'].tolist()

# tokenizer initialization
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")

# pretrianed model from finbert
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

from itertools import islice
nums = len(df)//200
length_to_split = [len(df)%200]
[length_to_split.append(200) for _ in range(nums)]

titles = iter(titles)
titles = [list(islice(titles, elem))
        for elem in length_to_split]

df_output = pd.DataFrame()
# tokenize input
for subset in titles:
    inputs = tokenizer(subset, padding=True, truncation=True, return_tensors='pt')
# inference
    outputs = model(**inputs)
# Postprocessing with softmax
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    positive = predictions[:, 0].tolist()
    negative = predictions[:, 1].tolist()
    neutral = predictions[:, 2].tolist()
    table = dict({'title':subset,
                  'pos':positive,
                  'neg':negative,
                  'neu':neutral})
    df_temp = pd.DataFrame(table,columns=['title','pos','neg','neu'])
    df_output = pd.concat([df_output,df_temp])


df_output['label'] = np.array(df_output[['pos','neg','neu']]).argmax(axis=1)






# Model classes
model.config.id2label


