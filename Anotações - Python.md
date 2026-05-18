**PYTHON**

O que é python? É uma linguagem de programação.

Sem muitas firulas, sempre ao objetivo! Aprender!

- O que é uma biblioteca?
  * É nada mais nada menos que uma espécie de kit pronto que já tem inúmeras coisas possíveis de serem usadas, funcionais, úteis.

Python sozinho:

```
 └─ Tem funções básicas (print, len, etc..)
```

Pandas (biblioteca):

```
 └─ Vem com ferramentas protnas para DADOS
 └─ Lê CSV, faz tabelas, calcula médias, etc.
```

NumPy (biblioteca):

```
 └─ Vem com ferramentas prontas para MATEMÁTICA
 └─ Faz contas complexas de forma rápida
```

Matplotlib (biblioteca):

```
 └─ Vem com ferramentas prontas para GRÁFICOS (perfumaria necessária kkk)
 └─ Desenha histograma, gráficos de linhas, etc.
```

Por que usar bibliotecas?

- Trabalho pesado já foi feito!
- Você não precisa perder tempo!
- Muito mais prático e rápido



***Como usar uma Biblioteca?***

Basicamente, você a importa. Como?

```
└─ import pandas
```

Isso significa: "Quero/Preciso usar a biblioteca nisto que estou desenvolvendo agora...". Para simplificar ainda mais damos um apelido:

```
└─ import pandas as pd
```

em outras palavras: "vou chamar o pandas de pd, pra agilizar o código e não escrever muito!". Depois disso, você pode pedir que o pandas (lembra das funções apresentadas? pois é!) leia um arquivo .csv por exemplo:

```
└─ df = pd.read_csv('arquivo.csv')
```

ou seja: "use a função read.csv da biblioteca pd (pandas)"

***DATAFRAME***

O que é um DataFrame? É uma tabela, jovem! Simplesmente isso! Uma **tabela**.

```
	Job_Title		Country		Salary_USD
0	Data Analyst	USA			120.000
1	ML Engineer		India		60.000
2	NLP Engineer	Canada		130.000
```

* Linhas (cada linha é uma pessoa/profissão)
* Colunas (cada coluna é uma informação: Job_Title, Country, Salary_USD)
* Índice (número da esquerda: 0, 1, 2, 3...)

 ``` 
 df = pd.read_csv('dados.csv')	# Lê o arquivo CSV e transforma em um DataFrame chamado df
 ```

***Como acessar dados em um DataFrame?***

Acessando uma coluna:

```
df['Salary_USD']
```

Isto retornará todos os salários como uma lista vertical:

```
0	120.000
1	60.000
2	110.000
3	130.000
```

Acessando várias colunas:

```
df[['Job_Title', 'Salary_USD']]
```

Isto retornará uma nova tabela com só estas duas colunas:

```
	Job_Title		Salary_USD
0	Data Analyst	120.000
1	ML Engineer		60.000
2	Data Scientist	110.000
```

Acessando UMA célula (uma linha + uma coluna):

```
df.loc[0, 'Salary_USD'] # Resultará no salário da primeira pessoa
120.000
```



***O que é uma FUNÇÃO?***

Uma função é uma AÇÃO que você pede ao computador para fazer.

```
df.mean()
```

count() é contagem

mean() é a função de cálculo de MÉDIA;

std() é o desvio-padrão

min()  mínimo valor

max() máximo valor

... Existem inúmeras funções. Abaixo, utilizei um DataFrame do projeto que estou desenvolvendo aqui neste repositório.

```
ESTATÍSTICAS DAS COLUNAS NUMÉRICAS:             

		 	Year     		Salary_USD 

count	2000.000000	    2000.000000 

mean	2023.970500  	94722.649000 

std		1.415497   		58925.012219 

min    	2022.000000    	8080.000000 

25%    	2023.000000   	44920.750000 

50%    	2024.000000  	77489.000000 

75%    	2025.000000  	143705.250000 

max    	2026.000000  	233977.000000


```



***Partes de uma função***

df.mean() 

|	  └─ Nome da função (mean = média) 
└──── Objeto que vai usar (df = nosso DataFrame)

***Funções com parâmetro***

df.head(10)

```
Mostra as 10 primeiras linhas do DataFrame
```

*head* é a função (mostrar início)

*10* é o parâmetro (quantas linhas)



**DIFERENÇA** entre .mean() e .mean

se eu uso df.mean() isto apenas **executa a função**

df.mean só aponta para a função, mas não executa.

OU SEJA, é necessário dos parênteses () para **executar** uma função.



**O que é um parâmetro?**

Parâmetro é uma CONFIGURAÇÃO que você passa para uma função.

```
plt.hist(data, bins=30)
```

data = o que você quer desenhar

bins=30 = parâmetro (quantas barras no histograma). Ou seja, se você alterasse para bins=10, seriam 10 barras ao invés de 30.



Agora para fixar, sem olhar em nada do material, responda:
```
O que é uma Biblioteca Python?
Como deve ser feito para acessar uma coluna?
O que é um DataFrame?
Qual a diferença entre df.mean() e df.mean?
O que é parâmetro?
```

Após responder, verifique se acertou! Caso contrário, volte e revise o material! Teve dúvida? Volte e revise o material!



*** ESTATÍSTICA x CÓDIGO***

Estatística

```
"Qual é a média dos salários?"
"Qual é o desvio padrão?"
"Qual lé a correlação entre X e Y?"
```

Código

```
df['Salary_USD'].mean()
df['Salary_USD'].std()
df['X'].corr(df['Y'])
```

O código é só a FERRAMENTA para calcular a estatística. Já a estatística é o **conceito**

Então, dicas:

* Aprender o conceito estatístico (ex: "o que é média?")
* Aprender porque é preciso? (ex:"porque calcular média?")
* Descobrir qual código deve ser usado ("ex: " .mean() calcula a média")
* **Escrever o código você mesmo!**



**AGRUPAMENTOS** - Analisando por categorias

> Você tem 1000 funcionários de vários países. Como saber "Qual é o salário médio por país?"
>
> * groupby
>
>   ```
>   df.groupby('Country')['Salary_USD'].mean()
>   ```
>
>   desmembrando:
>
>   * groupby('Country') - "separe os dados por país"
>
>     GRUPO USA:		[120000,	110000,	95000]
>
>     GRUPO Canada:	[80000,	90000]
>
>     GRUPO India:	[45000,	50000,	48000]
>
>   * ['Salary_USD'] - "De cada grupo, selecione a coluna salário"
>
>   * .mean() - "Calcule a média de cada grupo"
>
>     Resultado:
>
>     ```
>     Country
>     USA			108333.33
>     Canada		85000.00
>     India		47666.67
>     ```

​	Alguns outros exemplos úteis

* df.groupby('Country').size()				# Quantos funcionários por país?
* df.groupby('Country')['Salary_USD'].max()       # Qual o salário máximo por país?
* df.groupby('Country')['Salary_USD'].agg(['mean', 'max', 'min', 'count'])        #várias estatísticas 



**Porque o groupby é super interessante?**

Porque responde inúmeras perguntas que você vai se fazer ao montar um dashboard por exemplo.

1. Qual cargo paga melhor?
2. Em que país se ganha mais?
3. Quantas pessoas temos por área?

**FILTRO**

Filtro é um filtro. Não tem muito o que falar a respeito da definição. Contudo, há algumas formas de fazer um filtro e isso é importante, ter a forma com que estes filtros são feitos.

* **Filtro Simples**

  * Quero que liste somente quem ganha mais do que R$ 80.000.

    ```
    df[df['Salario'] > 80000]
    ```

​		E porque? Porque só a condição df['Salario'] > 80000 , retornaria uma lista de true/false, o que não é o que queremos! Então, como queremos os dados da tabela que preenchem a condição, utilizamos df[df['COLUNA'] condição]

* **Filtro Múltiplo**

  * Nada tão diferente, porém, **vale se atentar que as condições ficam dentro de ()**:

    ```
    Eu quero ver os funcionários de TI que ganham acima de 90.000
    
    df[
    (df['Departamento'] == 'TI') &
    (df['Salario'] > 90000)
    ]
    ```

    Neste caso, utilizamos & que implica em ambas as condições serem **TRUE**. Se fosse um **OU**, utilizaríamos uma **|** que resultaria em pelo menos uma condição verdadeira.

Então, pode estar se perguntando:

**QUANDO USAR GROUPBY / FILTRO?**

* **Use FILTRO quando:**

  * Você quer linhas específicas:

    * "Mostre só os managers;"

    * "Mostre só quem ganha acima de 80000;"

      

* **Use GROUPBY quando:**

  * Quando quiser calcular por CATEGORIA:
    * "Qual o salário médio por departamento?"
    * "Quantas pessoas há em cada cargo?"



**As funções mais utilizadas com o groupby:**

* mean()	#média
* std()             #desvio-padrão
* min()            #valor mínimo
* max()           #valor máximo
* size()            #quantidade de itens
* count()         #conta valores não-nulos (ignora NaN)
* sum()           #soma total
* median()     #mediana (valor do meio)
* nunique()    #quantos valores únicos
* first()            #primeiro valor do grupo
* last()             #último valor do grupo

​	agg()	    #várias estatísticas de uma única vez

```
df.groupby('Departamento')['Salario'].agg(['mean', 'max', 'min', 'count'])

              mean      max     min   count
Departamento                              
TI           96667   120000   75000     3
Vendas       87500   110000   65000     2
```

Resumindo:

O **GROUPBY** faz 2 coisas:

* Agrupa os dados por categoria
* Calcula alguma coisa para cada grupo



**MATPLOTLIB**

Agora, vamos começar com o que você enxerga! Porque de uma forma ou de outra, criar tabelas, é importante, porém, demonstrar os dados com gráficos é ***muito*** mais interessante e legível.

```
import matplotlib.pyplot as plt
```

Existem inúmeros tipos de gráficos! Vamos começar com o:

* Histograma

  * Como os salários são distribuídos? 

  * A maioria ganha muito ou pouco?

    * O histograma responde esse tipo de pergunta! Ele é perfeito porque mostra a frequência dos valores

    ```
    # Criando o histograma dos salários
    plt.hist(df['Salario'], bins=5)
    ```

    ​	'bins', é o número de "barras".

    ```
    # Adicionando títulos, para ficar profissional
    plt.title('Distribuição de Salários na Empresa')
    plt.xlabel('Faixa Salarial (USD)')
    plt.ylabel('Número de Funcionários')
    
    # Imprimindo o gráfico na tela
    plt.show()
    ```

    Em outras palavras, o Matplotlib pega todos os salários, divide em 5 "caixas" (bins) e conta quantos funcionários caem em cada caixa, desenhando uma barra para cada uma.

* Barras

  * Qual o salário médio por departamento?

    

    Vamos fazer isso aos poucos! Separadamente, para que fique bem compreendido.

    ```
    # 1º, pegamos os dados que queremos plotar!
    media_por_depto = df.groupby('Departamento')['Salario'].mean()
    
    # Neste caso, o resultado de 'media_por_depto' é:
    # Departamento
    # TI	96666.67
    # Vendas 87500.00
    ```

​		Depois, vamos desenhar o gráfico de barras com o Matplotlib

```
# Cria-se o gráfico de barras
# Eixo X: São os nomes dos departamentos (o índice)
# Eixo Y: Os valores das médias (os valores)
plt.bar(media_por_depto.index, media_por_depto.values, color='skyblue')

# Adiciona-se os títulos
plt.title('Salário Médio por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário Médio (USD)')

# Mostra o gráfico
plt.show()
```

Ou seja, o **Pandas**, prepara os dados! Já o **Matplotlib** desenha os gráficos.



import matplotlib.pyplot as plt



salario_max = df.groupby('Cargo')['Salario'].max()

plt.bar(salario_max.index, salario_max.values, color='skyblue')

plt.title('Salário Máximo por Cargo')
plt.xlabel('Salário Máximo')
plt.ylabel('Cargo')

plt.show()



___

Um exercício básico para treinar.
Utilizando o DataFrame:

import pandas as pd

import matplotlib.pyplot as plt

\# DataFrame com dados de vendas

df_vendas = pd.DataFrame({

​    'Vendedor': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fernando', 

​                 'Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fernando'],

​    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'Mouse',

​                'Teclado', 'Monitor', 'Mouse', 'Notebook', 'Teclado', 'Monitor'],

​    'Categoria': ['Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 

​                  'Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos',

​                  'Acessórios', 'Eletrônicos', 'Acessórios', 'Eletrônicos'],

​    'Valor_Venda': [2500, 50, 150, 800, 2200, 45, 120, 750, 55, 2800, 130, 820],

​    'Mes': ['Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar', 'Abr', 'Abr', 'Abr']

})

```
Qual o mês que mais vendeu? Construa o gráfico.
```

bargraph = df_vendas.groupby('Mes')['Valor_Venda'].sum()

plt.bar(bargraph.index, bargraph.values, color='black')

plt.title('Valor em R$')

plt.xlabel('Mês')

plt.ylabel('Quantidade')

plt.show()



![grafico](https://github.com/igortude/aprendendo-estatistica-ml/blob/main/assets/xx1.png)

Conseguimos verificar a disposição dos dados de forma correta, até porque o DataFrame utilizado está limpo! Ou seja, não está bagunçado (sujo), o que facilita demais! E no final das contas, é o que precisa ser feito, sempre que se começar a trabalhar com um DataFrame. 

**Analisar e Padronizar!**



Agora, vamos para um DataFrame bagunçado (SUJO).

```
import pandas as pd
import numpy as np

# Simulando dados bagunçados de verdade
dados_sujos = pd.DataFrame({
    'nome': ['João Silva', 'maria santos', 'PEDRO COSTA', 'Ana Oliveira', 'joão silva', 
             'Maria Santos', '', 'Carlos Lima', 'ana oliveira', 'Pedro Costa'],
    'departamento': ['TI', 'vendas', 'TI', 'RH', 'ti', 'Vendas', 'Marketing', 'TI', 'rh', ''],
    'salario': ['5000', '3500', 'R$ 7000', '4200', '5000', '3500', '', '6000', '4200', '7000'],
    'idade': [25, 30, '', 28, 25, 30, 22, 35, 28, 45],
    'email': ['joao@empresa.com', 'maria@empresa.com', 'pedro@empresa.com', '', 
              'joao@empresa.com', 'maria2@empresa.com', 'carlos@empresa.com', 
              'carlos@empresa.com', 'ana@empresa.com', 'pedro@empresa.com']
})

print("DADOS ORIGINAIS (BAGUNÇADOS):")
print(dados_sujos)
```

O que é que se consegue identificar ?

Nomes, maiúsculas, minúsculas, valores vazios, repetição de dados, etc... 

Ou seja, é interessante verificar tudo isso! E como podemos começar ?

```
dados_sujos.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   nome          10 non-null     object
 1   departamento  10 non-null     object
 2   salario       10 non-null     object
 3   idade         10 non-null     object
 4   email         10 non-null     object
dtypes: object(5)
memory usage: 532.0+ bytes
```

e também:

```
dados_sujos.describe()

		nome	departamento	salario	idade	email
count	10				10			10		10		10
unique	10				8			7		7		7
top		João Silva		TI			5000	25		joao@empresa.com
freq	1				3			2		2		2

```

Ou seja, há muita bagunça, certo? 

Agora, execute:

```
print("=== INFORMAÇÕES GERAIS ===")
dados_sujos.info()

print("\n=== VALORES ÚNICOS POR COLUNA ===")
for coluna in dados_sujos.columns:
    print(f"{coluna}: {dados_sujos[coluna].nunique()} valores únicos")
    
print("\n=== VERIFICANDO NULOS ===")
print(dados_sujos.isnull().sum())

print("\n=== PRIMEIRAS 5 LINHAS ===")
print(dados_sujos.head())

=== INFORMAÇÕES GERAIS ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   nome          10 non-null     object
 1   departamento  10 non-null     object
 2   salario       10 non-null     object
 3   idade         10 non-null     object
 4   email         10 non-null     object
dtypes: object(5)
memory usage: 532.0+ bytes

=== VALORES ÚNICOS POR COLUNA ===
nome: 10 valores únicos
departamento: 8 valores únicos
salario: 7 valores únicos
idade: 7 valores únicos
email: 7 valores únicos

=== VERIFICANDO NULOS ===
nome            0
departamento    0
salario         0
idade           0
email           0
dtype: int64

=== PRIMEIRAS 5 LINHAS ===
           nome departamento  salario idade              email
0    João Silva           TI     5000    25   joao@empresa.com
1  maria santos       vendas     3500    30  maria@empresa.com
2   PEDRO COSTA           TI  R$ 7000        pedro@empresa.com
3  Ana Oliveira           RH     4200    28                   
4    joão silva           ti     5000    25   joao@empresa.com
```

Olhe que **beleza**... Vamos começar a arrumar tudo!

Até porque, se temos 10 linhas no dataset e há pessoas repetidas, deveria ter menos de 10 valores únicos em algumas colunas.

```
# Vamos investigar os nomes únicos
print("NOMES 'ÚNICOS' SEGUNDO O PANDAS:")
print(dados_sujos['nome'].unique())

NOMES 'ÚNICOS' SEGUNDO O PANDAS:
['João Silva' 'maria santos' 'PEDRO COSTA' 'Ana Oliveira' 'joão silva'
 'Maria Santos' '' 'Carlos Lima' 'ana oliveira' 'Pedro Costa']
```

O Pandas considera 'João Silva' e 'joão silva', duas pessoas diferentes; 

```A mesma coisa acontece com o Departamento, 'TI' e 'ti'
print("DEPARTAMENTOS 'ÚNICOS':")
print(dados_sujos['departamento'].unique())
```

A mesma coisa acontece com o Departamento, 'TI' e 'ti'

Na verdade, são só 4 departamentos, mas por causa da 'não padronização', o Pandas, enxerga como diferentes.

Quando se percebe valores únicos demais, **dados inconsistentes**. Quando se vê valores únicos de menos, há possíveis **duplicatas**.

```
# CHECKLIST INICIAL - Limpeza de DADOS
```

**Passo 1: Padronização do Texto**

* ***Problema***: Maiúsculas, Minúsculas bagunçadas
* **SOLUÇÃO**: .str do Pandas

Vamos explorar um pouco essa nova função:

```
# .str.lower() = tudo minúsculo
dados_sujos['nome'].str.lower()

# .str.upper() = tudo maiúsculo
dados_sujos['nome'].str.upper()

# .str.title() = Primeiras Letras Maiúsculas
dados_sujos['nome'].str.title()

# .str.strip() = remove espaços das pontas
dados_sujos['nome'].str.strip()
```

Agora verifique:

```
dados_sujos['nome'].str.title()

#NOMES TRATADOS
nome
0	João Silva
1	Maria Santos
2	Pedro Costa
3	Ana Oliveira
4	João Silva
5	Maria Santos
6	
7	Carlos Lima
8	Ana Oliveira
9	Pedro Costa

dtype: object
```

E aí, você deve estar se perguntando... E como eu salvo isso? É simples!

basta adicionar 'dados_sujos['nome'] ='

```
dados_sujos['nome'] = dados_sujos['nome'].str.title()
```

Sem o 'dados_sujos['nome'] =' Servirá somente para a sua visualização.

logo, se você aplica o mesmo para a coluna de departamentos, tudo começa a ficar mais claro e possível de análise.

então, vamos lá!

```
dados_sujos['nome'] = dados_sujos['nome'].str.title()
dados_sujos['departamento'] = dados_sujos['departamento'].str.upper()

print(dados_sujos)

           nome departamento  salario idade               email
0    João Silva           TI     5000    25    joao@empresa.com
1  Maria Santos       VENDAS     3500    30   maria@empresa.com
2   Pedro Costa           TI  R$ 7000         pedro@empresa.com
3  Ana Oliveira           RH     4200    28                    
4    João Silva           TI     5000    25    joao@empresa.com
5  Maria Santos       VENDAS     3500    30  maria2@empresa.com
6                  MARKETING             22  carlos@empresa.com
7   Carlos Lima           TI     6000    35  carlos@empresa.com
8  Ana Oliveira           RH     4200    28     ana@empresa.com
9   Pedro Costa                  7000    45   pedro@empresa.com
```

e para verificação:

``` 
print("\n=== VALORES ÚNICOS POR COLUNA ===")
for coluna in dados_sujos.columns:
	print(f"{coluna}: {dados_sujos[coluna].nunique()} valore únicos")
	
=== VALORES ÚNICOS POR COLUNA ===
nome: 6 valores únicos
departamento: 5 valores únicos
salario: 7 valores únicos
idade: 7 valores únicos
email: 7 valores únicos
```

O Pandas já conseguiu identificar as mudanças. E agora, passamos para a **conversão de texto para número** (inteiro)

**PASSO 2: CONVERSÃO DE TEXTO EM NÚMERO**

***PROBLEMA***: Os salários não estão com valores padronizados (R$ 5000, 7000..)

**SOLUÇÃO**: Remover os caracteres e converter o tipo

```
# .str.replace() = substitui um texto por outro
dados_sujos['salario'].str.replace('R$ ', '')

# .str.replace() com regex para remover qualquer caractere não-numérico
dados_sujos['salario'].str.replace('[^0-9]', '', regex=True)

# pd.to_numeric() = converte para número
pd.to_numeric(dados_sujos['salario'])
```

Vamos primeiro investigar!

```
print("SALÁRIOS ORIGINAIS:")
print(dados_sujos['salario'])
print("Tipo da coluna:", dados_sujos['salario'].dtype)

print("\nAPÓS REMOVER 'R$ ':")
print(dados_sujos['salario'].str.replace('R$ ', ''))
```

```
Salários
0       5000
1       3500
2    R$ 7000
3       4200
4       5000
5       3500
6           
7       6000
8       4200
9       7000
Name: salario, dtype: object
Tipo da coluna: object

Após Remoção: 
salario
0	5000
1	3500
2	7000
3	4200
4	5000
5	3500
6	
7	6000
8	4200
9	7000

dtype: object
```

Tudo excelente agora! Só é necessário lembrar de salvar a substituição:

```
dados_sujos['salario'] = dados_sujos['salario'].str.replace('R$ ', '')
```

