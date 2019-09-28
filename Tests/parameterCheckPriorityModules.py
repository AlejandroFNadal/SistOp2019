from Clases.Procesos import *


def checker(lista_entrada,funcion):
    
    resultado=funcion(lista_entrada)
    if len(resultado) != len(lista_entrada):
        return False
    for  x in resultado:
        if isinstance(Proceso,x) == False:
            return False
    return True
        
