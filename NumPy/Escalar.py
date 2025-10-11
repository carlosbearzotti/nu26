import numpy as np

# Trabalhando com escalares e arrays
escalar = 5
array = np.array([1, 2, 3, 4, 5])

print("Escalar:", escalar)
print("Array:", array)

# Operações entre escalar e array
soma_escalar = array + escalar
multiplicacao_escalar = array * escalar
divisao_escalar = array / escalar
potencia_escalar = array ** escalar

print(f"\nArray + {escalar}:", soma_escalar)
print(f"Array * {escalar}:", multiplicacao_escalar)
print(f"Array / {escalar}:", divisao_escalar)
print(f"Array ** {escalar}:", potencia_escalar)

# Funções com escalares
array_float = np.array([1.5, 2.7, 3.1, 4.8, 5.2])
arredondado = np.round(array_float)
floor = np.floor(array_float)
ceil = np.ceil(array_float)

print(f"\nArray float: {array_float}")
print(f"Arredondado: {arredondado}")
print(f"Floor: {floor}")
print(f"Ceil: {ceil}")

# Criando arrays com valores específicos
zeros = np.zeros(5)
uns = np.ones(5)
sequencia = np.arange(0, 10, 2)  # De 0 a 10, passo 2
linear = np.linspace(0, 1, 5)   # 5 valores entre 0 e 1

print(f"\nZeros: {zeros}")
print(f"Uns: {uns}")
print(f"Sequência (0 a 10, passo 2): {sequencia}")
print(f"Valores lineares (0 a 1, 5 elementos): {linear}")

# Operações lógicas com escalar
maiores_que_3 = array > 3
print(f"\nArray: {array}")
print(f"Elementos > 3: {maiores_que_3}")
print(f"Elementos onde array > 3: {array[maiores_que_3]}")