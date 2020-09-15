import os

dirname = os.path.dirname(__file__)
filename = "perro.png"

with open(os.path.join(dirname, filename), "rb") as f:
    # print(f.read())

    for line in f.readlines():
        print(line, end="")