# **E-commerce Cosmetics - Análise de Comportamento do Cliente**

Este projeto tem como objetivo analisar o comportamento de compra dos clientes em uma loja de cosméticos online, utilizando dados de eventos capturados durante 5 meses. A análise permitirá identificar padrões de compra e fornecer insights para otimização de campanhas de marketing digital.

## **Informações do Banco de Dados**

O banco de dados contém uma vasta lista de eventos que ocorreram ao longo de cinco meses em uma loja de cosméticos. Cada linha no dataset representa um evento específico relacionado a um produto e um usuário.

A seguir, um exemplo de como os eventos estão estruturados:
> _"Usuário **user_id** durante uma sessão **user_session** adicionou ao carrinho (se **event_type == cart**) o produto **product_id** da marca **brand** da categoria **category_code** com o preço **price** no momento **event_time**."_

## **Estrutura do Banco de Dados**

| Propriedade   | Descrição                                                                 |
|---------------|---------------------------------------------------------------------------|
| `event_time`  | Data e hora em que o evento ocorreu                                       |
| `event_type`  | Tipo de evento (tipos detalhados abaixo)                                  |
| `product_id`  | ID do produto relacionado ao evento                                       |
| `category_id` | ID da categoria associada ao `product_id`                                 |
| `category_code`| Taxonomia ou nome da categoria do produto, quando disponível             |
| `brand`       | Nome da marca do produto em letras minúsculas                             |
| `price`       | Preço do produto em formato float                                         |
| `user_id`     | ID único do usuário                                                       |
| `user_session`| ID da sessão temporária do usuário, que muda a cada nova sessão           |

## **Tipos de Eventos**

Os eventos no dataset estão classificados nos seguintes tipos:

- **`view`**: O usuário visualizou um produto.
- **`cart`**: O usuário adicionou um produto ao carrinho.
- **`remove_from_cart`**: O usuário removeu um produto do carrinho.
- **`purchase`**: O usuário comprou um produto.

## **Observações Importantes**

- Uma única sessão (**user_session**) pode conter múltiplos eventos de compra (**purchase**), mas ainda será considerada como uma única ordem.
- Nem todas as categorias de produtos possuem um código definido (**category_code**), especialmente em categorias mais genéricas.

## **Objetivo do Projeto**

- **Limpeza e Transformação de Dados**: Realizar o processamento dos dados utilizando bibliotecas como pandas, tratando valores ausentes e padronizando as colunas para facilitar as análises.
- **Análise de Padrões de Compra**: Usar bibliotecas como matplotlib e seaborn para identificar padrões de comportamento dos usuários.
- **Dashboard Interativo**: Criar visualizações interativas com plotly para facilitar a exploração dos dados, como número de cliques, visualizações e compras ao longo do tempo.
- **Heatmap de Tempo**: Utilizar seaborn para construir um heatmap que mostre o volume de compras ao longo dos dias da semana e horas do dia.