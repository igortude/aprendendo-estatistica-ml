\# 📊 Aprendendo Estatística e Machine Learning do Zero 

## Minha história 

Saí da escola cedo, fiz Direito, depois Educação Física. Agora estou no Tecnólogo em Ciência de Dados e descobri que **não entendia nada de estatística**. A faculdade é rápida. Os vídeos pulam etapas. Os livros assumem coisas que você não sabe. Decidi criar este repositório para **aprender de verdade e compartilhar com quem  é como eu: estuda sozinho, teve dificuldade com matemática, ou precisa de tempo para entender**. 

## Como funciona 

Cada notebook segue este padrão: 

1. **O que vou aprender** (no início) 
2. **Código comentado** (linha por linha, não é resumido) 
3. **Explicações em markdown** (não é só código) 
4. **Visualizações** (gráficos ajudam a entender) 
5. **Conclusões** (o que aprendemos?) 

## DataSet

Estou usando: **AI Job Market Trends 2022-2026** (Kaggle).

**Por quê?**

- Relevante (é sobre a área que estou estudando)
- Dados reais (2000 registros, 8 colunas)
- Mistura dados numéricos e categóricos
- Sem dados faltando (100% completo)
- Tamanho pequeno o suficiente para aprender

**Colunas:** Year, Job_Title, Country, Company_Type, Experience_Level, Salary_USD, Remote, Top_Skill



## Roadmap 

- [x] Importar bibliotecas (pandas, numpy, matplotlib, seaborn)

- [x] Carregar Dados com pd.read_csv()

- [x] Explorar estrutura (shape, info, columns, dtypes)

- [x] Fundamentos de Estatística

- [x] Calcular estatísticas:

  - Média, Mediana, Desvio Padrão, Variância
  - Quartis (Q1, Q2, Q3) e IQR
  - Mínimo, Máximo

- [x] Entender diferença entre Média e Mediana

- [x] Identificar outliers (método IQR)

- [x] Criar visualizações:

  - Histogramas (ver distribuição)
  - Box Plots (ver quartis e outliers)
  - Gráficos de barras (categorias)

- [x] Explorar colunas categóricas

- [x] Descobrir padrões iniciais

  #### **Notebook 01: Análise Exploratória Avançada (EDA)**

- [x] Entender correlação (positiva, negativa, nenhuma)

- [x] Calcular Matriz de Correlação

- [x] Visualizar com Heatmap

- [x] Analisar Year vs Salary (correlação temporal vs casual)

- [x] Explorar Experience_Level:

  - Entry vs Mid vs Senior
  - Diferença de 270.9% (MUITO FORTE)
  - Visualizar com Boxplot

- [x] Explorar Country:

  - USA vs India vs demais países
  - Diferença de 226.0% (MUITO FORTE)
  - Visualizar com Violin Plot

- [x] Explorar Job_Title:

  - Diferença de apenas 6.5% (FRACO)
  - Descartável para o modelo

- [x] Explorar Top_Skill:

  - Diferença de 6.1% (FRACO)
  - Praticamente igual a Job_Title

- [x] Explorar Remote:

  - Diferença de apenas 3.3% (IRRELEVANTE)

- [x] Explorar Company_Type:

  - Diferença de apenas 1.2% (IRRELEVANTE)

- [x] Feature Selection:

  - Identificar variáveis que importam
  - Descartar variáveis inúteis

- [x] Cruzamento Experience_Level x Country:

  - Entender como as variáveis se combinam
  - Senior + USA = máximo salário (~$180k)
  - Entry + India = mínimo salário (~$40k)

  

  ### 📌 Em Progresso (Próximo)

- [ ] **Notebook 02: Regressão Linear**

  - Codificar variáveis categóricas
  - Treinar modelo linear com Experience_Level + Country
  - Fazer previsões de salário
  - Entender coeficientes
  - Calcular R², MAE, RMSE
  - Visualizar reta de regressão
  - Analisar resíduos

  ### ⏳ Próximos Passos

  **Notebook 03: Comparação de Modelos**

  - Regressão Linear vs Random Forest vs XGBoost
  - Cross-validation
  - Métricas comparativas
  - Evitar overfitting

  **Notebook 04: Interpretabilidade & Insights**

  - Feature Importance (Random Forest + XGBoost)
  - Análise de resíduos
  - SHAP values
  - Conclusões: qual modelo usar quando?



## 🎓 O Que Você Vai Aprender

### Fundamentos de Estatística

- ✅ Tipos de dados (numérico, categórico)
- ✅ Medidas centrais (média, mediana, moda)
- ✅ Medidas de dispersão (variância, desvio padrão)
- ✅ Quartis e IQR (Intervalo Interquartil)
- ✅ Distribuições e outliers
- ✅ Correlação e relação entre variáveis
- ⏳ Distribuição normal
- ⏳ Testes estatísticos



### Análise Exploratória (EDA)

- ✅ Explorar estrutura dos dados
- ✅ Identificar padrões
- ✅ Seleção de features (Feature Selection)
- ✅ Cruzamento de variáveis
- ⏳ Transformação de dados



### Machine Learning

- ⏳ Regressão Linear (conceito, cálculo, interpretação)
- ⏳ Random Forest (como funciona, vantagens)
- ⏳ XGBoost (boosting, quando usar)
- ⏳ Validação de modelos
- ⏳ Métricas (MAE, RMSE, R²)

### Python para Ciência de Dados

- ✅ Pandas (carregar, explorar, manipular)
  - `df.head()`, `df.shape()`, `df.info()`
  - `df.describe()`, `df.columns`
  - `df.groupby()`, `df.pivot_table()`
  - `df.select_dtypes()`, `df.isnull()`
- ✅ NumPy (cálculos matemáticos)
  - Operações básicas com arrays
- ✅ Matplotlib (gráficos básicos)
  - `plt.hist()`, `plt.boxplot()`, `plt.barh()`
  - `plt.subplots()`, `plt.plot()`
- ✅ Seaborn (gráficos bonitos)
  - `sns.boxplot()`, `sns.violinplot()`, `sns.heatmap()`
  - Paletas de cores
- ⏳ Scikit-learn (modelos de ML)



## 🎯 Para Quem Tem Dificuldade com Matemática

**Spoiler:** Você não precisa de QI 190. Precisa de:

- **Paciência** (não corre)
- **Repetição** (faz mais de uma vez)
- **Curiosidade** (por que funciona?)

Este repositório foi feito pensando em **você**.

Cada fórmula vem com explicação.
Cada conceito vem com exemplo.
Cada código vem com comentário.



## 📁 Estrutura do Repositório

```
aprendendo-estatistica-ml/
│
├── README.md (você está aqui!)
├── requirements.txt (dependências)
├── COMECE_AQUI.md (instruções iniciais)
│
├── 01_Fundamentos_Estatistica/
│   ├── 00_Python_Basico_Para_Ciencia_de_Dados.ipynb ✅ CONCLUÍDO
│   ├── 01_Analise_Exploratoria_Avancada_EDA.ipynb ✅ CONCLUÍDO
│   └── README_FUNDAMENTOS.md
│
├── 02_Regressao_Linear/
│   ├── 01_Regressao_Linear_Explicada.ipynb (próximo)
│   ├── 02_Prever_Salarios.ipynb
│   └── README_REGRESSAO.md
│
├── 03_Modelos_ML/
│   ├── 01_Random_Forest_Explicado.ipynb
│   ├── 02_XGBoost_Passo_a_Passo.ipynb
│   ├── 03_Comparacao_Modelos.ipynb
│   └── README_MODELOS.md
│
├── recursos_adicionais/
│   ├── dicas_python_basico.md
│   ├── dicas_matematica.md
│   ├── formulario_simplificado.md
│   └── videos_recomendados.md
│
├── dados/
│   └── ai-job-market.csv
│
└── .gitignore
```



## 🚀 Como Usar Este Repositório

### 1. **Clone ou baixe**

```
git clone https://github.com/seu_usuario/aprendendo-estatistica-ml.git
cd aprendendo-estatistica-ml
```

### 2. **Configure o ambiente**

```
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3. **Abra o Jupyter**

```
jupyter notebook
```

### 4. **Comece pelo Notebook 00**

Siga a ordem. Cada notebook depende do anterior.



## 📈 Principais Descobertas Até Agora

### Sobre o Dataset

```
Total de registros: 2000
Dados faltando: 0 (100% completo!)
```

### Sobre Salários

```
Salário Mínimo: $8.080
Salário Máximo: $233.977
Salário Médio: $94.723
Salário Mediana: $77.489 (mais representativo)
Distribuição: Enviesada à direita
```

### Variáveis Que Importam

| Variável             | Influência | Ação        |
| -------------------- | ---------- | ----------- |
| **Experience_Level** | 270.9%     | ✅ INCLUIR   |
| **Country**          | 226.0%     | ✅ INCLUIR   |
| Job_Title            | 6.5%       | ❌ Descartar |
| Top_Skill            | 6.1%       | ❌ Descartar |
| Remote               | 3.3%       | ❌ Descartar |
| Company_Type         | 1.2%       | ❌ Descartar |
| Year                 | Temporal   | ❌ Descartar |

### Feature Selection (Seleção de Variáveis)

```
Para prever salário, use APENAS:
1. Experience_Level (Entry, Mid, Senior)
2. Country (USA, UK, Canada, Germany, India)

Isso explica ~90% da variação!
```

### Cruzamento Experience x Country

```
MÁXIMO:  Senior + USA       = ~$180.000
MÍNIMO:  Entry + India      = ~$40.000
RAZÃO:   450% de diferença!
```

------

## 🤝 Como Contribuir

**Achou um erro?** Abra uma issue.

**Tem uma dúvida?** Abra uma issue.

**Quer sugerir algo?** Abra uma issue.

**Quer compartilhar seu aprendizado?** Faça um fork, estude, e volte com suas anotações!

------

## 📖 Recursos Recomendados

- **Livros:** Veja em `recursos_adicionais/livros_recomendados.md`
- **Vídeos:** Veja em `recursos_adicionais/videos_recomendados.md`
- **Canais:** TeoMewhy (YouTube)

------

## ⚠️ Disclaimer

Este repositório é feito por alguém **aprendendo**, para pessoas **aprendendo**.

Não é um substituto para:

- Um curso profissional
- Mentoria de um especialista
- Formação acadêmica

**É um complemento.** Um lugar para entender devagar.

------

## 📝 Licença

Este projeto é open source. Fique à vontade para estudar, copiar, modificar e compartilhar.

------

## 🙏 Agradecimentos

- Ao TeoMewhy por inspirar o aprendizado lento e profundo
- À comunidade do Kaggle por datasets reais
- A todos que passaram por isso e entendem a dificuldade



**Última atualização:** Abril 2026

**Status:** 🟡 Em desenvolvimento ativo

**Próximo notebook:** Regressão Linear

**Progresso Total:** ~40% (2 de 5 notebooks concluídos)