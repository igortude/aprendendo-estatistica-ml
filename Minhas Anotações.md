**TIPOS DE VARIÁVEIS**

Basicamente existem 4 tipos de variáveis.

- **Qualitativas**:
  - *Nominal*: Categorias sem ordem natural - EX: gênero, cor, cidade
  - *Ordinal*: Categorias com ordem natural - nível de ensino, satisfação...
- **Quantitativas **(números)
  * *Discreta*: Valores de contagem
    * Número de cliques, quantidade de produtos em um carrinho..
  * *Contínua*: Valores de mensuração
    * Peso, Salário, Temperatura

O tipo de dados *é importante para ajudar a determinar o tipo de exposição visual, análise de dados ou modelo*. Ou seja, a identificação do tipo de variável não é só um detalhe técnico, é necessário por inúmeros motivos, é o que vai "dizer" o que será usado. Logo, É o que define o tipo de gráfico será utilizado, qual teste estatístico aplicar, qual algoritmo de machine learning funcionará melhor.

Sem esquecer dos tipos

* **Temporais**: que diz respeito a tempo. Data, mês, ano, dia...

* **Geoespaciais**: associados a localizações geográficas.

**Medidas da Estatística Descritiva**

* **Média**: Soma de todos os valores, dividida pelo número de valores.
  * *Ponto fraco*: muito sensível a outliers (ou seja, valores extremos)
  
* **Mediana**: É o valor comum, do 'centro da fila de valores', ou seja, medida mais robusta, por não ter impacto direto com *outliers* (*observações extremas aos valores)*.

* **Moda**: É a variável mais frequente em um conjunto de dados. Um conjunto de dados pode não ter moda, pode ter uma moda (unimodal) ou muitas modas (multimodal).

> Histograma: é a representação visual de uma frequência ou frequência relativa da distribuição de dados **quantitativos**. 
>
> ![image-histograma](https://github.com/igortude/aprendendo-estatistica-ml/blob/main/assets/histograma.png)

Em se tratando de Tendência central e simetria

![image-histograma](https://github.com/igortude/aprendendo-estatistica-ml/blob/main/assets/tendencia_simetria.png)

*Ao olhar para o gráfico, e identificar que a **média > mediana**, é possível saber que há uma assimetria à direita (**assimétrica positiva)** e vice-versa, o contrário seria **assimetria negativa**. A **moda** é sempre o pico, a mediana, corta ao meio.*

>  Detectando outliers: Calcula a amplitude interquartil (Q1- Q3) com a fórmula: 

IQR = Q3-Q1

Calcula 1,5 * IQR

Computa o limite inferior: Q1 - 1,5 * IQR

Computa também o limite superior: Q3 + 1,5 * IQR

*Qualquer valor maior que o limite superior ou menor que o limite inferior é um **outlier***.

Os outliers são identificados por * no box plot

![image-boxplot](https://github.com/igortude/aprendendo-estatistica-ml/blob/main/assets/boxplot.png)

E para não haver dúvidas, a mediana é o Q2 (ou segundo quartil).

> ==============SUMÁRIO DE 5 NÚMEROS==========================

**Medidas de Dispersão**

Mostram a extensão ou variabilidade de um conjunto de dados. 

**Variabilidade**: é necessário saber o quão espalhados estão os dados, então, fica no centro da estatística. Pense assim, 2 cidades que tem a temperatura média igual no ano, porém, uma com um verão super quente e a outra, com um inverno absurdamente congelante. Ou seja, o que muda? É exatamente a **variabilidade**

As medidas de dispersão mais comuns são:

* **Amplitude**: Calcula-se: Valor máximo - Valor mínimo ; é a medida mais simples. Não é uma boa medida quando usada sozinha, já que é computada usando apenas dois valores.
* **Variância**: *Medida baseada na média.* A distância que um valor está da média é seu **desvio**; a variância é a média de **desvios ao quadrado**.
  * Então, o que ela faz é calcular a distância de cada ponto até a média, eleva ao quadrado e depois tira uma média de tudo isso. Se o número dessa média for alto, significa que os dados estão bem espalhados.
    * Porém, também apresenta um problema. A medida é "ao quadrado", e pense que se estivermos medindo um salário em REAIS, a variância seria um número absurdamente grande. Fica difícil de interpretar.
* **Desvio-Padrão**:  é a raiz quadrada da variância, ou seja, trás a unidade dos dados, inicialmente ao quadrado, para unidade original dos dados, facilitando a interpretação.

**Covariância** é uma medida numérica que descreve a direção da relação linear entre duas variáveis

Covariância > 0: relação linear positiva

Covariância < 0: relação linear negativa

Covariância = 0: sem relação linear

Ou seja, coloca-se uma variável no eixo x e outra no eixo y e marca-se um ponto para cada observação. "De cara", já é possível notar se há alguma tendência. Se os pontos sobem juntos, a **relação** é **POSITIVA**, se um sobe e o outro desce, a **relação** é **NEGATIVA.**

Correlação, vem da covariância, o coeficiente de correlação descreve não somente a direção mas também o grau da relação. Sempre será entre 1 e -1 ou 100% -100%

Correlação > 0: relação linear positiva

Correlação < 0: relação linear negativa

Correlação=0: sem relação linear

Correlação=1: relação linear positiva forte

Correlação=-1: relação linear negativa forte

**r é o coeficiente de correlação.**

![image-correlacao](https://github.com/igortude/aprendendo-estatistica-ml/blob/main/assets/correlacao.png)

O modelo matemático para este caso é a **regressão linear simples** ( *Y= a+bX+e* ). Nada mais é do que a fórmula de uma reta que tenta passar o mais próximo possível de todos aqueles pontos do gráfico. E tem duas finalidades:

* **Explicação**: entender o relacionamento geral entre variáveis. Para entender a força e relação entre as variáveis, observa-se o coeficiente.
* **Previsão**: Adivinhar o valor de Y para um dado que não vimos antes.



**Algoritmos de Machine Learning**

Uma das tarefas mais comuns no mundo do ML é a classificação, que nada mais é do que a resposta de SIM/NÃO, com base nos dados. (Este e-mail é spam? SIM/NÃO ; Este cliente vai cancelar a assinatura? SIM/NÃO...).

Agora, falamos sobre **RANDOM FOREST** que é um algoritmo de ML, que ao invés de construir um modelo robusto, ele cria inúmeros de modelos mais simples, que observam parte da amostra dos dados, ou seja, vai repetindo o processo até que a floresta esteja pronta para a combinação das previsões de todas as árvores, e aí, há uma votação para a predição final.

Indo além do RF, temos o **Boosting**, com seu algoritmo **XGBoost**, que ao invés de construir centenas, milhares de árvores para a previsão, constrói uma árvore após a outra, focando nos erros apresentados na anterior, refinando o resultado final.



**Probabilidade** - A linguagem da incerteza

Bom, imagine que se quiséssemos saber a opinião de todas as pessoas no Brasil sobre algo, isso seria a população. Ou seja, é impossível perguntar à todo mundo. Então, pegamos uma amostra da população (um grupo menor) e utiliza-se essa amostra para tentar entender o todo, e é aí que nasce a probabilidade. 

É o alicerce matemático sobre o qual toda a inferência estatística está construída. 

**Teorema de Bayes**; Espécie de máquina de aprendizado. Começamos com uma crença inicial, e o teorema faz o trabalho de recalcular tudo e entrega uma nova crença com dados atualizados e mais precisos. E essa lógica está presente em praticamente todo o lugar. EX: Sugestão de filmes do NetFlix (baseado em filmes que você já assistiu). Filtro de SPAM de e-mail, baseado no estudo das palavras contidas...

* **Probabilidade condicional;** Probabilidade do evento A ocorrer, dado que o evento B já ocorreu. É representada por P(A|B). Ex: Qual a probabilidade de um cidadão que comprou um produto de marca X, comprar um mesmo produto de marca Y?



*Como os dados se distribuem?*

Tabelas de frequência - organização dos dados - Utilizadas para descrever a distribuição de **variáveis qualitativas**. 

​	a) Frequência Absoluta:  "quantas vezes, aquele nível daquela categoria, aparece no dataset". É basicamente uma contagem de quantas vezes aquela categoria (variável) aparece no dataset.

​	b) Frequência Relativa (ou proporção): é uma maneira de relativizar a frequência absoluta através dos 'totais'. É uma proporção ou taxa. 

​	c) Frequência Absoluta Acumulada

![image-20260427144424307](/home/igor/.var/app/io.typora.Typora/config/Typora/typora-user-images/image-20260427144424307.png)



​	d) Frequência Relativa Acumulada;

![image-20260427144606771](/home/igor/.var/app/io.typora.Typora/config/Typora/typora-user-images/image-20260427144606771.png)



--

![image-20260427145842301](/home/igor/.var/app/io.typora.Typora/config/Typora/typora-user-images/image-20260427145842301.png)



​																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																												A forma mais famosa e importante é a **Curva em Sino** (**Distribuição Normal ou Gaussiana**). é definida somente por dois parâmetros: I) **média** (onde fica o centro da curva), e o II) **desvio padrão**, que diz o quão espalhados estão os dados em volta do centro.

Regra Empírica: Se um conjunto de dados segue uma distribuição normal

 **>** **68-95-99,7%** **<**

exemplo: *Altura de homens adultos.*

* 68% dos dados estão a 1 desvio-padrão da média;																																																																				
* 95% dos dados estão a 2 desvios-padrão da média;
* 99,7% dos dados estão a 3 desvios-padrão da média;

Poder de previsão imenso!

Porém, muitos dados do mundo real como a renda das pessoas, não seguem essa curva de sino perfeitamente. Entra o conceito da **Teorema Central do Limite**, que diz que mesmo que os dados originais tenham distribuição completamente esquisita, se tirarmos diversas amostras e em seguida a média dessas amostras,  essas médias irão formar uma **distribuição normal perfeita**. (ex:  modelagem de contínuos, regressão. - Alturas, erros, notas)

**CONTANDO SUCESSOS**

**Binomial**: Modela o número de sucessos em 'n' tentativas. Ou seja,  lida com um número fixo de tentativas. (Taxas de conversão - Testes A/B - Cliques em anúncios)

​	ex: Cliques, vendas.

**Poisson**: Modela o número de eventos em um intervalo. Ou seja, não tem um número fixo, conta quantos eventos acontecem em um intervalo de tempo ou espaço. (Contagens por intervalo - Acessos/minuto a um site)

​	ex: Acessos por minuto; Chamadas por hora..

Contudo, quantos se tem poucos dados, ou quando o que importa é modelar o tempo até que uma coisa aconteça?

* **Distribuição t de Student**: Semelhante a Normal, mas com 'caudas mais largas', refletindo a maior incerteza de amostras pequenas. (Testes t, Regressão - Comparar médias de grupos).
  * **Exponencial**: excelente para medir o tempo entre eventos. Parte do princípio que o tempo de um evento acontecer, é sempre o mesmo.
    * ex: tempo entre a chegada de 2 clientes numa fila.
  * **Weibull**:  É mais flexível. Diz que a chance de falha, pode aumentar com o tempo.
    * Consegue modelar o tempo até a falha de um equipamento. A falha acontece mais brevemente conforme a peça vai envelhecendo.

 			​	

**Amostragem e Inferência**

***População vs Amostra > Teorema Central do Limite > Medindo Incerteza > Técnica do Bootstrap > Intervalos de Confiança***

**I) População vs Amostra:** A população é o grupo inteiro que se quer estudar. (Ex: todos os eleitores do país). Essa amostra tem que ser representativa. 

**II) Teorema Central do Limite** (**TCL**): Não importa o formato da distribuição de dados originais, pode ser algo completamente esquisito. A distribuição da média amostral se torna normal com amostras grandes, não importando a distribuição original.

**Medindo Incerteza**

**Erro-Padrão**: Desvio padrão de uma estatística amostral sobre muitas amostras 

