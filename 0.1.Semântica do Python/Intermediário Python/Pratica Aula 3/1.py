# ====================================================
# EXEMPLOS DE USO DE LISTAS E DICIONÁRIOS
# ====================================================

# =========================================
# Exemplo 1: Soma de listas dentro de lista de listas
# =========================================

lista_de_listas = [[1,2,3],[4,5,6],[7,8,9]]

for lista in lista_de_listas:
    print(sum(lista))  # Soma todos os elementos de cada sublista
    lista = []         # Não altera lista_de_listas, só a variável local
# 6
# 15
# 24

# =========================================
# Exemplo 2: Extraindo elementos de tuplas
# =========================================

lista_de_tuplas = (
    ("Júlia", 23, "São Paulo", "SP", "Python para DS 1"),
    ("Carlos", 28, "Rio de Janeiro", "RJ", "Python para DS 2"),
    ("Mariana", 21, "Belo Horizonte", "MG", "Python para DS 1")
)
lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[2])  # Pega o terceiro elemento de cada tupla
print(lista)
# ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

# =========================================
# Exemplo 3: Reconstruindo tuplas com índice
# =========================================

lista_de_tuplas = (
    ("Júlia", 23, "São Paulo", "SP", "Python para DS 1"),
    ("Carlos", 28, "Rio de Janeiro", "RJ", "Python para DS 2"),
    ("Mariana", 21, "Belo Horizonte", "MG", "Python para DS 1")
)

# Cria uma lista apenas com as cidades (terceiro elemento)
lista = [tupla[2] for tupla in lista_de_tuplas]

# Cria uma nova lista de tuplas (índice, valor)
lista_com_indices = []
for i in range(len(lista)):
    lista_com_indices.append((i, lista[i]))  # tupla: (indice, cidade)

print(lista_com_indices)
# [(0, 'São Paulo'), (1, 'Rio de Janeiro'), (2, 'Belo Horizonte')]

# =========================================
# Exemplo 4: List comprehension com filtro
# =========================================

aluguel = [
    ("Apartamento", 2500),
    ("Casa", 3200),
    ("Apartamento", 2800),
    ("Kitnet", 1800),
    ("Apartamento", 3000),
]

lista = [tupla[1] for tupla in aluguel if tupla[0]== 'Apartamento']
print(lista)  # Pega somente os valores de "Apartamento"
# [2500, 2800, 3000]

# =========================================
# Exemplo 5: Dict comprehension simples
# =========================================

# Listas de meses e despesas correspondentes
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"]
despesa = [2500, 2700, 2900, 3100, 3300]

dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)  # Cria dicionário associando cada mês à despesa
# {'Janeiro': 2500, 'Fevereiro': 2700, 'Mar�o': 2900, 'Abril': 3100, 'Maio': 3300}

# =========================================
# Exemplo 6: List comprehension com múltiplas condições
# =========================================

vendas = [
    ('2021', 5000),
    ('2022', 7200),
    ('2022', 5900),
    ('2022', 8100),
    ('2023', 6400),
]

filtro = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]
print(filtro)  # Filtra vendas de 2022 maiores que 6000

# =========================================
# Exemplo 7: List comprehension com múltiplos if/else
# =========================================

glicemia = [65, 85, 110, 130, 70, 95, 125]

rotulos = [
    ('Hipoglicemia', glicose) if glicose <= 70
    else ('Normal', glicose) if glicose < 100
    else ('Alterada', glicose) if glicose < 125
    else ('Diabetes', glicose)
    for glicose in glicemia
]
print(rotulos)  # Rotula cada valor de glicemia

# =========================================
# Exemplo 8: Criando uma tabela com list comprehension
# =========================================

id = [1, 2, 3, 4]
quantidade = [10, 5, 3, 8]
preco = [12.5, 20.0, 15.0, 10.0]

tabela = [('id', 'quantidade', 'preco', 'total')]  # Cabeçalho
tabela += [
    (id[i], quantidade[i], preco[i], quantidade[i]*preco[i])
    for i in range(len(id))
]
# Cria tuplas com id, quantidade, preço e total
print(tabela)

# =========================================
# Exemplo 9: Trabalhando com sets para valores únicos
# =========================================

estados = ["SP", "RJ", "MG", "SP", "BA", "RJ", "RS"]
estados_unicos = list(set(estados))  # Remove duplicatas
print(estados_unicos)

# =========================================
# Exemplo 10: Lista de listas com valores repetidos de cada estado
# =========================================
lista_de_listas = []
for estado in estados_unicos:
    lista = [uf for uf in estados if uf == estado]  # Todos elementos iguais ao estado
    lista_de_listas.append(lista)
print(lista_de_listas)

# =========================================
# Exemplo 11: Dicionário com contagem de elementos por estado
# =========================================
contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(contagem_valores)

# =========================================
# Exemplo 12: Estados únicos de funcionários
# =========================================

funcionarios = [
    ("SP", 10),
    ("RJ", 7),
    ("MG", 4),
    ("SP", 3),
    ("BA", 5),
    ("RS", 2),
]

estados_unicos = list(set([tupla[0] for tupla in funcionarios]))  # Extrai estados sem repetição
print(estados_unicos)

# =========================================
# Exemplo 13: Lista de listas com funcionários por estado
# =========================================
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]  # Valores de cada estado
    lista_de_listas.append(lista)
print(lista_de_listas)

# =========================================
# Exemplo 14: Dicionário agrupando funcionários por estado
# =========================================
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamento_por_estado)

# =========================================
# Exemplo 15: Soma de funcionários por estado
# =========================================
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)