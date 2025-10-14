a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print(a+b+c)

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a-b)

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a*b)

numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador/denominador)

operador = int(input('Digite o operador valor: '))
potencia = int(input('Digite a potência valor: '))
print(operador**potencia)

numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador//denominador)

numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador%denominador)

nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
nota_3 = float(input('Digite a 3° nota: '))
print(f'Média {(nota_1+nota_2+nota_3)/3}.')

media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'Média {media_ponderada}.')