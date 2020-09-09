lista = [1, 2, 3, 8, 9]

print("lista")
print(lista)
print("primer elemento de la lista:")
print(lista[0])

seis = "seis"

tupla = (1, 4, 8, 0, 5, seis)
print("tupla")
print(tupla)
print("El primer elemento de la tupla:")
print(tupla[0])

print("id:")
print(id(tupla))

# lista[0] = 5
# print("lista")
# print(lista)

tupla = tupla + (99,)
print("tupla")
print(tupla)
print("id:")
print(id(tupla))

nueva_lista = list(tupla)
nueva_lista[0] = 99
tupla = tuple(nueva_lista)
print("tupla")
print(tupla)
print("id:")
print(id(tupla))
