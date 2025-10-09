#Sets a partir de arrays

carros = {"Honda", "Nissan", "Mazda", "Toyota"}

'Honda' in carros # Testa se Honda esta dentro

print(carros)

for i in carros:
    print(i)

carrosEmotos = {10, "b", 31,2, True}
print(carrosEmotos)

for i in carrosEmotos:
    print(i)

#Sets a partir de Listas

lista_carros = {"Fiat", "Ford", "Chevrolet", "Toyota"}
 
carros_set = set(lista_carros)
print(carros_set)