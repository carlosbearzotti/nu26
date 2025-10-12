# Buscando dados dentro da Tupla, conjunto de dados ordenado e imutável
cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")
nome, idade, cidade, estado, turma = cadastro
print(cadastro[0]) # imprime Júlia
print(cadastro[-1]) # imprime Python para DS 1
print(f'A estudante {nome} tem {idade} anos e mora em {cidade}-{estado}. Ela está matriculada na turma de {turma}.')

#Trabalhando dados dentro da tupla
notas_aluno = ("João", 8.0, 9.0, 10.0)
nome, n1, n2, n3 = notas_aluno  # Desempacotamento, define nome = nome e notas como nx (n1, n2, n3)
media = (n1 + n2 + n3) / 3
print(f"{nome} → Média: {media:.2f}")