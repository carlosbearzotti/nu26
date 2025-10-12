# Coletamos os valores de início e fim
inicio = int(input('Insira o primeiro número inteiro: '))
fim = int(input('Insira o segundo número inteiro: '))

# Verificamos se o valor de início é maior que o fim
if inicio < fim:
  # podemos imprimir os inteiros entre o menor e o maior valor
  for i in range(inicio + 1, fim): 
    print(i)
elif inicio > fim:
  for i in range(fim + 1, inicio):
    print(i)
else: #caso os números sejam iguais, não conseguimos imprimir sequência alguma
  print('Os números são iguais.')

# número inicial de bactérias
colonia_a = 4
colonia_b = 10

# taxas de crescimento das colônias
taxa_a = 0.03
taxa_b = 0.015

# contador de dias
dias = 0

# A condição que finaliza o laço é o caso em que
# a colônia A ultrapasse a colônia B
while colonia_a <= colonia_b:
  # usamos um operador de atribuição com multiplicação
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  # contamos o dia para cada iteração
  dias += 1

# resultado final
print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')

# laço para pegar as 15 notas
for i in range(15):
  nota = float(input(f'Insira a nota da pessoa usuária {i}: '))

  # verifica se a nota está entre 0 e 5
  # se estiver, o laço rodará ininterruptamente até ser obtido um valor válido
  while (nota < 0) or (nota > 5):
    nota = float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))

print('Verificação feita. Todas as notas são válidas')

# coletamos a temperatura
temperatura = float(input('Insira a temperatura em Celsius: '))

# inicializamos uma contadora e soma para a média
contadora = 0
soma = 0

# nosso código executa sempre até o valor de temperatura for igual a -273
while temperatura != -273:
    # a soma é dada com a adição da temperatura à variavel soma
    soma += temperatura
    # contamos a quantidade de valores coletados através da contadora
    contadora += 1
    # coletamos novamente a temperatura
    temperatura = float(input('Insira a temperatura em Celsius: '))

media = soma / contadora

print(f'A média das temperaturas é: {media}')

# Pedir o número
num = int(input('Informe um número inteiro: '))

# Inicializar o cálculo
fatorial = 1

# nosso contador inicializa com o número máximo
# e será feita uma contagem decrescente com o operador -=
i = num
while i > 0:
    # queremos multiplicar agora o valor do fatorial pelo num
    # e todos os números abaixo dele até 1
    fatorial *= i
    i -= 1

# Imprimir o cálculo do fatorial
print(f'Fatorial de {num} é {fatorial}')

# Pedir o número
num = int(input('Informe um número inteiro de 1 a 10: '))

# Vamos gerar a tabuada
print(f'Tabuada do {num}:')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

    # Solicitamos o número
num = int(input("Digite o número: "))

# Assumimos que o número é primo até que se prove o contrário
eh_primo = True

# Números abaixo de 2 não são primos
if num <= 1 :
  eh_primo = False
else:
    for i in range(2, num):
        # Se o número for divisível por qualquer número dentro deste intervalo,
        # ele não é primo, portanto, mudamos a variável 'eh_primo' para False e saímos do loop.
        if num % i == 0:
            eh_primo = False
            break
  
# Verifica se 'eh_primo' ainda é True, o que significa que o número passou pelo loop
# sem ser divisível por nenhum número além de 1 e ele mesmo.
if eh_primo:
    # Se for o caso, o número é primo.
    print(f'O número {num} é primo')
else:
    # Caso contrário, o número não é primo.
    print(f'O número {num} não é primo')

# Coletamos as idades dos clientes
idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

# Inicializamos as variáveis de contadores
contador_0_25 = 0 # contador de idades entre 0 e 25
contador_26_50 = 0 # contador de idades entre 26 e 50
contador_51_75 = 0 # contador de idades entre 51 e 75
contador_76_100 = 0 # contador de idades entre 76 e 100

# nosso código executa sempre até o valor de idade for negativa
while idade >= 0:
    # contamos cada caso
    if idade >= 0 and idade <= 25:
        contador_0_25 += 1
    elif idade >= 26 and idade <= 50:
        contador_26_50 += 1
    elif idade >= 51 and idade <= 75:
        contador_51_75 += 1
    elif idade >= 76 and idade <= 100:
        contador_76_100 += 1
    
    # Repetir o processo de entrada de dados até que seja digitado um número negativo    
    idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

# Mostramos os resultados
print('Distribuição de idades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)

# Inicializamos as variáveis contadoras
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_branco = 0

# Início do laço para ler os votos
for i in range(0,20):
    voto = int(input('Informe seu voto: '))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Voto inválido.")

print(f'Votos candidato 1: {votos_candidato1}')
print(f'Votos candidato 2: {votos_candidato2}')
print(f'Votos candidato 3: {votos_candidato3}')
print(f'Votos candidato 4: {votos_candidato4}')
print(f'Votos nulos: {votos_nulos}')
print(f'Votos em branco: {votos_branco}')
print(f'Percentual de votos nulos: {(votos_nulos / 20 * 100)}')
print(f'Percentual de votos em branco: {(votos_branco / 20 * 100)}')