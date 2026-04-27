## 2️⃣ README_FUNDAMENTOS.md

```markdown
# 📊 Módulo 01: Fundamentos de Estatística

## 🎯 Objetivo

Construir uma base sólida em **Estatística e Análise Exploratória de Dados (EDA)** usando Python.

Você vai aprender:
- ✅ O que é estatística e por que importa
- ✅ Como explorar dados reais
- ✅ Como identificar padrões
- ✅ Como decidir quais variáveis usar em um modelo

---

## 📚 Conteúdo

### Notebook 00: Python Básico + Estatística Descritiva

**Duração:** ~3-4 horas

**Objetivo:** Aprender o Python mínimo e entender conceitos básicos de estatística.

#### Conteúdo

##### Parte 1: Importações e Setup
- Importar bibliotecas (pandas, numpy, matplotlib, seaborn)
- Carregar dataset
- Explorar estrutura básica

##### Parte 2: Estatística Descritiva
- **Medidas Centrais:**
  - Média (soma ÷ quantidade)
  - Mediana (o valor do meio)
  - Moda (valor que mais aparece)

- **Medidas de Dispersão:**
  - Variância (quanto os dados variam)
  - Desvio Padrão (raiz da variância)
  - Amplitude (max - min)

- **Quartis:**
  - Q1 (25º percentil): 25% ganham menos
  - Q2/Mediana (50º percentil): 50% ganham menos
  - Q3 (75º percentil): 75% ganham menos
  - IQR (Intervalo Interquartil): Q3 - Q1

##### Parte 3: Visualizações
- **Histograma:** Ver a distribuição dos dados
- **Box Plot:** Ver quartis, mediana e outliers
- **Violin Plot:** Ver distribuição completa
- **Gráfico de Barras:** Contar categorias

##### Parte 4: Exploração de Categorias
- Entender colunas categóricas ( o)
- Contar quantas categorias diferentes tem
- Ver a distribuição de cada categoria

---

### Notebook 01: Análise Exploratória Avançada (EDA)

**Duração:** ~3-4 horas

**Objetivo:** Entender como as variáveis se relacionam e decidir qual usar no modelo.

#### Conteúdo

##### Parte 1: Correlação Numérica
- O que é correlação (como duas variáveis se relacionam)
- Tipos de correlação:
  - **Positiva:** Uma sobe, outra sobe (+0.8)
  - **Negativa:** Uma sobe, outra desce (-0.7)
  - **Nenhuma:** Sem relação (0.0)
- Matriz de Correlação (tabela com todas as relações)
- Heatmap (visualizar correlação com cores)

##### Parte 2: Relacionamentos Categóricos
- Salário vs Experience_Level
  - Entry, Mid, Senior
  - Diferença: 270.9% (MUITO FORTE)
- Salário vs Country
  - USA, UK, Canada, Germany, India
  - Diferença: 226.0% (MUITO FORTE)
- Salário vs Job_Title
  - NLP Engineer, Data Scientist, etc
  - Diferença: 6.5% (FRACO)
- Salário vs Top_Skill
  - PyTorch, SQL, Python, etc
  - Diferença: 6.1% (FRACO)
- Salário vs Remote
  - Yes/No
  - Diferença: 3.3% (IRRELEVANTE)
- Salário vs Company_Type
  - Big Tech, Startup, Freelance
  - Diferença: 1.2% (IRRELEVANTE)

##### Parte 3: Seleção de Features
- Feature Selection: escolher variáveis importantes
- Descartar variáveis inúteis
- Decidir qual combinar

##### Parte 4: Cruzamento de Variáveis
- Tabela cruzada: Experience x Country
- Entender combinações
- Senior + USA = salário máximo
- Entry + India = salário mínimo

---

## 🔑 Conceitos-Chave

### Média vs Mediana
MÉDIA:
└─ Soma tudo, divide pela quantidade
└─ Afetada por outliers (valores extremos)
└─ Use quando: distribuição simétrica

MEDIANA:
└─ Valor do meio
└─ NÃO é afetada por outliers
└─ Use quando: distribuição enviesada (skewed)

EXEMPLO:
Salários: [40k, 50k, 60k, 1.000k]
Média = 262.5k (puxada para cima!)
Mediana = 55k (mais real)

 


### Desvio Padrão
DEFINIÇÃO:
"Quanto, em média, os dados variam da média"

INTERPRETAÇÃO:
Desvio = $58.925
Média = $94.723

└─ 68% dos dados estão entre: $35.798 e $153.648
└─ Desvio PEQUENO = dados agrupados
└─ Desvio GRANDE = dados espalhados

 


### Quartis e IQR
Q1 (25%): 25% ganham MENOS que isso
Q2 (50%): 50% ganham MENOS que isso (=MEDIANA)
Q3 (75%): 75% ganham MENOS que isso

IQR = Q3 - Q1 (altura da caixa no box plot)

OUTLIERS:
Limite inferior = Q1 - 1.5 × IQR
Limite superior = Q3 + 1.5 × IQR
└─ Valores fora desses limites = outliers

 


### Correlação
COEFICIENTE DE PEARSON:

-1.0 ← Correlação negativa PERFEITA (nunca sobe junto)
-0.7 ← Correlação negativa FORTE
-0.3 ← Correlação negativa FRACA
0.0 ← SEM correlação (independentes)
+0.3 ← Correlação positiva FRACA
+0.7 ← Correlação positiva FORTE
+1.0 ← Correlação positiva PERFEITA (sempre sobe junto)

EXEMPLO:
Experience vs Salary: +0.85 (forte positiva)
└─ Mais experiência = mais salário

Remote vs Salary: +0.03 (praticamente zero)
└─ Ser remote não afeta o salário

 


---

## 🎨 Visualizações Explicadas

### Histograma
O que mostra:
└─ Distribuição de uma variável numérica
└─ Quantas pessoas em cada faixa de salário

Como ler:
└─ Eixo X: Salários
└─ Eixo Y: Quantidade de pessoas
└─ Altura da barra: Quantas pessoas ganham naquele valor

Quando usar:
└─ Ver a "forma" dos dados
└─ Identificar se tem outliers
└─ Checar se é simétrico ou enviesado

 


### Box Plot
O que mostra:
└─ Quartis, mediana e outliers

Partes:
├─ Caixa: 50% dos dados (Q1 a Q3)
├─ Linha na caixa: MEDIANA (Q2)
├─ Bigodes: Mínimo e máximo "normais"
└─ Pontinhos: Outliers (fora do padrão)

Quando usar:
└─ Comparar distribuição entre categorias
└─ Ver simetria vs assimetria
└─ Identificar outliers rapidamente

 


### Violin Plot
O que mostra:
└─ Distribuição COMPLETA de uma variável

Como ler:
└─ Largura = densidade de pessoas naquele valor
└─ Mais largo = mais concentrado lá
└─ Mais estreito = menos concentrado

Quando usar:
└─ Melhor que box plot para exploração
└─ Ver a "forma" completa dos dados
└─ Comparar distribuição entre grupos

 


### Heatmap
O que mostra:
└─ Correlação entre todas as variáveis

Como ler:
├─ Vermelho: Correlação positiva forte
├─ Azul: Correlação negativa forte
└─ Branco/Claro: Pouca/nenhuma correlação

Quando usar:
└─ Ver todas as relações de uma vez
└─ Identificar variáveis correlacionadas
└─ Planejar seleção de features

 


---

## 📊 Resultados Principais

### Dataset
Total: 2.000 registros
Colunas: 8
Dados faltando: 0 (100% completo!)

 


### Variáveis Numéricas
Year (2022-2026)
Salary_USD:
└─ Mínimo: $8.080
└─ Máximo: $233.977
└─ Média: $94.723
└─ Mediana: $77.489
└─ Desvio Padrão: $58.925
└─ Distribuição: Enviesada à direita

 


### Variáveis Categóricas
Job_Title: 5 categorias
└─ NLP Engineer (20.7%)
└─ Data Analyst (19.9%)
└─ Data Scientist (18.9%)
└─ ML Engineer (19.2%)
└─ AI Engineer (21.3%)
└─ Padrão: Bem distribuído

Country: 5 categorias
└─ UK (20.4%)
└─ Canada (20.2%)
└─ India (19.9%)
└─ Germany (19.7%)
└─ USA (19.7%)
└─ Padrão: Bem distribuído

Experience_Level: 3 categorias
└─ Senior (34.1%)
└─ Entry (33.8%)
└─ Mid (32.2%)
└─ Padrão: Bem distribuído

Company_Type: 3 categorias
└─ Big Tech (33.5%)
└─ Startup (33.4%)
└─ Freelance (33.1%)
└─ Padrão: Bem distribuído

Remote: 2 categorias
└─ Yes (50.8%)
└─ No (49.2%)
└─ Padrão: Perfeitamente equilibrado

Top_Skill: 5 categorias
└─ PyTorch (22.1%)
└─ SQL (20.8%)
└─ Python (19.8%)
└─ TensorFlow (19.1%)
└─ NLP (18.4%)
└─ Padrão: Bem distribuído

 


### Influência de Cada Variável

| Variável | Diferença % | Influência | Ação |
|----------|-----------|-----------|------|
| Experience_Level | 270.9% | ⭐⭐⭐⭐⭐ | ✅ INCLUIR |
| Country | 226.0% | ⭐⭐⭐⭐⭐ | ✅ INCLUIR |
| Job_Title | 6.5% | ⭐⭐ | ❌ Descartar |
| Top_Skill | 6.1% | ⭐⭐ | ❌ Descartar |
| Remote | 3.3% | ⭐ | ❌ Descartar |
| Company_Type | 1.2% | ⭐ | ❌ Descartar |
| Year | Temporal | - | ❌ Descartar |

---

## 🎯 Feature Selection

### Variáveis Selecionadas Para o Modelo
Experience_Level
├─ Diferença: 270.9% (MUITO FORTE)
├─ Tipo: Categórica (Entry, Mid, Senior)
└─ Razão: Capacitação profissional → salário

Country
├─ Diferença: 226.0% (MUITO FORTE)
├─ Tipo: Categórica (USA, UK, Canada, Germany, India)
└─ Razão: Custo de vida e economia local

 


### Por Que Descartar as Outras?
Job_Title (6.5%):
└─ Diferença muito pequena
└─ Não vale a complexidade adicionada

Top_Skill (6.1%):
└─ Praticamente igual a Job_Title
└─ Redundante

Remote (3.3%):
└─ Praticamente nenhuma influência
└─ Ser remote não afeta salário

Company_Type (1.2%):
└─ Praticamente irrelevante
└─ Tipo de empresa não afeta salário

Year:
└─ Correlação é temporal, não causal
└─ Salários sobem porque tem mais seniors em 2025
└─ Não é Year em si que causa aumento

 


---

## 💡 Insights Principais

### Descoberta 1: Experience é Rei
Entry: ~$48.000
Mid: ~$88.000 (+83% vs Entry)
Senior: ~$130.000 (+48% vs Mid)

Total: Entry → Senior = +270%

Conclusão:
└─ Experiência é o fator MAIS importante
└─ Investir em desenvolvimento profissional = mais dinheiro

 


### Descoberta 2: País Importa MUITO
USA: ~$120.000
UK: ~$100.000
Canada: ~$99.000
Germany: ~$98.000
India: ~$50.000

Total: USA vs India = +226%

Conclusão:
└─ Custo de vida e economia local definem salário
└─ Trabalhar em país rico = ganhar mais

 


### Descoberta 3: Remote Não Influencia
Remote (Sim): ~$96.000
Remote (Não): ~$93.000

Diferença: +3.3%

Conclusão:
└─ Ser home office não muda salário
└─ O que importa é a competência, não o local

 


### Descoberta 4: Cruzamento Experience x Country
MÁXIMO: Senior + USA = ~$180.000
MÍNIMO: Entry + India = ~$40.000
RAZÃO: 450% de diferença!

Padrão:
└─ USA sempre no topo (independente da experiência)
└─ India sempre embaixo
└─ Experience sobe em todos os países (mas proporção diferente)

 


---

## 🚀 Próximo Módulo

Quando terminar este módulo, você estará pronto para:

**Módulo 02: Regressão Linear**
- Usar Experience_Level + Country para PREVER salários
- Entender como um modelo aprende
- Fazer predições

---

## 📖 Recursos Adicionais

- Livros recomendados: `recursos_adicionais/livros_recomendados.md`
- Vídeos: `recursos_adicionais/videos_recomendados.md`
- Fórmulas simplificadas: `recursos_adicionais/formulario_simplificado.md`
- Dicas de Python: `recursos_adicionais/dicas_python_basico.md`
- Dicas de Matemática: `recursos_adicionais/dicas_matematica.md`

---

## ✅ Checklist: Você Aprendeu?

Após completar este módulo, você consegue:

- [ ] Carregar dados com Pandas
- [ ] Calcular média, mediana e desvio padrão
- [ ] Entender a diferença entre média e mediana
- [ ] Fazer histogramas e box plots
- [ ] Entender correlação
- [ ] Ler um heatmap
- [ ] Decidir qual variável é importante
- [ ] Explicar por que tal variável influencia o resultado
- [ ] Preparar dados para um modelo

Se marcou todos → **Você completou o Módulo 01!** 🎉

---

**Próximo:** Notebook 02 - Regressão Linear 🚀