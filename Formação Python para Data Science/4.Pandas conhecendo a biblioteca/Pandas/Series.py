import pandas as pd
import numpy as np

# ========== CRIAÇÃO DE SERIES ==========

# Criando Series a partir de lista
serie_lista = pd.Series([10, 20, 30, 40, 50])
print("Series from list:")
print(serie_lista)

# Criando Series com índice personalizado
serie_index = pd.Series([100, 200, 300, 400], 
                       index=['A', 'B', 'C', 'D'])
print("\nSeries com índice personalizado:")
print(serie_index)

# Criando Series a partir de dicionário
dados_dict = {'São Paulo': 12.3, 'Rio de Janeiro': 6.7, 'Belo Horizonte': 2.5}
serie_dict = pd.Series(dados_dict)
print("\nSeries from dictionary:")
print(serie_dict)

# ========== OPERAÇÕES BÁSICAS ==========

print(f"\nValores da série: {serie_index.values}")
print(f"Índices da série: {serie_index.index}")
print(f"Tipo dos dados: {serie_index.dtype}")
print(f"Shape: {serie_index.shape}")

# Acesso a elementos
print(f"\nPrimeiro elemento: {serie_index['A']}")
print(f"Elementos B e C: {serie_index[['B', 'C']]}")

# ========== OPERAÇÕES MATEMÁTICAS ==========

print(f"\nSérie original: {serie_lista}")
print(f"Soma: {serie_lista.sum()}")
print(f"Média: {serie_lista.mean()}")
print(f"Desvio padrão: {serie_lista.std()}")
print(f"Valor máximo: {serie_lista.max()}")
print(f"Valor mínimo: {serie_lista.min()}")

# Operações vetoriais
serie_dobro = serie_lista * 2
serie_raiz = np.sqrt(serie_lista)
print(f"\nDobro dos valores: {serie_dobro}")
print(f"Raiz quadrada: {serie_raiz}")

# ========== FILTROS E CONDIÇÕES ==========

serie_notas = pd.Series([8.5, 7.0, 9.2, 6.8, 5.5, 10.0], 
                       index=['Ana', 'João', 'Maria', 'Pedro', 'Carla', 'Lucas'])

print("\nNotas dos alunos:")
print(serie_notas)

# Filtros
aprovados = serie_notas[serie_notas >= 7.0]
print("\nAlunos aprovados (nota >= 7.0):")
print(aprovados)

# Operações booleanas
maiores_que_8 = serie_notas > 8.0
print(f"\nNotas maiores que 8.0: {maiores_que_8}")

# ========== MÉTODOS ESTATÍSTICOS ==========

print(f"\nDescrição estatística:")
print(serie_notas.describe())

print(f"\nMediana: {serie_notas.median()}")
print(f"Moda: {serie_notas.mode().values}")

# ========== TRATAMENTO DE DADOS ==========

# Series com dados faltantes
serie_com_nan = pd.Series([1, 2, np.nan, 4, np.nan, 6])
print(f"\nSeries com NaN: {serie_com_nan}")
print(f"Valores não nulos: {serie_com_nan.dropna()}")
print(f"Preencher NaN com 0: {serie_com_nan.fillna(0)}")

# ========== ORDENAÇÃO ==========

print("\nSeries ordenada ascendente:")
print(serie_notas.sort_values())

print("\nSeries ordenada descendente:")
print(serie_notas.sort_values(ascending=False))

# ========== OPERAÇÕES COM STRINGS ==========

serie_nomes = pd.Series(['joão silva', 'MARIA Santos', 'Pedro Costa'])
print(f"\nNomes originais: {serie_nomes}")
print(f"Nomes em maiúsculo: {serie_nomes.str.upper()}")
print(f"Nomes capitalizados: {serie_nomes.str.title()}")
print(f"Primeiros nomes: {serie_nomes.str.split().str[0]}")