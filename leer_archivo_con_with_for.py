import os

dirname = os.path.dirname(__file__)
filename = "hola_que_tal.txt"

with open(os.path.join(dirname, filename), "r") as f:
    # print(f.read())

    for line in f.readlines():
        print(line, end="")