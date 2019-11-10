from Clases.Procesos import *
from Clases.Procesador import *


class ColaListos:
    def __init__(self):
        self.cola_listos=[]

    # Setters

    # Getters
    def get_cola_listos(self):
        return self.cola_listos

    # Funciones
    def anade_proceso(self, proc):
        self.cola_listos.append(proc)

    def fcfs(self):
        self.cola_listos
        procesador.bloqueados_listos()  # LineaNueva
        # LineaNueva None es el quatum, en este caso no nos interesa
        procesador.listos_ejecucion(None)
        procesador.imprime_cola_bloqueados()  # LineaNueva
        procesador.imprime_cola_listos()  # LineaNueva

    def prioridades(self, procesador):
        self.cola_listos.sort(key=lambda x: x.get_prioridad(), reverse=True)
        procesador.bloqueados_listos()  # LineaNueva
        # LineaNueva None es el quantum, en este caso no nos interesa
        procesador.listos_ejecucion(None)
        procesador.imprime_cola_bloqueados()  # LineaNueva
        procesador.imprime_cola_listos()  # LineaNueva

    def imprimir_consola(self):
        for x in self.cola_listos:
            x.print_proceso_fake()

    def multinivel(self, CL1, CL2, CL3, procesador):
        for proc in self.get_cola_listos():
            tiempo_uso_cpu = 0
            for rafaga in (proc.get_rafaga_tot()):
                if rafaga[0] == "C":
                    tiempo_uso_cpu = tiempo_uso_cpu + int(rafaga[1])
            if tiempo_uso_cpu < 10:
                CL1.anade_proceso(proc)
            elif tiempo_uso_cpu < 20:
                CL2.anade_proceso(proc)
            else:
                CL3.anade_proceso(proc)

        # de esta forma, se ejecuta primero todo lo de la cola 1, despues todo lo de la cola 2,etc
        if CL1 != []:
            CL1.round_robin(5, procesador)
        elif CL2 != []:
            CL2.round_robin(3, procesador)
        else:
            CL3.fcfs(procesador)

    def elimina_elemento(self, num):
        self.cola_listos.pop(num)

    def round_robin(self, quantum, procesador):

        # self.quantum = quantum
        aux = procesador.get_proceso_actual()
        if aux != None:
            tiempo_r = aux.get_tiempo_restante()
            q = aux.get_quantum()
            if tiempo_r > 0 and q > 0:
                print(">>>> aux != None and tiempo_r > 0 and q >0  <<<<")
                # tiempo_r -=1
                q -= 1
                # aux.set_tiempo_restante(tiempo_r)
                aux.set_quantum(q)
                print("quantum actual : "+str(aux.get_quantum()))
                print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                procesador.set_proceso_actual(aux)
            elif tiempo_r > 0 and q == 0:
                print(">>>> aux != None and tiempo_r > 0 and q == 0 <<<<")
                # tiempo_r -= 1
                # aux.set_tiempo_restante(tiempo_r)
                print("quantum actual : "+str(aux.get_quantum()))
                print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                # se añade el proceso a la cola de listos
                self.modificar_rafaga_total(aux,tiempo_r)
                self.anade_proceso(aux)
                self.imprime_cola_listos()
                # Le aplicamos un expropiese venezolano
                procesador.set_proceso_actual(None)
                procesador.bloqueados_listos()
                procesador.listos_ejecucion(quantum)
                procesador.imprime_cola_bloqueados()
                procesador.imprime_cola_listos()

                # if self.cola_listos !=[]: #LineaNueva
                #    proc = self.cola_listos[0]
                #    proc.set_quantum= self.quantum
                #    procesador.set_proceso_actual(proc)
            else:
                if tiempo_r == 0:
                    print("pasa a bloqueado o terminado")
                    procesador.bloqueados_listos()
                    procesador.listos_ejecucion(quantum)
                    procesador.imprime_cola_bloqueados()
                    procesador.imprime_cola_listos()
        else:
            print("################## procesador vacio ###################")
            print(" ")
            procesador.bloqueados_listos()
            procesador.listos_ejecucion(quantum)
            procesador.imprime_cola_bloqueados()
            procesador.imprime_cola_listos()
        return self.cola_listos

    def ordenar(self, algoritmo, quantum, CL1, CL2, CL3, procesador):
        if algoritmo == 0:
            self.fcfs(procesador)  # LineaNueva se agrego procesador
        if algoritmo == 1:
            self.round_robin(quantum, procesador)
        if algoritmo == 2:
            self.prioridades(procesador)  # LineaNueva se agrego procesador
        if algoritmo == 3:
            self.multinivel(CL1, CL2, CL3, procesador)

    def isvacio(self):
        return self.cola_listos == []

    def imprime_cola_listos(self):
        print("Procesos listos")
        for x in self.get_cola_listos():
            print("ID: "+str(x.get_id())+" Tiempo Restante " +
                  str(x.get_tiempo_restante()))
        print("----------------")

#solucion momentanea(o permanente je), se modifica la rafaga total cuando q=0
    def modificar_rafaga_total(self,proceso,tiempo_restante):
        num_rafaga = proceso.get_num_rafaga_actual()
        rafaga_total = proceso.get_rafaga_tot()
        rafaga_total[num_rafaga] = "C"+str(tiempo_restante)