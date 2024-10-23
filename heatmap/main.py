import os
import glob
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho dinâmico para os arquivos CSV (independente do sistema operacional)
data_dir = os.path.join(os.getcwd(), 'analise-de-dados')  # Ajusta conforme a pasta onde seus arquivos estão
csv_files = glob.glob(os.path.join(data_dir, '../*.csv'))  # Busca todos os arquivos .csv na pasta

# Carregar e concatenar todos os arquivos CSV
combined_df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# Convertendo a coluna 'event_time' para datetime
combined_df['event_time'] = pd.to_datetime(combined_df['event_time'])

# Extraindo dia da semana e hora
combined_df['day_of_week'] = combined_df['event_time'].dt.day_name()
combined_df['hour'] = combined_df['event_time'].dt.hour

# Criando a tabela para o heatmap
heatmap_data = combined_df.pivot_table(index='day_of_week', columns='hour', aggfunc='size', fill_value=0)

# Ordem dos dias da semana
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data.reindex(days_order)

# Plot do heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=False)
plt.title('Volume de Compras ao Longo do Tempo (Dias da Semana vs Horas do Dia)')
plt.ylabel('Dia da Semana')
plt.xlabel('Hora do Dia')
plt.show()
