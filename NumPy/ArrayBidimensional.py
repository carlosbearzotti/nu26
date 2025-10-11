import numpy as np

# Criando arrays bidimensionais (matrizes)
matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)

# Operações matriciais
soma_matriz = matriz1 + matriz2
multiplicacao_elemento = matriz1 * matriz2
multiplicacao_matricial = np.dot(matriz1, matriz2)

print("\nSoma das matrizes:")
print(soma_matriz)
print("\nMultiplicação elemento a elemento:")
print(multiplicacao_elemento)
print("\nMultiplicação matricial:")
print(multiplicacao_matricial)

# Acessando elementos
print("\nElemento [1,2]:", matriz1[1, 2])
print("Primeira linha:", matriz1[0, :])
print("Segunda coluna:", matriz1[:, 1])

# Transposta e determinante
print("\nTransposta:")
print(matriz1.T)
print("Determinante:", np.linalg.det(matriz1))

# Resolvendo sistema linear
# Ax = b, onde A é a matriz e b é o vetor resultado
b = np.array([1, 2, 3])
x = np.linalg.solve(matriz1, b)
print(f"\nSolução do sistema Ax = b: {x}")