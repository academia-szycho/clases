# EJERCICIO 1 PYTHON OSCAR VASTA
# UN PROGRAMA QUE PIDE AL USUARIO 3 NÚMEROS Y LOS GUARDA EN UN ARRAY
""" eso sería para inicializar el arreglo en 3 elementos nulos si fuera necesario:
 arreglo = [0 for numero in range(3)] """
cont = 0
numeroleido=0
arreglo = []
while cont <= 2:
    print(arreglo)
    valor = input("ingrese un número")
    numeroleido = int(valor)
    arreglo.append(numeroleido)
    print(numeroleido)
    cont = cont + 1



