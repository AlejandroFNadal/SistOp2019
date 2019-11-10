from Clases.ColaListos import ColaListos
from Clases.Procesos import *
from Clases.Memoria import *
import time


class Procesador:  # contendra gran parte de las tareas generales
    def __init__(self):
        self.reloj_total = 0
        self.procesos_listos = ColaListos()
        self.proceso_actual = None
        self.proceso_io = None
        self.cola_nuevos = []
        self.cola_bloqueados = []
        self.cola_terminados = []
        self.cubo = []  # matriz 3d que contiene cada suceso en la simulacion, usada para estadisticas
        self.cant_procesos = 0
        # esto se deberia pasar luego a otra clase
        self.tabla_memoria = []
        self.memoria = None

    # Setters
    def set_proceso_actual(self, proc):
        self.proceso_actual = proc

    def set_cant_procesos(self, lista):
        self.cant_procesos = len(lista)

    # Getters
    def get_proceso_actual(self):
        return self.proceso_actual

    # Funciones
    def buscar_indice(self, buscar, pos):
        if self.cola_nuevos[pos].get_id() == buscar:
            return pos

    def add_proceso(self, proceso):
        self.procesos_listos.anade_proceso(proceso)

    def show_procesos(self):
        print("ID    Pro_Tam    Prioridad  Tiempo de Arribo  Secuencia")
        # auxiliar que contiene la cola de listos
        proc_list_aux = self.procesos_listos.get_cola_listos()
        for x in proc_list_aux:
            x.muestra_proceso()

    def cargar_cola_nuevos(self, procesos):  # Term0.1
        #print("Cargando cola nuevos")
        conteliminador = 0
        for x in procesos:
            #print("Proceso "+str(x.id_proc)+" Arribo "+str(x.tiempo_arribo))
            if x.tiempo_arribo == self.reloj_total:
                auxdatos = [x.id_proc, x.tam_proc,
                            x.prioridad, x.rafagaCPU, x.tiempo_arribo]
                auxproc = Procesos(auxdatos)
                auxproc.split_rafaga_tot()
                #print("En funcion Cola_nuevos, rafaga total"+str(auxproc.get_rafaga_tot()))
                #print("En funcion Cola_nuevos, elemento rafaga "+str(auxproc.get_rafaga_tot()[0]))
                #print("En funcion Cola_nuevos, tiempo restante en rafaga"+str(auxproc.get_rafaga_tot()[0][1]))
                auxproc.set_tiempo_restante(
                    int(auxproc.get_rafaga_tot()[0][1]))
                #print("En funcion Cola_nuevos: Tiempo restante: " +str(auxproc.get_tiempo_restante()))
                procesos.pop(conteliminador)
                self.cola_nuevos.append(auxproc)
            #print("Contador "+str(conteliminador))
            conteliminador += 1

        print("Cola Nuevos:")
        for y in self.cola_nuevos:
            print("     "+str(y.get_id()))
        return procesos

    # borramos parametro procesos
    def cargar_cola_listos(self, algoritmo, particiones, memoria, quantum, CL1, CL2, CL3):
        #print("Cargar cola listos")
        #print("Cola listos actual:" +str(self.procesos_listos.get_cola_listos()))
        cont_cola_nuevos = 0
        for proc in self.cola_nuevos:
            if memoria.comprobar_memoria(proc):
                self.procesos_listos.anade_proceso(proc)
                self.imprime_cola_listos()
                self.cola_nuevos.pop(cont_cola_nuevos)
            cont_cola_nuevos += 1
        self.procesos_listos.ordenar(algoritmo, quantum, CL1, CL2, CL3, self)

    # de bloqueados a listos
    # De esta forma se implementa que solo hay un dispositivo E/S
    def bloqueados_listos(self):
        cont = 0
        while cont < (len(self.procesos_listos.get_cola_listos())):
            proc = self.procesos_listos.get_cola_listos()[cont]
            pos = proc.get_num_rafaga_actual()

            if proc.get_rafaga_tot()[pos][0] != "C":
                proc.set_estado(3)  # pasamos a bloqueado
                self.cola_bloqueados.append(proc)
                self.procesos_listos.elimina_elemento(cont)
                cont -= 1  # Se resta 1 para moverse 1 a la izquierda de la lista, por que el pop borra 1 elemento y se mueve todo 1 posicion a la izquierda
            cont += 1

        if self.cola_bloqueados != []:
            proc = self.cola_bloqueados[0]
            if proc.get_tiempo_restante() == 0:
                rafaga_proc = proc.get_rafaga_tot()
                # podemos preguntar por el que sigue por que la ultima rafaga es C
                pos = proc.get_num_rafaga_actual()

                if rafaga_proc[pos+1][0] == "C":
                    proc.set_estado(2)
                    proc.increment_num_rafaga_actual()
                    proc.set_tiempo_restante(int(rafaga_proc[pos+1][1]))
                    self.procesos_listos.anade_proceso(proc)
                    indice = self.cola_bloqueados.index(proc)
                    self.cola_bloqueados.pop(indice)
                elif rafaga_proc[pos+1][0] != "C":
                    proc.increment_num_rafaga_actual()
                    tiempo = proc.get_num_rafaga_actual()
                    proc.set_tiempo_restante(int(rafaga_proc[tiempo][1]))

    # por si se rompe, aca se agrego quantum y lineas que tengan #LineaNueva
    def listos_ejecucion(self, quantum):
        # si proceso actual es igual a vacio
        if self.proceso_actual == None and self.procesos_listos.get_cola_listos() != []:
            print("proceso actual NONE  y cola de listos distinto de vacio")
            pos = self.procesos_listos.get_cola_listos()[
                0].get_num_rafaga_actual()
            rafaga_proc = self.procesos_listos.get_cola_listos()[
                0].get_rafaga_tot()
            if rafaga_proc[pos][0] == "C":
                print("siguiente elemento CPU y tiempo restante proc_listos = 0")
                self.proceso_actual = self.procesos_listos.get_cola_listos()[0]
                self.proceso_actual.set_quantum(quantum)  # LineaNueva
                #print("Quantum cargado : " + str(self.proceso_actual.get_quantum()))
                self.proceso_actual.set_tiempo_restante(
                    int(rafaga_proc[self.proceso_actual.get_num_rafaga_actual()][1]))
                # self.proceso_actual.increment_num_rafaga_actual()
                self.procesos_listos.elimina_elemento(0)

        elif self.proceso_actual != None:
            part = self.proceso_actual.get_particion_proc()
            # si el tiempo del proceso actual es 0
            if self.proceso_actual.get_tiempo_restante() == 0 and self.procesos_listos.get_cola_listos() != []:
                if self.proceso_actual.get_num_rafaga_actual() < len(self.proceso_actual.get_rafaga_tot())-1:
                    self.procesos_listos.anade_proceso(self.proceso_actual)
                    self.proceso_actual = self.procesos_listos.get_cola_listos()[0]
                    self.proceso_actual.set_quantum(quantum)  # LineaNueva
                    #print("Quantum cargado : " + str(self.proceso_actual.get_quantum()))
                    self.procesos_listos.elimina_elemento(0)
                else:
                    if self.memoria.get_tipo_part() == "variable":
                        self.memoria.eliminar_particion(part)
                        self.memoria.generar_lista_vacios()
                    self.cola_terminados.append(self.proceso_actual)
                    self.proceso_actual = self.procesos_listos.get_cola_listos()[0]
                    self.proceso_actual.set_quantum(quantum)  # LineaNueva
                    #print("Quantum cargado : " + str(self.proceso_actual.get_quantum()))
                    self.procesos_listos.elimina_elemento(0)
                    self.imprime_cola_terminados()
                    self.memoria.imprime_particiones()
            elif self.proceso_actual.get_tiempo_restante() == 0 and self.procesos_listos.get_cola_listos() == []:
                # Ultimo proceso
                if self.proceso_actual.get_num_rafaga_actual() == len(self.proceso_actual.get_rafaga_tot())-1:
                    self.cola_terminados.append(self.proceso_actual)
                    self.proceso_actual = None
                    self.imprime_cola_terminados()
                    if self.memoria.get_tipo_part() == "variable":
                        self.memoria.eliminar_particion(part)
                        self.memoria.generar_lista_vacios()
                    self.memoria.imprime_particiones()

    def generar_tabla(self):
        aux = []
        for x in self.procesos_listos.get_cola_listos():
            id = x.get_id()
            estado = x.get_estado()
            aux.append([id, estado])  # faltan las particiones aca
        self.cubo.append(aux)

    def cuenta_tiempo(self):  # por ahora solo descuenta tiempo del primero de bloqueados
        if self.cola_bloqueados != []:
            # si es cero, la transicion se hara en bloqueados_listos
            self.cola_bloqueados[0].decrementar_tiempo_restante()
            print("Tiempo restante bloqueados: " +
                  str(self.cola_bloqueados[0].get_tiempo_restante()))
        if self.proceso_actual != None:
            # Si es cero, la transicion se hace en listoa
            self.proceso_actual.decrementar_tiempo_restante()

    def Simular(self, preset, procesos, particiones):
        intprocesos = procesos  # para manejar paso por copia en lugar de referencia
        # alg_planificacion = preset.algoritmo_as  # agregar luego como un valor de preset, traer de la BD
        alg_planificacion = 1
        cola_listos_principal = ColaListos()
        quantum = 5
        self.memoria = Memoria(preset.tamMemoria, preset.fija_variable,
                               preset.algoritmo_as, preset.sistOpMem)  # tamano, fija_variable
        self.set_cant_procesos(procesos)
        if alg_planificacion == 3:  # MQL
            CL1 = ColaListos()
            CL2 = ColaListos()
            CL3 = ColaListos()
        while len(self.cola_terminados) < self.cant_procesos:
            # esta llamada deberia funcionar ya
            intprocesos = self.cargar_cola_nuevos(intprocesos)
            if alg_planificacion == 3:
                self.cargar_cola_listos(
                    alg_planificacion, particiones, self.memoria, quantum, CL1, CL2, CL3)
            else:
                self.cargar_cola_listos(
                    alg_planificacion, particiones, self.memoria, quantum, None, None, None)
            # self.bloqueados_listos() #LineaNueva se comentaron estas lineas por que se ejecutaran dentro de cada planificador
            # self.listos_ejecucion()
            # self.imprime_cola_bloqueados()
            # self.imprime_cola_listos()
            if self.proceso_actual != None:
                print("Proceso en ejecucion "+str(self.proceso_actual.get_id()) +
                      "tiempo restante "+str(self.proceso_actual.get_tiempo_restante()))
            else:
                print(self.proceso_actual)
            self.generar_tabla()
            self.cuenta_tiempo()
            print("CLK: "+str(self.reloj_total))
            print(
                "-------------------------------------------------------------------------")
            self.reloj_total += 1
            time.sleep(1)
        # preset es una lista de preconfiguraciones, procesos
        # es lista de objetos del tipo proceso y particiones es una lista de objetos del tipo particiones
        # DEBUGGING FUNCTIONS

    def imprime_cola_listos(self):
        print("Procesos listos")
        for x in self.procesos_listos.get_cola_listos():
            print("ID: "+str(x.get_id())+" Tiempo Restante " +
                  str(x.get_tiempo_restante()))
        print("----------------")

    def imprime_cola_bloqueados(self):
        print("Procesos bloqueados")
        for x in self.cola_bloqueados:
            print("ID: "+str(x.get_id())+" Tiempo Restante " +
                  str(x.get_tiempo_restante()))

        print("----------------")

    def imprime_cola_terminados(self):
        print("Procesos terminados")
        for x in self.cola_terminados:
            print("ID: "+str(x.get_id())+" Tiempo Restante " +
                  str(x.get_tiempo_restante()))
        print("----------------")
