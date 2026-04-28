import pandas as pd

data = {
    'Nome' : ['João', 'Maria', 'Pedro'],
    'Idade': [20, 25, 30],
    'Nota': [8, 9, 10],
    'Nota1': [6,7,8],
    'Nota2': [6,9,5]
    # 'Nota3': [7,8,4]
    
}


df = pd.DataFrame(data)

df['Nota Média'] = (df['Nota1'] + df['Nota2']) / 2

print(df)

# import pandas as pd

# lista = [
#     ['João', 20, 8],
#     ['Maria', 25, 9],
#     ['Pedro', 30, 10]
# ]

# df = pd.DataFrame(lista, columns=['Nome','Idade','Nota'])
# print(df)