import numpy as np

# Criando array 3D (exemplo: 3 matrizes 2x3)
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], 
                   [[7, 8, 9], [10, 11, 12]], 
                   [[13, 14, 15], [16, 17, 18]]])

print("Array 3D shape:", arr_3d.shape)
print("Array 3D:")
print(arr_3d)

# Acessando elementos em 3D
print("\nPrimeira matriz 2D:")
print(arr_3d[0])
print("\nSegunda linha da primeira matriz:")
print(arr_3d[0, 1])
print("\nElemento [1, 0, 2]:", arr_3d[1, 0, 2])

# Operações em arrays N-dimensionais
soma_3d = arr_3d + 10
media_por_matriz = np.mean(arr_3d, axis=0)
soma_por_linha = np.sum(arr_3d, axis=1)
soma_por_coluna = np.sum(arr_3d, axis=2)

print("\nArray + 10:")
print(soma_3d)
print("\nMédia por matriz (axis=0):")
print(media_por_matriz)
print("\nSoma por linha (axis=1):")
print(soma_por_linha)
print("\nSoma por coluna (axis=2):")
print(soma_por_coluna)

# Redimensionando
arr_reshape = arr_3d.reshape(2, 9)
print("\nArray redimensionado para 2x9:")
print(arr_reshape)