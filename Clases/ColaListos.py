from Clases.Procesos import *


class ColaListos:
    def __init__(self):
        self.cola_listos=[]
    def anade_proceso(self,proc):
        self.cola_listos.append(proc)
    def get_cola_listos(self):
        return self.cola_listos
    def fcfs(self):
        return self.cola_listos
    def prioridades(self):
        self.cola_listos.sort(key=lambda x: x.get_prioridad(),reverse=True)
    def imprimir_consola(self):
        for x in self.cola_listos:
            x.print_proceso_fake()
    def multinivel(self):
        return self.cola_listos
    def elimina_elemento(self, num):
        self.cola_listos.pop(num)
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
    
    def ordenar(self,algoritmo,quantum,procesador):
        if algoritmo ==0:
            self.fcfs()
        if algoritmo == 1:
            self.round_robin(quantum,procesador)
        if algoritmo == 2:
            self.prioridades()
        if algoritmo == 3:
            self.multinivel()




