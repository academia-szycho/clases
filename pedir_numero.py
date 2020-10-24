"""
Ejercicio 6.9. Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido,
la función lo debe devolver.
Ejemplo:
z = pedir_entero("¿Cuál es tu número favorito?", -50, 50)
¿Cuál es tu número favorito? [-50..50]:
10
Por favor ingresa un número entre -50 y 50.
"""
def centinela(numero, minimo, maximo):
    numero = input(f"Por favor ingresa un número entero entre {minimo} y {maximo}:")
    return numero

def pedir_entero(mensaje, minimo, maximo):
    """
    Devuelve un mensaje ingresado y el número entero ingresado por el usuario.
        Parameters:
                (str) Un mensaje para el usuario.
                (int) El valor mínimo y el máximo entre los que debe 
                estar el número entero solicitado al usuario.
                (int) El número entero ingresado por el usuario.
        
        Returns: El número entero ingresado si está entre los parámetros indicados,
                o una cadena que indica que lo vuelva a ingresar indefinidamente.
    """
    mensaje = f"{mensaje} [{minimo}..{maximo}]:"
    numero = None
    while numero is None or numero < minimo or numero > maximo:
        try:
            texto_ingresado = input(mensaje)
            numero = int(texto_ingresado)
        except Exception:
            pass
            
    return numero

#Ej.
print(pedir_entero("¿Cuál es tu número favorito?",-50,50))