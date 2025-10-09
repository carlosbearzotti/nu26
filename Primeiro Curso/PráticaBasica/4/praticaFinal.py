# Dados de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Calculamos a média encontrando o valor total de gastos com sum
# e a quantidade total de compras realizadas com len
total_gastos = sum(gastos)
quantidade_compras = len(gastos)
media_gastos = total_gastos / quantidade_compras
# Resultado
print(f'A média de gastos é {media_gastos} reais.')

# Dados de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Variável que vai contar quantas compras foram feitas acima de 3000
contador_acima_3000 = 0
# Usamos o laço para ler a lista de gastos
for gasto in gastos:
  # Verificamos se o elemento está acima de 3000
  if gasto > 3000:
    # Acrescentamos mais um no contador, caso tenha algum valor acima de 3000
    contador_acima_3000 += 1
    
# Quantidade Compras
# Variável que vai ser utilizada para o cálculo da porcentagem
quantidade_compras = len(gastos)	


# Com a contagem conseguimos calcular a porcentagem de valores acima de 3000 entre todas as compras
porcentagem_acima_3000 = 100 * (contador_acima_3000) / (quantidade_compras) 

# Resultado
print(f'{contador_acima_3000} compras foram acima de R$3000,00.')
print(f'{porcentagem_acima_3000}% dos gastos foram acima de R$3000,00.')

# Lista que irá armazenar os 5 números inteiros
lista_numeros = []

# Criamos um laço que vai iterar 5 vezes para receber os 5 números
for i in range(0, 5):
  # Coletamos o valor e inserimos na lista por 5 vezes
  numero = int(input('Digite um número inteiro: '))
  lista_numeros.append(numero)
#Resultado
print(f'Lista de números inseridos: {lista_numeros}')

# Lista que irá armazenar os 5 números inteiros
lista_numeros = []

# Criamos um laço que vai iterar 5 vezes para receber os 5 números
for i in range(0, 5):
  # Coletamos o valor e inserimos na lista por 5 vezes
  numero = int(input('Digite um número inteiro: '))
  lista_numeros.append(numero)
# Usamos da lógica de partição para imprimir o resultado
print(f'Lista de números invertida: {lista_numeros[::-1]}')

# Coletamos o números
numero = int(input('Digite um número inteiro: '))
# Lista para receber os números primos
lista_primos = []
# Laço que vai rodar por todos os números abaixo do número digitado
for num in range(2, numero):
  # Primo é uma bandeira, ela permite sabermos se o valor analisado é ou não primo
  primo = True 
  # Testamos se todos os números abaixo do especificado no primeiro laço podem
  # gerar uma divisão exata
  for teste_divisiveis in range(2, num):
    if num % teste_divisiveis == 0:
      # Caso seja divisivel por algum número entendemos que 
      # o num não é primo e finalizamos o laço interno com break
      primo = False
      break
  # A condição se torna o resultado booleno de primo: False, ignoramos o condicional
  # True, executamos o bloco do if
  if primo:
    lista_primos.append(num)
# Resultado
print(f'Lista de números primos: {lista_primos}')

# Coletamos a data
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

# Análise de fevereiro
if mes == 2:
  # Verificamos se é ou não um ano bissexto
  if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    dias_fevereiro = 29
  else:
    dias_fevereiro = 28
  # Verificamos se o dia colocado corresponde ao máximo de dias de fevereiro
  if dia >= 1 and dia <= dias_fevereiro:
    print('Data válida')
  else:
    print('Data inválida')
# Verificamos meses terminados em 31 dias
elif mes in [1, 3, 5, 7, 8, 10, 12]:
  if dia >= 1 and dia <= 31:
    print('Data válida')
  else:
    print('Data inválida')
# Verificamos meses terminados em 30 dias
elif mes in [4, 6, 9, 11]:
  if dia >= 1 and dia <= 30:
    print('Data válida')
  else:
    print('Data inválida')
# Caso o mês não esteja entre 1 e 12
else:
  print('Data inválida')

  # Lista de crescimento das bactérias
bacterias_colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
# Lista que irá armazenar as porcentagens de crescimento
porcentagem_crescimento = []
# Vamos percorrer os índices de 1 a 9 para compararmos o valor atual com o passado
for i in range(1, len(bacterias_colonia)):
  # seguimos o cálculo 100 * (amostra_atual - amostra_passada) / (amostra_passada)
  porcentagem = 100 * (bacterias_colonia[i] - bacterias_colonia[i-1]) / (bacterias_colonia[i-1])
  # adicionamos o resultado na lista porcentagem_crescimento
  porcentagem_crescimento.append(porcentagem)
# Resultado
print(f'Porcentagens de crescimento:\n{porcentagem_crescimento}')

# Lista que vai receber os valores de IDs
ids = []
# Variáveis contadoras de doces e amargos
doce = 0
amargo = 0

# Criamos um laço que vai iterar 10 vezes para receber os 10 IDs
for i in range(0,10):
  # Coletamos o ID e adicionamos o id na lista
  ids.append(int(input(f'Digite o {i+1}° ID: ')))

# Ler todos os elementos da lista ids e atribuir à id
for id in ids:
  # Verificamos se os elementos são pares ou ímpares para fazer a contagem
  if id % 2 == 0:
    doce += 1
  else:
    amargo += 1

# Resultado
print(f'Quantidade de produtos doces: {doce}')
print(f'Quantidade de produtos amargos: {amargo}')

# Inicializamos os dados
respostas = [] # Lista para receber as respostas
# Lista de gabaritos
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0 # Irá acumular a nota total

# Recebemos as respostas do aluno
for i in range(0, 10):
  respostas.append(input(f'Insira a resposta da questão {i + 1}: ').upper())

# Verificamos se as respostas são iguais e adicionamos à nota
for i in range(0,10):
  if respostas[i] == gabarito[i]:
    nota += 1

# Exibindo nota final
print(f'Nota final: {nota}')

# Coletamos a lista de temperaturas
temperaturas_mensais = []
for i in range(0,12):
  temperaturas_mensais.append(float(input(f'Digite a média de temperatura do mês {i+1}: ')))
# Criamos uma lista auxiliar para os nomes dos meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# Calculamos a média
media_anual = sum(temperaturas_mensais) / len(temperaturas_mensais)

#Resultado
print('Temperaturas acima da média em: ')
for i in range(0,12):
  # Verificamos todas as temperaturas de acordo com a média anual
  if temperaturas_mensais[i] > media_anual:
    # Como os índices dos meses correspondem às temperaturas,
    # podemos imprimir eles sob o mesmo índice
    print(meses[i])

    # Dicionário de vendas
dados_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

# Inicializamos as variáveis
total_vendas = 0 # Irá somar todos as vendas
produto_mais_vendido = '' # Irá armazenar o nome do produto mais vendido
unidades_produto_mais_vendido = 0 # Irá armazenar a maior quantidade vendas

# Percorremos os valores de chaves e elementos do dicionário
for produto in dados_vendas.keys():
  # Somamos o total de vendas 
  total_vendas += dados_vendas[produto]
  # Verificamos se valor de venda atual desing (dados_vendas[produto]) é maior que o valor armazenado em unidades_produto_mais_vendido
  # Cada vez que dados_vendas[produto] superar o valor em unidades_produto_mais_vendido, 
  # a variável unidades_produto_mais_vendido vai ser igual à dados_vendas[produto], atribuindo um novo valor
  # De forma similar, produto_mais_vendido também é substituído pelo produto atual
  if dados_vendas[produto] > unidades_produto_mais_vendido:
    unidades_produto_mais_vendido = dados_vendas[produto]
    produto_mais_vendido = produto
# Resultados
print(f'Total de vendas é {total_vendas}')
print(f'{produto_mais_vendido} é o mais vendido')

# Dicionário de votos por design
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

# Inicializamos as variáveis
total_votos = 0 # Irá somar todos os votos 
vencedor = '' # Irá armazenar o nome do design vencedor
voto_vencedor = 0 # Irá armazenar a quantidade vencedora de votos

# Percorremos os valores de chaves e elementos do dicionário
for design, voto_desing in votos.items():
  # Somamos o total de votos
  total_votos += voto_desing
  # Verificamos se o voto do atual desing (voto_desing) é maior que o valor armazenado em voto_vencedor
  # Cada vez que voto_desing superar o valor em voto_vencedor, 
  # a variável voto_vencedor vai ser igual à voto_desing, atribuindo um novo valor
  # De forma similar, o vencedor também é substituído pelo design
  if voto_desing > voto_vencedor:
    voto_vencedor = voto_desing
    vencedor = design
# Calculamos a porcentagem do design vencedor
porcentagem = 100 * (voto_vencedor) / (total_votos)

#Resultado
print(f'{vencedor} é o vencedor: ')
print(f'Porcentagem de votos: {porcentagem}%')

# Lista de salários
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# Inicializamos as variáveis
dic_abonos = {} # Dicionário de abonos
total_abono = 0 # Irá somar todos os gastos com abono
abonos_minimo = 0 # Irá armazenar a quantidade de abonos mínimos 
maior_abono = 0 # Irá armazenar o maior valor de abono 

# Percorremos toda a lista de salários
for salario in salarios:
  # Calculamos o valor teórico de abono
  abono = salario * 0.1
  # Caso o abono seja inferior a 200,
  # ajustamos o valor de abono para o mínimo (200)
  if abono < 200:
    abono = 200
  # Adicionamos um novo dado no dicionário chave abono
  dic_abonos[salario] = abono

# Percorremos todos os valores do dicionário de abonos
for abono in dic_abonos.values():
  # Contamos o salário minimo
  if abono == 200:
    abonos_minimo += 1
  # Verificamos se o abono lido é maior que o valor armazenado em maior_abono
  # Cada vez que o abono superar o valor de maior_abono, 
  # a variável maior_abono vai ser igual à abono, atribuindo um novo valor
  if abono > maior_abono:
    maior_abono = abono
  # Somamos os abonos
  total_abono += abono
# Resultados
print(f'Abonos: {dic_abonos}')
print(f'Total de gasto com abonos: {total_abono}')
print(f'Número de funcionários que receberam o abono mínimo: {abonos_minimo}')
print(f'Maior valor de abono: {maior_abono}')

# Especificamos os dados para um dicionário
dados = {'Área Norte': [2819, 7236],
         'Área Leste': [1440, 9492],
         'Área Sul': [5969, 7496],
         'Área Oeste': [14446, 49688],
         'Área Centro': [22558, 45148]}
# Inicializamos as variáveis
soma_media = 0 # Irá somar todas as médias
maior_diversidade = '' # Irá armazenar a área com maior diversidade
maior_soma = 0 # Irá armazenar a maior soma de espécies 
# Percorremos os valores de chaves e elementos do dicionário
for area, especies in dados.items():
  # Fazemos a soma do números de espécies em cada área com a função sum
  soma_especies = sum(especies)
  # Calculamos a média dividindo a soma das espécies pela quantidade de espécies
  media = soma_especies / len(especies)
  # Imprimimos
  print(f'A {area} tem a média de {media} espécies')
  # Verificamos se a soma das espécies é maior que o valor armazenado de maior_soma
  # Cada vez que a soma_especies superar o valor de maior_soma, 
  # a variável maior_soma vai ser igual à soma_especies, atribuindo um novo valor
  # De forma similar, maior_diversidade também é substituída
  if soma_especies > maior_soma:
      maior_soma = soma_especies
      maior_diversidade = area
  # Somamos as médias
  soma_media += media
# A média total será dada pela soma_media dividida pela quantidade de áreas
media_total = soma_media / len(dados)
print(f'Média geral de espécies: {media_total}')
print(f'Área com a maior diversidade biológica: {maior_diversidade}')

# Especificamos os dados para um dicionário
dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Inicializamos a variável que irá somar todas as idades
total_idades = 0
# Percorremos os valores de chaves e elementos do dicionário
for setor, idades in dados.items():
  # Calculamos a média dividindo a soma das idades pela quantidade funcionários em cada setor
  media_idade = sum(idades) / len(idades)
  # Imprimimos
  print(f'O {setor} tem a média de {media_idade}')
  # Somamos as médias
  total_idades += sum(idades)
# A média total será dada pela total_idades dividida pela quantidade de pessoas totais (setores * funcionários por setor)
media_total = total_idades / (len(idades) * len(dados))
print(f'A média de idade geral é {media_total}')

# Inicializamos a variável que irá contar todas pessoas com idade acima da média
acima_media = 0
# Percorremos novamente os valores de chaves e elementos do dicionário
for setor, idades in dados.items():
  # Lemos os elementos (idades) dentro de cada lista de idades no dicionário
  for id in idades:
    # Verificamos se o valor da idade é superior à média total
    if id > media_total:
      # Caso o valor da idade seja superior à média, incrementamos mais um no contador
      acima_media += 1
# Resultado
print(f'{acima_media} pessoas estão acima da idade média geral')