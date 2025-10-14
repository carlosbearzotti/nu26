# 🧠 RESUMO GERAL — COMANDOS E FUNÇÕES EM PYTHON PARA DATA SCIENCE
# ---------------------------------------------------------------

# 🔹 ENTRADA, SAÍDA E TIPOS
input()      # Recebe entrada do usuário (sempre como string)
print()      # Exibe mensagens no console
type()       # Retorna o tipo do dado (int, float, str, etc.)
int()        # Converte para número inteiro
float()      # Converte para número decimal

# 🔹 STRINGS
.upper()     # Transforma texto em MAIÚSCULAS
.lower()     # Transforma texto em minúsculas
.strip()     # Remove espaços extras do início e fim
.replace()   # Substitui parte do texto por outro
chr()        # Converte número em caractere (ex: 65 → 'A')

# 🔹 ESTRUTURAS DE CONTROLE
if / elif / else   # Estruturas condicionais
for / while        # Laços de repetição
range()            # Gera uma sequência numérica
match / case       # Estrutura de decisão (Python 3.10+)

# 🔹 OPERADORES
<  >  <=  >=       # Comparações numéricas
==  !=              # Igual / diferente
in                 # Verifica se um valor pertence a um conjunto

# 🔹 FUNÇÕES ÚTEIS
sum()       # Soma elementos de uma lista ou tupla
len()       # Conta quantos elementos existem
max()       # Retorna o maior valor
min()       # Retorna o menor valor
sorted()    # Retorna lista ordenada
round()     # Arredonda números (round(3.1415, 2) → 3.14)
pow()       # Potência (pow(2,3) → 8)

# 🔹 ESTRUTURAS DE DADOS
list()      # Lista (coleção ordenada e mutável)
dict()      # Dicionário (pares chave:valor)
set()       # Conjunto (sem valores duplicados)

.append()   # Adiciona elemento a uma lista
.keys()     # Retorna as chaves de um dicionário
.values()   # Retorna os valores de um dicionário

# 🔹 COMPREENSÕES (COMPREHENSIONS)
[x**2 for x in range(5)]         # List comprehension
{x: x*2 for x in range(3)}       # Dict comprehension

# 🔹 FUNÇÕES E TRATAMENTO DE ERROS
def nome_funcao():   # Define uma função
    pass

lambda               # Cria função anônima (sem nome)
map()                # Aplica uma função a cada item de um iterável

try / except / else / finally   # Tratamento de exceções (erros)

# 🔹 MÓDULOS E IMPORTAÇÕES
import nome_modulo             # Importa um módulo
import modulo as apelido       # Importa com apelido (ex: import numpy as np)
from modulo import funcao      # Importa função específica
help(funcao)                   # Mostra ajuda/documentação de uma função

# 🔹 BIBLIOTECAS
pip install nome               # Instala biblioteca (no terminal)
pip list                       # Mostra bibliotecas instaladas

# 🔹 RANDOM (valores aleatórios)
import random
random.randint(a, b)           # Número inteiro aleatório entre a e b
random.random()                # Número decimal aleatório entre 0 e 1
random.sample(seq, n)          # Seleciona n itens únicos de uma sequência
from random import choice
choice(lista)                  # Escolhe 1 item aleatório da lista

# 🔹 MATH (operações matemáticas)
import math
math.sqrt(x)                   # Raiz quadrada
math.pow(x, y)                 # Potência (x^y)

# 🔹 MATPLOTLIB (visualização de dados)
import matplotlib.pyplot as plt
plt.bar(x, y)                  # Cria gráfico de barras
plt.title()                    # Define o título do gráfico
plt.xlabel()                   # Nome do eixo X
plt.ylabel()                   # Nome do eixo Y
plt.show()                     # Exibe o gráfico

# 🔹 NUMPY E PANDAS (análise de dados)
import numpy as np
import pandas as pd
# (Exemplos práticos vistos em cursos seguintes)