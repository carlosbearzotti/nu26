import numpy as np

# Criando arrays unidimensionais
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Operações básicas
soma = arr1 + arr2
multiplicacao = arr1 * 2
potencia = arr1 ** 2
raiz_quadrada = np.sqrt(arr1)

print("\nSoma:", soma)
print("Multiplicação por 2:", multiplicacao)
print("Potência ao quadrado:", potencia)
print("Raiz quadrada:", raiz_quadrada)

# Funções estatísticas
print("\nMédia:", np.mean(arr1))
print("Desvio padrão:", np.std(arr1))
print("Valor máximo:", np.max(arr1))
print("Valor mínimo:", np.min(arr1))

# Fatiamento (slicing)
print("\nPrimeiros 3 elementos:", arr1[:3])
print("Últimos 2 elementos:", arr1[-2:])
print("Elementos do índice 1 ao 3:", arr1[1:4])