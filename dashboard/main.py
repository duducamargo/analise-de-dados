import pandas as pd
import plotly.express as px

# Ler o arquivo CSV e converter 'event_time' para datetime
df = pd.read_csv('data.csv', parse_dates=['event_time'])

# Definir 'event_time' como índice
df.set_index('event_time', inplace=True)

# Agrupar e contar o número de eventos por dia para cada tipo de evento
df_resampled = df.groupby('event_type').resample('D').size().unstack(0).fillna(0)

# Resetar o índice
df_resampled = df_resampled.reset_index()

# Converter para formato longo
df_melted = df_resampled.melt(id_vars='event_time', value_vars=df_resampled.columns[1:], 
                              var_name='event_type', value_name='count')

# Criar o gráfico interativo
fig = px.line(df_melted, x='event_time', y='count', color='event_type',
              title='Número de eventos ao longo do tempo')

# Exibir o gráfico
fig.show()
