from intervalo import Intervalo

desde = input("Escriba el desde: ")
hasta = input("Escriba el hasta: ")
try:
    desde = int(desde)
    hasta = int(hasta)
    nuevo_intervalo = Intervalo(10,5)
except AssertionError as e:
    print(e)
except ValueError as e:
    print("Desde y hasta deben ser números enteros.")
