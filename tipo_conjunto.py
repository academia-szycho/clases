lista = ["banana", "manzana", "naranja", "naranja"]

frutas_sin_repetir = set(lista)
'''
for fruta in lista:
    if fruta not in frutas_sin_repetir:
        frutas_sin_repetir.append(fruta)
'''
print(frutas_sin_repetir)

frutas_sin_repetir = {"naranja", "frutilla"}
print(frutas_sin_repetir)

frutas_sin_repetir.remove("naranja")
print(frutas_sin_repetir)