**TIPOS DE VARIÁVEIS**

Basicamente existem 4 tipos de variáveis.

- **Qualitativas**:
  - *Nominal*: Categorias sem ordem natural - EX: gênero, cor, cidade
  - *Ordinal*: Categorias com ordem natural - nível de ensino, satisfação...
- **Quantitativas **(números)
  * Discreta: Valores de contagem
    * Número de cliques, quantidade de produtos em um carrinho..
  * Contínua: Valores de mensuração
    * Peso, Salário, Temperatura

O tipo de dados é importante para ajudar a determinar o tipo de exposição visual, análise de dados ou modelo. Ou seja, a identificação do tipo de variável não é só um detalhe técnico, é necessário por inúmeros motivos, é o que vai "dizer" o que será usado. Logo, É o que define o tipo de gráfico será utilizado, qual teste estatístico aplicar, qual algoritmo de machine learning funcionará melhor.

Medidas da Estatística Descritiva

* **Média**: Soma de todos os valores, dividida pelo número de valores.

  * Ponto fraco: muito sensível a outliers (ou seja, valores extremos)

* **Mediana**: É o valor comum, do 'centro da fila de valores', ou seja, medida mais robusta, por não ter impacto direto com outliers.

* **Variabilidade**: é necessário saber o quão espalhados estão os dados, então, fica no centro da estatística. Pense assim, 2 cidades que tem a temperatura média igual no ano, porém, uma com um verão super quente e a outra, com um inverno absurdamente congelante. Ou seja, o que muda? É exatamente a **variabilidade**

  * uma das principais formas de  medir essa dispersão é a **VARIÂNCIA**. Então, o que ela faz é calcular a distância de cada ponto até a média, eleva ao quadrado e depois tira uma média de tudo isso. Se o número dessa média for alto, significa que os dados estão bem espalhados.

    * Porém, também apresenta um problema. A medida é "ao quadrado", e pense que se estivermos medindo um salário em REAIS, a variância seria um número absurdamente grande. Fica difícil de interpretar.

    E é onde entra o **DESVIO PADRÃO**, que é nada mais nada menos a raiz quadrada da variância, ou seja, trás a unidade dos dados, inicialmente ao quadrado, para unidade original dos dados, facilitando a interpretação.



**Diagrama de Dispersão**

Coloca-se uma variável no eixo x e outra no eixo y e marca-se um ponto para cada observação. "De cara", já é possível notar se há alguma tendência. Se os pontos sobem juntos, a relação é **POSITIVA**, se um sobe e o outro desce, a relação é **NEGATIVA.**

O modelo matemático para este caso é a **regressão linear simples** ( *Y= a+bX+e* ). Nada mais é do que a fórmula de uma reta que tenta passar o mais próximo possível de todos aqueles pontos do gráfico. E tem duas finalidades:

* **Explicação**: entender o relacionamento geral entre variáveis. Para entender a força e relação entre as variáveis, observa-se o coeficiente.
* **Previsão**: Adivinhar o valor de Y para um dado que não vimos antes.



**Algoritmos de Machine Learning**

Uma das tarefas mais comuns no mundo do ML é a classificação, que nada mais é do que a resposta de SIM/NÃO, com base nos dados. (Este e-mail é spam? SIM/NÃO ; Este cliente vai cancelar a assinatura? SIM/NÃO...).

Agora, falamos sobre **RANDOM FOREST** que é um algoritmo de ML, que ao invés de construir um modelo robusto, ele cria inúmeros de modelos mais simples, que observam parte da amostra dos dados, ou seja, vai repetindo o processo até que a floresta esteja pronta para a combinação das previsões de todas as árvores, e aí, há uma votação para a predição final.

Indo além do RF, temos o **Boosting**, com seu algoritmo **XGBoost**, que ao invés de construir centenas, milhares de árvores para a previsão, constrói uma árvore após a outra, focando nos erros apresentados na anterior, refinando o resultado final.

