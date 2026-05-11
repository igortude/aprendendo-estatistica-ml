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

O GROUPBY faz 2 coisas:

* Agrupa os dados por categoria
* Calcula alguma coisa para cada grupo