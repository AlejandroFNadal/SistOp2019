from Procesos import *

class prueba:
    def __init__(self,a,b):
        self.d1=a
        self.d2=b#prioridad
    def print_proceso_fake(self):
        print(self.d1)
    def get_prioridad(self):
        return self.d2


    
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
    def round_robin(self):
        return self.cola_listos

            

cola1=ColaListos()
p1=prueba(1,2)
p2=prueba(3,4)
cola1.anade_proceso(p2)
cola1.anade_proceso(p1)
cola1.prioridades()
cola1.imprimir_consola()