numero = [5] # Ej: 1028
multiplicador = 10 #

def multiplicar(a, b):
    # a = [0] # 1032
    a[0] = 25
    return a[0] * b

print(multiplicar(numero, multiplicador))
print(numero[0])
print(multiplicador)
print(multiplicar(numero, multiplicador))
