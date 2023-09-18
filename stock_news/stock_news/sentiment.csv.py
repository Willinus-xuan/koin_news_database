from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
import torch

df = pd.read_csv('./stock_news/news_content.csv')

t = df[df.news_content.isin([np.nan])]

# tokenizer initialization
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")

# pretrianed model from finbert
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

# tokenize input

inputs = tokenizer(df['news_content'], padding=True, truncation=True, return_tensors='pt')

# inference
outputs = model(**inputs)

# Postprocessing with softmax
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Model classes
model.config.id2label

