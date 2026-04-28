**PANDAS**

Pandas é uma biblioteca do Python e foi criada para trabalhar com datasets e tabelas, permitindo que se faça operações elementares como manipulação de dados, filtros, agrupamentos e muito mais.

*Dataframes*: é uma estrutura de dados bidimensional composta por linhas (índices) e colunas (nós). Você pode pensar em um DataFrame como uma tabela do Excel ou uma planilha de dados.

*Séries*: É uma sequência ordenada de valores, semelhante a uma lista. E são úteis para trabalhar com dados temporais ou categóricos.

**Operações Básicas**

Algumas das mais comuns operações básicas que se pode fazer com Pandas:

* df.head(): mostra as primeiras linhas do DataFrame
* df.tail(): mostra as últimas linhas do DataFrame
* df.info(): Fornece informações sobre o tamanho, tipos de dados e memória utilizada pelo DataFrame.
* df.descibe(): Gera um relatório de estatísticas descritivas para as colunas numéricas.

Vamos começar criando algo simples. Um dataframe chamado *students* com os seguintes dados:

import pandas as pd

data = {

'Nome' : ['João', 'Maria', 'Pedro'],

'Idade' : [20, 25, 30],

'Nota': [8, 9, 10]

}

df = pd.DataFrame(data)

print(df)



Isso gerará um DataFrame com as seguintes colunas:

![image-20260428183351973](/home/igor/.var/app/io.typora.Typora/config/Typora/typora-user-images/image-20260428183351973.png)

Valendo a ressalva de que é possível também, criar com uma lista, ao invés de um dicionário. No exemplo anterior, o dicionário ***data*** é composto por chaves Nome, Idade, Nota, cada uma com uma lista de valores correspondentes.

Isso é conhecido como "pandas do dict" ou "dict to dataframe".

Mas é possível também, criar um DataFrame apartir de uma lista. Por exemplo:


import pandas as pd

lista = [
    ['João', 20, 8],
    ['Maria', 25, 9],
    ['Pedro', 30, 10]
]

df = pd.DataFrame(lista, columns=['Nome','Idade','Nota'])
print(df)

