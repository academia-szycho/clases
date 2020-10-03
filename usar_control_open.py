from control_open import control_open
archivo_procesado = False
while not archivo_procesado:
    nombre_archivo = input("Ingrese archivo:")
    control_archivo = control_open(nombre_archivo)
    if len(control_archivo) == 0:
        # hacer algo
        archivo_procesado = True
    else:
        print(control_archivo)

print("Fin del programa.")