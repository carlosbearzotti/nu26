lista_carros = {"Fiat", "Ford", "Chevrolet", "Toyota"}
carros = {"Honda", "Nissan", "Mazda", "a"}

# Verificando se são disjuntos (sem elementos em comum)

lista_carros & carros
# São iguais & (e comercial) e set.intersection
print(set.intersection(lista_carros, carros))
print(set.isdisjoint(lista_carros, carros))