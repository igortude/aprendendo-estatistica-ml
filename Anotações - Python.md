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