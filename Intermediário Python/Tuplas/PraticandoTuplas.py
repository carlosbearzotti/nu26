cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")
nome, idade, cidade, estado, turma = cadastro
print(cadastro[0]) # imprime Júlia
print(cadastro[-1]) # imprime Python para DS 1
print(f'A estudante {nome} tem {idade} anos e mora em {cidade}-{estado}. Ela está matriculada na turma de {turma}.')