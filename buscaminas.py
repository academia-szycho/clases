
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

def crear_celda():
    return {
        "visible": False,
        "minada": False,
        "numero": None
    }

def generar_mapa(x, y):
    mapa = []
    for fila in range(x):
        nueva_fila = []
        for columna in range(y):
            nueva_fila.append(crear_celda())
        mapa.append(nueva_fila)
    return mapa

def dibujar_mapa(mapa):
    for columna in range(len(mapa[0])):
        print(f" {letras[columna]} ", end="")
    print("")
    for fila in mapa:
        for celda in fila:
            if celda["visible"]:
                if celda["minada"]:
                    print(" X ", end="")
                elif celda["numero"] is None:
                    print("| |", end="")
                else: # está visible y es un número
                    print(f" {celda['numero']} ", end="")
            else:
                print("[ ]", end="")
        print()  # imprimo un enter
    print("**********")

def aumentar_contador_celda(celda):
    if celda["numero"] is None:
        celda["numero"] = 1
    else:
        celda["numero"] += 1

def poner_bomba(mapa, x, y):
    try:
        celda = mapa[x][y]
        celda["minada"] = True
    except IndexError:
        print(f"No existe la celda {x}, {y} en el mapa.")
        return
    try:
        celda_superior_izquierda = mapa[x-1][y-1]
        aumentar_contador_celda(celda_superior_izquierda)
    except IndexError:
        pass
    try:
        celda_superior = mapa[x][y-1]
        aumentar_contador_celda(celda_superior)
    except IndexError:
        pass
    try:
        celda_superior_derecha = mapa[x+1][y-1]
        aumentar_contador_celda(celda_superior_derecha)
    except IndexError:
        pass
    try:
        celda_izquierda = mapa[x-1][y]
        aumentar_contador_celda(celda_izquierda)
    except IndexError:
        pass
    try:
        celda_derecha = mapa[x+1][y]
        aumentar_contador_celda(celda_derecha)
    except IndexError:
        pass
    try:
        celda_inferior_izquierda = mapa[x-1][y+1]
        aumentar_contador_celda(celda_inferior_izquierda)
    except IndexError:
        pass
    try:
        celda_inferior = mapa[x][y+1]
        aumentar_contador_celda(celda_inferior)
    except IndexError:
        pass
    try:
        celda_inferior_derecha = mapa[x+1][y+1]
        aumentar_contador_celda(celda_inferior_derecha)
    except IndexError:
        pass

def revelar_celda(mapa, x, y):
    try:
        celda = mapa[x][y]
        celda["visible"] = True
    except IndexError:
        print(f"No existe la celda {x}, {y} en el mapa.")
    