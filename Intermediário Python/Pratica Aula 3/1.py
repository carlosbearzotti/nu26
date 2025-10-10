for lista in lista_de_listas:
    print(sum(lista))
    lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[2])
print(lista)

lista_de_tuplas = []
for i in range(len(lista)):
    lista_de_tuplas.append((i, lista[i]))
print(lista_de_tuplas)

lista = [tupla[1] for tupla in aluguel if tupla[0]== 'Apartamento']
print(lista)

dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)

filtro = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]
print(filtro)

rotulos = [('Hipoglicemia', glicose) if glicose <= 70 else ('Normal', glicose) if glicose < 100 else ('Alterada', glicose) if glicose < 125 else ('Diabetes', glicose) for glicose in glicemia]
print(rotulos)

tabela = [('id', 'quantidade', 'preco', 'total')]
tabela += [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]

# Armazenando os estados sem repetição de valor
estados_unicos = list(set(estados))

# Criando uma lista de listas com valores repetidos de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [uf for uf in estados if uf == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário em que a chave é o nome de cada estado único e o valor é a contagem de elementos
contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(contagem_valores)

# Armazenando os estados sem repetição de valor
estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

# Criando uma lista de listas com valores de funcionários de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário com dados agrupados de funcionário por estado
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamento_por_estado)

# Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)