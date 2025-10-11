import numpy as np

# Exemplos de broadcasting
# Broadcasting permite operações entre arrays de shapes diferentes

# Exemplo 1: Array 2D + escalar
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
resultado1 = matriz + 10
print("Matriz + 10:")
print(resultado1)

# Exemplo 2: Array 2D + array 1D (broadcasting na linha)
vetor_linha = np.array([1, 2, 3])
resultado2 = matriz + vetor_linha
print("\nMatriz + vetor linha [1,2,3]:")
print(resultado2)

# Exemplo 3: Array 2D + array 1D (broadcasting na coluna)
vetor_coluna = np.array([[1], [2], [3]])
resultado3 = matriz + vetor_coluna
print("\nMatriz + vetor coluna [[1],[2],[3]]:")
print(resultado3)

# Exemplo 4: Broadcasting em operações mais complexas
arr_3d = np.ones((2, 3, 4))  # Array 3D de uns
arr_1d = np.array([1, 2, 3, 4])  # Array 1D
resultado4 = arr_3d * arr_1d
print("\nArray 3D (2,3,4) * Array 1D (4,):")
print("Shape do resultado:", resultado4.shape)
print(resultado4)

# Exemplo 5: Broadcasting com condições
condicao = matriz > 5
resultado5 = np.where(condicao, matriz * 2, matriz)
print("\nElementos > 5 multiplicados por 2:")
print(resultado5)