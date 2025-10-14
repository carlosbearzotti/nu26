objeto_zip = zip([1,2,3])
objeto_zip

list(objeto_zip)

id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

mapa = list(zip(id, regiao))
mapa

codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["maçã", "uva", "banana", "laranja"]

mercadorias = list(zip(codigos, frutas))
mercadorias

tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
ids, nomes  = zip(*tupla_iteravel)

ids = list(ids)
nomes = list(nomes)

print("IDs = ", ids)
print("Nomes = ", nomes)

# Pode combinar duas ou mais listas, tuplas, strings, etc. Ele junta os dados e transforma em tupla, quando o menor acaba ele encerra.