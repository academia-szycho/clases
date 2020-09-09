s = "ejemplo"
print("1er id: ", id(s))
s = "otro"
print("2do id: ", id(s))

print(s[1])

s = "153"
print("3er id: ", id(s))
print(s[2])

# s[2] = "5"
# print(s[2])

numero = 5
print("1er id numero: ", id(numero))
numero2 = numero
print("2do id numero: ", id(numero))

lista = [0, 1, 3]

def no_cambia_lista(lista_recibida):
    lista_recibida = [4, 5, 6]
    print("lista interna:", lista_recibida)

no_cambia_lista(lista)
print(lista)    

def append_lista(lista_recibida):
    lista_recibida.append(100)

append_lista(lista)
print(lista)

def cambia_lista(otra_lista):
    """
    Modifica el valor de la posición 0 pisándolo por el valor de la posición 1 multiplicado por 5

    Parameters:
    otra_lista (list): una lista con mínimo 2 elementos

    Returns:
    list: 
    """
    otra_lista[0] = otra_lista[1] * 5

cambia_lista(lista)
print(lista)

