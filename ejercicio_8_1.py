"""
Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:

a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
tidad de coincidencias encontradas.
"""

from contar_coincidencias import contar_coincidencias

lista = [ 7, 8, 4, 2, 4.7, 0, 10, 0]
elemento = 0

coincidencias_encontradas = contar_coincidencias(lista, elemento)

print(coincidencias_encontradas)

