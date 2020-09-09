# EJERCICIO 1 PYTHON OSCAR VASTA
# UN PROGRAMA QUE PIDE AL USUARIO 3 NÚMEROS Y LOS GUARDA EN UN ARRAY
""" eso sería para inicializar el arreglo en 3 elementos nulos si fuera necesario:
 arreglo = [0 for numero in range(3)] """
cont = 0
numero_leido=0
arreglo = []
while cont <= 2:
    print(arreglo)
    valor = input("ingrese un número")
    numero_leido = int(valor)
    arreglo.append(numero_leido)
    print(numero_leido)
    cont = cont + 1



