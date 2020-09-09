alumno = {
    "nombre": "Gabo",
    "apellido": "Lato",
    "email": "saraza@massaraza.com",
    "dni": "444567789",
    # 0: ""
}

print(alumno["nombre"])

alumno["nombre"] = "Plofi"

print(alumno["nombre"])

alumno["direccion"] = "calle falsa 123"

print(alumno)

print(alumno.keys())

for clave in alumno.keys():
    print(clave, alumno[clave])


alumno1 = {
    "nombre": "Plofi",
    "apellido": "Lato",
    "email": "saraza@massaraza.com",
    "dni": "444567789",
    "edad": 33
    # 0: ""
}    

alumno2 = {
    "nombre": "Gabo",
    "apellido": "Lato",
    "email": "saraza@menosaraza.com",
    "dni": "444567789",
    # 0: ""
}

alumnos = [alumno1, alumno2]

print(alumnos)


padrones = {
    10766: alumno1,
    7: alumno2 
}

print(padrones)

padrones[778] = {
    "nombre": "Homero"
}

alumno_encontrado = padrones.get(778, "No encontrado")

print(alumno_encontrado)

# padrones.set(233, {"nombre": "Lisa"})  # No funciona
padrones[233] = {"nombre": "Lisa"}

print(padrones)