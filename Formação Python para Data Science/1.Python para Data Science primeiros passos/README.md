# Estudos Data Science
Projetos para estudo para teste técnico

# 🐍 PYTHON PARA DATA SCIENCE: PRIMEIROS PASSOS
# ----------------------------------------------

# 🔹 TIPOS E FUNÇÕES BÁSICAS
int("10")           # Converte string para número inteiro → 10
float("3.14")       # Converte string para número decimal → 3.14
input("Digite: ")   # Recebe entrada do usuário como string
print("Olá")        # Exibe mensagem no console
type(3.14)          # Retorna o tipo do dado → <class 'float'>

# 🔹 MANIPULAÇÃO DE STRINGS
"python".upper()          # Transforma em maiúsculas → 'PYTHON'
"PYTHON".lower()          # Transforma em minúsculas → 'python'
"  texto  ".strip()       # Remove espaços extras → 'texto'
"data".replace("a", "@")  # Substitui partes do texto → 'd@t@'
chr(65)                   # Converte número em caractere → 'A'

# 🔹 ESTRUTURAS DE CONTROLE
x = 10
if x > 0:
    print("Positivo")
elif x == 0:
    print("Zero")
else:
    print("Negativo")

# Laços de repetição
for i in range(5):        # Executa de 0 a 4
    print(i)

contador = 0
while contador < 3:       # Executa enquanto a condição for verdadeira
    print(contador)
    contador += 1

# Estrutura match (Python 3.10+)
cor = "vermelho"
match cor:
    case "azul":
        print("Cor fria")
    case "vermelho":
        print("Cor quente")
    case _:
        print("Cor desconhecida")

# 🔹 OPERADORES
# Comparações
# < menor que, <= menor ou igual, >= maior ou igual, == igual, != diferente
a, b = 5, 10
print(a < b)    # True
print(a == b)   # False

# Verificação de pertencimento
print(3 in [1, 2, 3])     # True
print("a" in "data")      # True

# 🔹 FUNÇÕES ÚTEIS
numeros = [10, 20, 30]
print(sum(numeros))       # Soma elementos → 60
print(len(numeros))       # Conta elementos → 3

# 📚 ESTRUTURAS DE DADOS

# Lista (list) — coleção ordenada e mutável
frutas = ["maçã", "banana", "uva"]

# Dicionário (dict) — pares chave:valor
pessoa = {"nome": "Ana", "idade": 25}

# Conjunto (set) — coleção sem duplicatas
numeros = {1, 2, 3, 3}     # → {1, 2, 3}

# Compreensão de listas (list comprehension)
quadrados = [x**2 for x in range(5)]   # → [0, 1, 4, 9, 16]

# Compreensão de dicionários (dict comprehension)
dobros = {x: x*2 for x in range(3)}    # → {0: 0, 1: 2, 2: 4}

# Funções built-in (nativas do Python)
print(max([1, 5, 3]))    # Maior valor → 5
print(min([1, 5, 3]))    # Menor valor → 1
print(sorted([3, 1, 2])) # Ordena → [1, 2, 3]