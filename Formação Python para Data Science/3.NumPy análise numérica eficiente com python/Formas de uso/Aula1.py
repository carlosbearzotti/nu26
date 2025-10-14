import numpy as np
import matplotlib.pyplot as plt

ano_inicial = 2002
ano_final = 2102
np.arange(ano_inicial, ano_final + 1, 4)

import numpy as np

# cria uma lista
lista = [1, 2, 3, 4, 5]

# transforma a lista em um array Numpy
array = np.array(lista)

print("Lista: ", lista)
print("Array: ", array)

import numpy as np
import time

# cria uma lista com 1000000 elementos
lista = list(range(1000000))

# transforma a lista em um array Numpy
array = np.array(lista)

# começa a cronometrar o tempo para a operação com a lista
start_time = time.time()

# realiza a operação de elevar ao quadrado cada elemento da lista
lista_quadrado = [i**2 for i in lista]

# para o cronômetro
list_time = time.time() - start_time

# começa a cronometrar o tempo para a operação com o array
start_time = time.time()

# realiza a operação de elevar ao quadrado cada elemento do array
array_quadrado = array**2

# para o cronômetro
array_time = time.time() - start_time

print("Tempo da operação com a lista: ", list_time)
print("Tempo da operação com o array: ", array_time)

dado = 0
diametro_laranja = dado[:5000,0]
diametro_toranja = dado[5000:,0]
peso_laranja = dado[:5000,1]
peso_toranja = dado[5000:,1]



plt.plot(diametro_laranja, peso_laranja)
plt.plot(diametro_toranja, peso_toranja)

Y = peso_laranja
X = diametro_laranja
n = np.size(X)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2)
b = np.mean(Y) - a*np.mean(X)

norma = np.array([])
np.random.seed(84)
coef_angulares = np.random.uniform(low=0.0,high=30.0,size=100)

for i in range(100):
  norma = np.append(norma,np.linalg.norm(Y- (coef_angulares[i]*X+b)))