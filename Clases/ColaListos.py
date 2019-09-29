from Procesos import *
#from Procesador import *

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
    def set_tiempo_restante(self,valor):
        self.tiempo_restante=valor
        
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
    def get_cola_listos(self):
        return self.cola_listos
    def fcfs(self,procesador):
        return self.cola_listos
    def prioridades(self):
        self.cola_listos.sort(key=lambda x: x.get_prioridad(),reverse=True)
    def imprimir_consola(self):
        for x in self.cola_listos:
            x.print_proceso_fake()
    def multinivel(self):
        return self.cola_listos
    def round_robin(self, quantum, procesador):
        
        self.quantum = quantum
        aux = procesador.get_proceso_actual()
        if aux != None:
            tiempo_r = aux.get_tiempo_restante()
            q = aux.get_quantum()
            if tiempo_r >0 and q >0:
                tiempo_r -=1
                q -= 1
                aux.set_tiempo_restante(tiempo_r)
                aux.set_quantum(q) 
                procesador.set_proceso_actual(aux)
            elif tiempo_r >0 and q ==0:
                tiempo_r -= 1
                aux.set_tiempo_restante(tiempo_r)
                self.anade_proceso(aux)
                if self.cola_listos !=[]:
                    proc = self.cola_listos[0]
                    proc.set_quantum= self.quantum
                    procesador.set_proceso_actual(proc)
            else:
                if tiempo_r == 0:
                    print("pasa a bloqueado o terminado")
                    # pasa a bloqueado o terminado
        return self.cola_listos




