import pandas as pd
import matplotlib.pyplot as plt

# DataFrame com dados de vendas
df_vendas = pd.DataFrame({
    'Vendedor': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fernando', 
                 'Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fernando'],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'Mouse',
                'Teclado', 'Monitor', 'Mouse', 'Notebook', 'Teclado', 'Monitor'],
    'Categoria': ['Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 
                  'Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos',
                  'Acessórios', 'Eletrônicos', 'Acessórios', 'Eletrônicos'],
    'Valor_Venda': [2500, 50, 150, 800, 2200, 45, 120, 750, 55, 2800, 130, 820],
    'Mes': ['Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar', 'Abr', 'Abr', 'Abr']
})