from Procesos import *


class prueba:
    def __init__(self,id,prioridad,tamano,tiempo_restante,quantum):
        self.id=id
        self.prioridad=prioridad#prioridad
        self.tamano = tamano
        self.tiempo_restante=tiempo_restante
        self.quantum=quantum
    def print_proceso_fake(self):
        print(self.id)
    def get_prioridad(self):
        return self.prioridad
    def get_tamano(self):
        return self.tamano
    def get_tiempo_restante(self):
        return self.tiempo_restante
    def get_quantum(self):
        return self.quantum
    def set_quantum(self,valor):
        self.quantum=valor

def procesosfalsitos():
    p1=prueba(1,3,10,0,0)
    p2=prueba(2,8,9,0,0)
    p3=prueba(3,1,3,0,0)
    return p1,p2,p3

class ColaListos:
    def __init__(self):
        self.cola_listos=[]
    def anade_proceso(self,proc):
        self.cola_listos.append(proc)
    def fcfs(self):
        return self.cola_listos
    def prioridades(self):
        self.cola_listos.sort(key=lambda x: x.get_prioridad(),reverse=True)
    def imprimir_consola(self):
        for x in self.cola_listos:
            x.print_proceso_fake()
    def multinivel(self):
        return self.cola_listos
    def round_robin(self):
        return self.cola_listos

            

#cola1=ColaListos()
#p1=prueba(1,2)
#p2=prueba(3,4)
#cola1.anade_proceso(p2)
#cola1.anade_proceso(p1)
#cola1.prioridades()
#cola1.imprimir_consola()