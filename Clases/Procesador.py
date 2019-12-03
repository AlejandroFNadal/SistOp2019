from Clases.ColaListos import ColaListos
from Clases.Procesos import *
from Clases.Memoria import *
import time
from Clases.Gantt import *
from Clases.Mapa_memoria import *
import matplotlib.pyplot as plt 


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
        self.salir=False #Controla salidas del bucle principal
        #Para multinivel
        self.cola1=[] 
        self.cola2=[] 
        self.cola3=[]
        self.estadoMLQ=0 #Esto indica que cola se esta usando actualmente. 

    # Setters
    def set_proceso_actual(self, proc):
        self.proceso_actual = proc
    def set_estadoMLQ(self,val):
        if val>=0 and val <=3:
            self.estadoMLQ=val
    def set_cant_procesos(self, lista):
        self.cant_procesos = len(lista)
        print(self.cant_procesos)

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

    def cargar_cola_nuevos(self, procesos,quantum, alg_planificacion):
        cont = 0
        while cont < len(procesos):
            proc = procesos[cont]
            if proc.tiempo_arribo == self.reloj_total:
                auxdatos = [proc.id_proc, proc.tam_proc,proc.prioridad,proc.rafagaCPU,proc.tiempo_arribo]
                auxproc = Procesos(auxdatos)
                auxproc.split_rafaga_tot()
                #funcion para realizar carga de quamtum al proceso
                #primer IF son FCFS,PRIORIDADES,SJF,SRTF
                if alg_planificacion==0 or alg_planificacion==2 or alg_planificacion==4 or alg_planificacion==5:
                    auxproc.set_quantum(None)
                elif alg_planificacion == 1: #significa que es  RR 
                    #creo que no va a ser necesario cargarlo peeeeero por las dudas
                    auxproc.set_quantum(quantum)
                elif alg_planificacion == 3: #multinivel
                    if auxproc.get_prioridad() == 1:
                        auxproc.set_quantum(5)
                    elif auxproc.get_prioridad() == 2:
                        auxproc.set_quantum(3)
                    else:
                        auxproc.set_quantum(None)
                #auxproc.set_quantum(quantum)
                auxproc.set_estado(1) #Nuevo
                auxproc.set_tiempo_restante(int(auxproc.get_rafaga_tot()[0][1]))
                procesos.pop(cont)
                cont -=1 
                #le restamos 1 por que eliminamos un elemento de procesos y "se corre" todo hacia la izquierda
                self.cola_nuevos.append(auxproc)
            cont +=1
        print("Cola Nuevos:")
        for y in self.cola_nuevos:
            print("     "+str(y.get_id()))
        print("---------------------")
        return procesos

    def cargar_cola_listos(self, algoritmo, quantum, memoria):
        cont = 0
        if algoritmo==3: #Multinivel
            while cont < len(self.cola_nuevos):
                proc=self.cola_nuevos[cont]
                if memoria.comprobar_memoria(proc,self):
                    proc.set_estado(2) #Listo
                    if proc.get_prioridad()==1:
                        self.cola1.append(proc)
                    elif proc.get_prioridad()==2:
                        self.cola2.append(proc)
                    elif proc.get_prioridad()==3:
                        self.cola3.append(proc)
                    self.cola_nuevos.pop(cont)
                    cont-=1
                cont+=1    
        else:
            while cont < len(self.cola_nuevos):
                proc = self.cola_nuevos[cont]
                if memoria.comprobar_memoria(proc,self):
                    proc.set_estado(2) #Listo
                    self.procesos_listos.anade_proceso(proc)
                    self.cola_nuevos.pop(cont)
                    cont -= 1 #lo mismo que en cargar cola nuevos
                cont +=1
        self.procesos_listos.ordenar(algoritmo, quantum, self)


    # de bloqueados a listos
    # De esta forma se implementa que solo hay un dispositivo E/S
    def bloqueados_listos(self):
        #Listos a bloqueados
        cont = 0
        while cont < (len(self.procesos_listos.get_cola_listos())):
            proc = self.procesos_listos.get_cola_listos()[cont]
            print(proc.get_id())
            pos = proc.get_num_rafaga_actual()

            if proc.get_rafaga_tot()[pos][0] != "C":
                proc.set_estado(3)  # pasamos a bloqueado
                #print("proc set estado 3")
                print(int(proc.get_rafaga_tot()[pos][1]))
                
                self.cola_bloqueados.append(proc)
                self.procesos_listos.elimina_elemento(cont)
                cont -= 1  # Se resta 1 para moverse 1 a la izquierda de la lista, por que el pop borra 1 elemento y se mueve todo 1 posicion a la izquierda
            cont += 1

        #Bloqueados a Listos
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
        

    def listos_ejecucion(self):
        # si proceso actual es igual a vacio
        if self.proceso_actual == None and self.procesos_listos.get_cola_listos() != []:
            #print("LE1")
            #print("proceso actual NONE  y cola de listos distinto de vacio")
            pos = self.procesos_listos.get_cola_listos()[0].get_num_rafaga_actual()
            rafaga_proc = self.procesos_listos.get_cola_listos()[0].get_rafaga_tot()
            if rafaga_proc[pos][0] == "C":
                #print("Elemento actual CPU")
                self.proceso_actual = self.procesos_listos.get_cola_listos()[0]
                self.proceso_actual.set_estado(5)  #EN EJECUCION
                self.proceso_actual.set_tiempo_restante(
                    int(rafaga_proc[self.proceso_actual.get_num_rafaga_actual()][1]))
                self.procesos_listos.elimina_elemento(0)

        elif self.proceso_actual != None:
            #print("LE2")
            part = self.proceso_actual.get_particion_proc()
            # si el tiempo del proceso actual es 0
            if self.proceso_actual.get_tiempo_restante() == 0 and self.procesos_listos.get_cola_listos() != []:
                #print("LE2-1")
                if self.proceso_actual.get_num_rafaga_actual() < len(self.proceso_actual.get_rafaga_tot())-1:
                    self.proceso_actual.increment_num_rafaga_actual() #LN
                    pos = self.proceso_actual.get_num_rafaga_actual()
                    self.proceso_actual.set_estado(2)
                    tiempo_restante=int(self.proceso_actual.get_rafaga_tot()[pos][1])
                    #print("tiemporestante")
                    #print(tiempo_restante)
                    self.proceso_actual.set_tiempo_restante(int(self.proceso_actual.get_rafaga_tot()[pos][1]))
                    self.procesos_listos.anade_proceso(self.proceso_actual)
                    self.proceso_actual = self.procesos_listos.get_cola_listos()[0]
                    self.proceso_actual.set_estado(5)
                    self.procesos_listos.elimina_elemento(0)
                else:
                    #aca no seria necesario incrementa la rafaga actual por que seria la ultima rafaga (creo)
                    self.proceso_actual.increment_num_rafaga_actual() #LN
                    if self.memoria.get_tipo_part() == "variable":
                        self.memoria.eliminar_particion(part)
                        self.memoria.generar_lista_vacios()
                    else:
                        #es fija, aca desasignamos la particion del proceso
                        pos_part=self.memoria.get_lista_part().index(part)
                        self.memoria.get_lista_part()[pos_part] .desasignar()
                    self.proceso_actual.set_estado(4) #TERMINADO
                    self.proceso_actual.set_particion_proc(None)
                    self.cola_terminados.append(self.proceso_actual)
                    self.proceso_actual = self.procesos_listos.get_cola_listos()[0]
                    self.proceso_actual.set_estado(5)
                    self.procesos_listos.elimina_elemento(0)
                    self.imprime_cola_terminados()
                    self.memoria.imprime_particiones()
            elif self.proceso_actual.get_tiempo_restante() == 0 and self.procesos_listos.get_cola_listos() == []:
                print("LE2-2")
                # No necesariamente es el ultimo proceso
                if self.proceso_actual.get_num_rafaga_actual() == len(self.proceso_actual.get_rafaga_tot())-1:
                    print("LE2-2-1")
                    self.proceso_actual.increment_num_rafaga_actual()
                    self.proceso_actual.set_estado(4) #TERMINADO
                    self.proceso_actual.set_particion_proc(None)
                    self.cola_terminados.append(self.proceso_actual)
                    self.proceso_actual = None
                    self.imprime_cola_terminados()
                    if self.memoria.get_tipo_part() == "variable":
                        self.memoria.eliminar_particion(part)
                        self.memoria.generar_lista_vacios()
                    else:
                        part.desasignar()
                    self.memoria.imprime_particiones()
                else:
                    print("LE2-2-2")
                    self.proceso_actual.increment_num_rafaga_actual()
                    self.proceso_actual.set_estado(2) #LISTO
                    pos=self.proceso_actual.get_num_rafaga_actual()
                    rafaga_total=self.proceso_actual.get_rafaga_tot()
                    self.proceso_actual.set_tiempo_restante(int(rafaga_total[pos][1]))
                    self.procesos_listos.anade_proceso(self.proceso_actual)
                    self.proceso_actual=None                  
                    self.memoria.imprime_particiones()
        #teoricamente no tendria q hacer nada en estos 2 casos pero los pongo para tenerlos en cuenta
        #elif self.proceso_actual == None and self.procesos_listos.get_cola_listos() == []:
        #    print("proceso actual == None // procesos listos == []")
        #elif self.proceso_actual != None and self.procesos_listos.get_cola_listos() != []:
        #    print("proceso actual != None // procesos listos != []")


    def generar_tabla(self):
        #Primero juntamos todos los procesos, todos
        todos_procesos=[]
        for x in self.procesos_listos.get_cola_listos():
            todos_procesos.append(x)
        for x in self.cola_nuevos:
            todos_procesos.append(x)
        if self.proceso_actual!=None:
            todos_procesos.append(self.proceso_actual)
        for x in self.cola_bloqueados:
            todos_procesos.append(x)
        for x in self.cola_terminados:
            todos_procesos.append(x)
        aux = []
        todos_procesos.sort(key=lambda x:x.get_id())
        for x in todos_procesos:
            id = x.get_id()
            estado = x.get_estado()
            if x.get_particion_proc() ==None:
                parti=-1
            else:
                parti=x.get_particion_proc().get_id_par()
            aux.append([id, estado,parti])  # faltan las particiones aca
        self.cubo.append(aux)


    def imprime_cubo(self):
        clk=0
        for x in self.cubo: #iterando sobre tiempo
            print("Tiempo: "+str(clk))
            for y in x:#Iterando sobre procesos
                print("Id: "+str(y[0])+" Estado "+ str(y[1])+" Particion "+str(y[2]))
            clk+=1
    # Metodo para generar el mapa de memoria
    def generar_mapa(self, cubo):
        part_libres = []
        part_ocupadas = []
        aux =[]
        for x in self.memoria.lista_particiones:
            #asddd = {}
            #asddd['aa'] = x.get_id_par()

            #aux.append(asddd)
            dic = {}
            dic['id_par'] = x.get_id_par()
            dic['tama'] = x.get_tamano()
            dic['dir_ini'] = x.get_dir_in()
            dic['dir_fin'] = x.get_dir_fin()
            dic['estado'] = x.get_estado() # Si es Falso esta libre
            
            dic['proceso'] = 0
            if x.get_estado():
                for c in cubo:
                    for i in c:
                        if i[2] == x.get_id_par():
                            dic['proceso'] = i[0]
            aux.append(dic)
                                        
        self.tabla_memoria.append(aux)



    def cuenta_tiempo(self):  # por ahora solo descuenta tiempo del primero de bloqueados
        if self.cola_bloqueados != []:
            # si es cero, la transicion se hara en bloqueados_listos
            self.cola_bloqueados[0].decrementar_tiempo_restante()
            print("Tiempo restante bloqueados: " +
                  str(self.cola_bloqueados[0].get_tiempo_restante()))
        if self.proceso_actual != None:
            # Si es cero, la transicion se hace en listoa
            self.proceso_actual.decrementar_tiempo_restante()

    def Simular(self, preset, procesos, particiones,alg_planificacion,quantum):
        intprocesos = procesos  # para manejar paso por copia en lugar de referencia
        proc_gantt = []
        gantt_amplitud = []
        p = 1
        #For para hacer una lista con las Ids de procesos para el gantt
        for i in procesos:
            proc_gantt.append(str(p))
            gantt_amplitud.append(p*10)
            p+=1
        # alg_planificacion = preset.algoritmo_as  # agregar luego como un valor de preset, traer de la BD
        
        self.memoria = Memoria(preset.tamMemoria, preset.fija_variable,
                               preset.algoritmo_as, preset.sistOpMem,particiones)  # tamano, fija_variable
        self.memoria.imprime_particiones()
        self.set_cant_procesos(procesos)
        self.salir=False
        #Se verifica que todos los procesos puedan entrar
        if self.verificar(preset,particiones,procesos): #si deuvelve True es por que entra
            print("Datos simulacion")
            print("Algoritmo Planificacion "+str(alg_planificacion))
            print("Quantum "+str(quantum))
            while len(self.cola_terminados) < self.cant_procesos and not self.salir:
                intprocesos = self.cargar_cola_nuevos(intprocesos,quantum,alg_planificacion)
                self.cargar_cola_listos(alg_planificacion, quantum, self.memoria)
                if self.proceso_actual != None:
                    print("Proceso en ejecucion "+str(self.proceso_actual.get_id()) +
                          " tiempo restante "+str(self.proceso_actual.get_tiempo_restante()))
                else:
                    print(self.proceso_actual)
                self.generar_tabla()
                self.generar_mapa(self.cubo)
                self.cuenta_tiempo()
                #self.memoria.imprime_particiones()
                if alg_planificacion ==3:
                    if self.estadoMLQ==1:
                        self.cola1=[]
                    elif self.estadoMLQ==2:
                        self.cola2=[]
                    for x in self.procesos_listos.get_cola_listos():
                        if x.get_prioridad()==1:
                            self.cola1.append(x)
                        if x.get_prioridad()==2:
                            self.cola2.append(x)
                    self.procesos_listos.purge_list()
                print("Cola 1:")
                for x in self.cola1:
                    print(x.get_id())
                print("Cola 2:")
                for x in self.cola2:
                    print(x.get_id())
                print("CLK: "+str(self.reloj_total))
                print(
                    "-------------------------------------------------------------------------")
                
                self.reloj_total += 1
                #time.sleep(1)

            self.imprime_cubo()
            mapa1 = Mapa_memoria()
<<<<<<< HEAD
            mapa1.mapa_memoria(self.tabla_memoria, preset.tamMemoria)
=======
            mapa1.mapa_memoria(self.tabla_memoria)
>>>>>>> a31ad6b4cff6949c05f675c81c322d200c63bdfa
            
            gantt1 = Gantt()
            gantt1.gantt(self.cubo, proc_gantt, gantt_amplitud)
            
        else:
            #cuando almenos un proceso no entra
            print(">>> Error <<<")
            print(" Almenos 1 proceso es mayor que las particiones disponibles")
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

    def verificar(self,preset,particiones,procesos):
        tipo_part  = preset.fija_variable
        if tipo_part == "variable":
            tamano_mayor_part = preset.tamMemoria - (preset.sistOpMem*preset.tamMemoria/100)
        else:
            #Recorremos todas las particiones y buscamos la de mayor tamano
            tamano_mayor_part = 0
            for i in particiones:
                if tamano_mayor_part < i.tam_part:
                    tamano_mayor_part = i.tam_part

        band = True # band == False --> no entra alemenos un proceso   band == True --> entran los proceso
        #empezamos con la hipotesis de que entran todos
        for i in procesos:
                if i.tam_proc > tamano_mayor_part:
                    band = False
        return band
