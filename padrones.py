padrones = {}

def agregar_alumno(padrones, nombre, apellido):
    numero_padron_nuevo = generar_numero_padron_nuevo(padrones)
    padrones[numero_padron_nuevo] = {"nombre": nombre, "apellido", apellido}

def generar_numero_padron_nuevo(padrones):
    padron = 0
    encontrado = False
    while not encontrado:
        if padron not in padrones.keys():
            nuevo_padron = padron
            encontrado = True
        else:
            padron = padron + 1
    return nuevo_padron