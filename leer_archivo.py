import os

dirname = os.path.dirname(__file__)
filename = "hola_que_tal.txt"

f = open(os.path.join(dirname, filename), "r")
# print(f.read())

print(f.readline())
print(f.readline())