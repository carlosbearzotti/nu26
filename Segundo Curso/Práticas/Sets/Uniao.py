lista_carros = {"Fiat", "Ford", "Chevrolet", "Toyota"}
carros = {"Honda", "Nissan", "Mazda", "Toyota"}

# Verificando se são disjuntos (sem elementos em comum)

lista_carros | carros

print(set.union(lista_carros, carros, {'Mazda'})) #adiciona o Mazda na saída