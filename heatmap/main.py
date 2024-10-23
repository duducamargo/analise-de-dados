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

combined_df['event_time'] = pd.to_datetime(combined_df['event_time'])

combined_df['day_of_week'] = combined_df['event_time'].dt.day_name()  
combined_df['hour'] = combined_df['event_time'].dt.hour  

heatmap_data = combined_df.pivot_table(index='day_of_week', columns='hour', aggfunc='size', fill_value=0)

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data.reindex(days_order)

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=False)  
plt.title('Volume de Compras ao Longo do Tempo (Dias da Semana vs Horas do Dia)')
plt.ylabel('Dia da Semana')
plt.xlabel('Hora do Dia')
plt.show()
