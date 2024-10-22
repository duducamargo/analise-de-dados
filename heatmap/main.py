import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

files = ['C:\\Users\\edufa\\analise-de-dados\\2019-Oct.csv', 
         'C:\\Users\\edufa\\analise-de-dados\\2019-Nov.csv', 
         'C:\\Users\\edufa\\analise-de-dados\\2019-Dec.csv', 
         'C:\\Users\\edufa\\analise-de-dados\\2020-Jan.csv',
         'C:\\Users\\edufa\\analise-de-dados\\2020-Feb.csv']

dfs = []

for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

print(combined_df.head())
