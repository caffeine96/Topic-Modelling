import pandas as pd
import gensim
import numpy as np
#Importing preprocessing function from preprocess py file
from preprocess import preprocess

#Read CSV data, lines with too many commas are not returned
data = pd.read_csv('abcnews-date-text.csv',error_bad_lines=False)
headlines = data[['headline_text']] 
headlines['index'] = headlines.index
documents = headlines   # Created a dataframe with headlines and index number

#Headlines parsed for preprocessing
processed_docs = documents['headline_text'].map(preprocess)
print processed_docs[:10]