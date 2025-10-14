# 🐍 CURSO 2 — PYTHON PARA DATA SCIENCE
# Trabalhando com funções, estruturas de dados e exceções
# -------------------------------------------------------

# 🔹 BIBLIOTECAS
# Bibliotecas são pacotes com funções e métodos prontos para uso.

# Instalar uma biblioteca (executado no terminal ou notebook)
# pip install nome_da_biblioteca
# Exemplo:
# pip install numpy pandas matplotlib

# Listar bibliotecas instaladas
# pip list

# Importar bibliotecas
import numpy as np          # Importa o numpy com apelido 'np'
import pandas as pd         # Importa o pandas com apelido 'pd'
import matplotlib.pyplot as plt  # Importa matplotlib para gráficos

# 🔹 MÉTODOS COMUNS
lista = [1, 2, 3]
lista.append(4)             # Adiciona um elemento → [1, 2, 3, 4]

# 🔹 RANDOM (gera valores aleatórios)
import random
random.randint(1, 10)       # Retorna número inteiro aleatório entre 1 e 10
random.random()             # Retorna número decimal aleatório entre 0 e 1
random.sample(range(10), 3) # Escolhe 3 números únicos de 0 a 9
from random import choice
choice(["maçã", "banana", "uva"])  # Escolhe 1 item da lista

help(choice)                # Mostra documentação da função 'choice'

# 🔹 MATH (operações matemáticas)
import math
math.sqrt(9)                # Raiz quadrada → 3.0
math.pow(2, 3)              # Potência → 8.0
pow(2, 3)                   # Também faz potência → 8
round(3.14159, 2)           # Arredonda número → 3.14

# 🔹 FUNÇÕES
def media(notas):
    """Calcula a média de uma lista de notas"""
    return sum(notas) / len(notas)

resultado = media([6, 7, 8])
print(resultado)            # → 7.0

# 🔹 FUNÇÕES LAMBDA E MAP
# Funções anônimas (sem nome), úteis em operações rápidas
# map() aplica uma função a todos os itens de um iterável

numeros = [1, 2, 3, 4]
dobro = list(map(lambda x: x * 2, numeros))  # → [2, 4, 6, 8]

# 🔹 EXEMPLO DE ORGANIZAÇÃO DE DADOS
notas_turma = ["Ana", 7, 8, 9, "Bruno", 6, 7, 8]
nomes = []
notas_juntas = []

for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])      # Guarda o nome do aluno
    else:
        notas_juntas.append(notas_turma[i])  # Guarda as notas

print(nomes)         # → ['Ana', 'Bruno']
print(notas_juntas)  # → [7, 8, 9, 6, 7, 8]

# 🔹 TRATAMENTO DE EXCEÇÕES
# try / except / else / finally

try:
    notas = [6, 7, 8, "9"]               # "9" é string → erro
    resultado = media(notas)             # Pode gerar TypeError
except TypeError:
    print("❌ Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)                             # Captura outros erros de valor
else:
    print(resultado)                     # Executa se não houver erro
finally:
    print("✅ A consulta foi encerrada!")

# 🔹 VISUALIZAÇÃO COM MATPLOTLIB
# Criar um gráfico de barras simples

nomes = ["Ana", "Bruno", "Clara"]
medias = [7.5, 8.0, 6.5]

plt.bar(nomes, medias)                   # Cria gráfico de barras
plt.title("Médias da Turma")             # Título do gráfico
plt.xlabel("Estudantes")                 # Eixo X
plt.ylabel("Média")                      # Eixo Y
plt.show()                               # Exibe o gráfico