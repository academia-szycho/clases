lista = ["banana", "manzana", "naranja", "naranja",
"banana", "manzana", "naranja", "naranja",
"banana", "manzana", "naranja", "naranja",
"banana", "manzana", "naranja", "naranja",]

frutas_sin_repetir = []

for fruta in lista:
    if fruta not in frutas_sin_repetir:
        frutas_sin_repetir.append(fruta)

for index, fruta in enumerate(frutas_sin_repetir):
    if fruta == "naranja":
        del frutas_sin_repetir[index]

print(frutas_sin_repetir)

conjunto = set(lista)
conjunto.remove("naranja")
print(list(conjunto))