import os

dirname = os.path.dirname(__file__)
# filename = "nombres.csv"
filename = "cuentas.csv"
try:
    f = open(os.path.join(dirname, filename), "r")
except FileNotFoundError:
    print("archivo no encontrado")
    exit()

try: 
    encabezado = []
    encabezado.append(f.readline().split(","))

    cuentas = []
    (numerador, divisor) = f.readline().split(",")
    cuentas.append((numerador, divisor))

    (numerador, divisor) = f.readline().split(",")
    cuentas.append((numerador, divisor))

    for resultado in cuentas:
        print(f"Resultado: {float(resultado[0])/float(resultado[1])}.")
    
    print("Corrió todo bien")

except ValueError as e:
    print("Error de valores: revise que el archivo tenga 3 líneas como mínimo.")
finally:
    print("Terminé el procesamiento del archivo")

print("Terminé el procesamiento del archivo")

print("Fin de programa.")