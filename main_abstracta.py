from clase_abstracta import Ave, Perico, Aguila

aves = []

for i in range(10):
    if i % 2 == 0:
        ave = Perico()
        aves.append(ave)
    else:
        ave = Aguila()
        aves.append(ave)

for i in range(5):
    for ave in aves:
        ave.vuela()
        ave.mostrar_posicion()
    print("---------------")
