import os

directorio = os.path.dirname(__file__)

def control_open(archivo):
    try:
        nombre_archivo = os.path.join(directorio, archivo)
        f = open(nombre_archivo,'r')
    except FileNotFoundError as err:
        return "FileNotFoundError: {}".format(nombre_archivo)
    except IOError as err:
        return '=======',"IO error: {}".format(err),'======='
    f.close()
    return ""