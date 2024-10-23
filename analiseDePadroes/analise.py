import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# Caminho dos arquivos CSV (ajuste conforme necessário)
caminho_arquivos = 'caminho/para/arquivos/'
arquivos = glob.glob(caminho_arquivos + "*.csv")

# Carregar e combinar todos os arquivos
dados = pd.concat([pd.read_csv(f) for f in arquivos], ignore_index=True)

# Convertendo 'event_time' para datetime
dados['event_time'] = pd.to_datetime(dados['event_time'])

# Visualizando uma amostra dos dados
print(dados.head())

plt.figure(figsize=(8, 6))
sns.countplot(data=dados, x='event_type', palette='viridis')
plt.title('Número de Eventos por Tipo')
plt.show()

# Agrupando por data e tipo de evento
eventos_por_data = dados.groupby([dados['event_time'].dt.date, 'event_type']).size().reset_index(name='count')

plt.figure(figsize=(10, 6))
sns.lineplot(data=eventos_por_data, x='event_time', y='count', hue='event_type', marker='o')
plt.title('Evolução dos Eventos ao Longo do Tempo')
plt.xticks(rotation=45)
plt.show()

# Produtos mais adicionados ao carrinho
cart_produtos = dados[dados['event_type'] == 'cart']['product_id'].value_counts().head(10)

plt.figure(figsize=(8, 6))
sns.barplot(x=cart_produtos.values, y=cart_produtos.index, palette='Blues_r')
plt.title('Top 10 Produtos Mais Adicionados ao Carrinho')
plt.show()

# Produtos mais comprados
compras = dados[dados['event_type'] == 'purchase']

# Contar a quantidade de compras por produto
contagem_compras = compras['product_id'].value_counts()

# Filtrar produtos com quantidade maior que 3141
produtos_filtrados = contagem_compras[contagem_compras > 3141].head(10)

# Visualizar os 10 principais produtos
plt.figure(figsize=(10, 6))
sns.barplot(x=produtos_filtrados.values, y=produtos_filtrados.index, palette='Greens_r')
plt.title('Top 10 Produtos Mais Comprados (Quantidade > 3141)')
plt.xlabel('Quantidade Comprada')
plt.ylabel('ID do Produto')
plt.show()

# Número de eventos por tipo (cart e purchase)
cart_count = dados[dados['event_type'] == 'cart'].shape[0]
purchase_count = dados[dados['event_type'] == 'purchase'].shape[0]

conversao = (purchase_count / cart_count) * 100
print(f'Taxa de conversão de carrinho para compra: {conversao:.2f}%')

# Filtrando apenas eventos de compra e calculando preço médio por categoria
preco_categoria = dados[dados['event_type'] == 'purchase'].groupby('category_code')['price'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=preco_categoria, x='price', y='category_code', palette='coolwarm')
plt.title('Preço Médio por Categoria')
plt.show()

# Sessões com mais compras
compras_sessoes = dados[dados['event_type'] == 'purchase']['user_session'].value_counts().head(10)

plt.figure(figsize=(8, 6))
sns.barplot(x=compras_sessoes.values, y=compras_sessoes.index, palette='Purples_r')
plt.title('Top 10 Sessões com Mais Compras')
plt.show()
