from buscaminas import *

mapa = generar_mapa(10,10)
dibujar_mapa(mapa)
poner_bomba(mapa, 2, 2)
dibujar_mapa(mapa)
revelar_celda(mapa, 2, 1)
dibujar_mapa(mapa)

accion = None
estado = "en juego"
while accion != "terminar" and estado == "en juego":
    accion = preguntar_accion()
    if accion == "revelar":
        posicion = preguntar_posicion()
        revelar_celda(mapa, posicion[0], posicion[1])
        dibujar_mapa(mapa)
        estado = evaluar_situacion(mapa)

if estado == "gano":
    print("ganaste")
else:
    print("perdiste")