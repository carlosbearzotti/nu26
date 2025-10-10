nome = "Ana Maria"
idade = 17
print(f"O nome da aluna é {nome} e sua idade é {idade} anos.")

nome_aluno = 'Fabricio Daniel'

print('Nome do aluno: %s' %(nome_aluno))

nome_aluno2 = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno2, idade_aluno, media_aluno))

x = True
print("Valor de x: %s" % str(x))

nome_aluno3 = 'Fabricio Daniel'

print('Nome do aluno: {}'.format(nome_aluno3))

nome_aluno4 = 'Fabricio Daniel'
idade_aluno2 = 15
media_aluno2 = 8.45

print('Nome do aluno é {}, ele tem {} anos e sua média é {}.' .format(nome_aluno4, idade_aluno2, media_aluno2))

#\n é o caractere de nova linha e é usado para pular uma linha no texto (função do Enter)
print("Estudar é um esforço constante,\nÉ como cultivar uma planta,\nPrecisamos de dedicação e paciência,\nPara ver o fruto amadurecer.")
#\t é o caractere de tabulação usado para adicionar um espaço de tabulação no texto.
print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')
#\\ é usado para imprimir uma única barra invertida. Caso não seja usada a dupla barra invertida, o código poderá resultar em erro ou em um resultado inesperado, pois o Python considera a \ um chamado para um caractere especial. Usamos esta sintaxe para garantir que não ocorram erros
print("Caminho do arquivo: C:\\arquivos\\documento.csv")
#\" é usado para imprimir aspas duplas quando estamos trabalhando com uma string criada a partir de aspas duplas ". Porém, isso não é necessário caso seja uma string criada por aspas simples '.
print("Ouvi uma vez \"Os frutos do conhecimento são os mais doces e duradouros de todos.\"")
#\' é usado para imprimir aspas simples quando estamos trabalhando com uma string criada a partir de aspas simples '. Caso seja uma string criada por aspas duplas ", isso não é necessário.
print('Minha professora uma vez disse \'Estudar é a chave do sucesso.\' ')