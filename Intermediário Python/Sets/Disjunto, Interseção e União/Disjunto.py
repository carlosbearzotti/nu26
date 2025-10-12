lista_carros = {"Fiat", "Ford", "Chevrolet", "Toyota"}
carros = {"Honda", "Nissan", "Mazda", "Toyota"}

# Verificando se são disjuntos (sem elementos em comum)

# São iguais | (barra reta) e set.isdisjoint
print(set.isdisjoint(lista_carros, carros))
print(set.intersection(lista_carros, carros))