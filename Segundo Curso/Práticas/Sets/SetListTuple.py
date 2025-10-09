import time

elementos_set = set(range(10000))
elementos_list = list(range(10000))
elementos_tuple = tuple(range(10000))

def verifica_elemento_in(elemento_iteravel):
    
    for i in range (10000):
        if i in elemento_iteravel:
            pass

print('Tempo de exec set:')
inicio = time.time()
verifica_elemento_in(elementos_set)
fim = time.time()
print(f"{fim - inicio:.6f} segundos")
print('=' * 30)

print('Tempo de exec list:')
inicio = time.time()
verifica_elemento_in(elementos_list)
fim = time.time()
print(f"{fim - inicio:.6f} segundos")
print('=' * 30)

print('Tempo de exec tuple:')
inicio = time.time()
verifica_elemento_in(elementos_tuple)
fim = time.time()
print(f"{fim - inicio:.6f} segundos")
print('=' * 30)

#set é muito mais otimizado mais ou menos 600%-