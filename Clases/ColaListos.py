from Clases.Procesos import *
#from Clases.Procesador import *

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

    def fcfs(self,procesador):   
        #None es el quatum, en este caso no nos interesa
        procesador.listos_ejecucion()
        procesador.bloqueados_listos()
        if procesador.get_proceso_actual() == None:
            procesador.listos_ejecucion()
        procesador.imprime_cola_listos()
        procesador.imprime_cola_bloqueados()

        
    def prioridades(self, procesador):
        self.cola_listos.sort(key=lambda x: x.get_prioridad())
        procesador.listos_ejecucion()
        procesador.bloqueados_listos()
        if procesador.get_proceso_actual() == None:
            procesador.listos_ejecucion()
        procesador.imprime_cola_bloqueados()
        procesador.imprime_cola_listos()

    def imprimir_consola(self):
        for x in self.cola_listos:
            x.print_proceso_fake()
    def multinivel(self,procesador):
        aux = procesador.get_proceso_actual()
        self.purge_list()
        if procesador.cola1 != [] or (procesador.get_proceso_actual() != None and procesador.get_proceso_actual().get_prioridad()==1):
            quantum=5
            procesador.set_estadoMLQ(1)
            #Magic here
            for x in procesador.cola1:
                self.cola_listos.append(x)
            #Magic here
            if aux != None and aux.get_prioridad() == 3:
                aux.set_estado(2) #listo
                tiempo_r_fcfs = aux.get_tiempo_restante()
                self.modificar_rafaga_total(aux,tiempo_r_fcfs)
                self.cola_listos.append(aux)
                procesador.set_proceso_actual(None)
                procesador.listos_ejecucion()
                aux = procesador.get_proceso_actual()
            if aux != None and aux.get_prioridad() == 2:
                aux.set_estado(2) #listo
                tiempo_r_rr2 = aux.get_tiempo_restante()
                self.modificar_rafaga_total(aux,tiempo_r_rr2)
                self.cola_listos.append(aux)
                procesador.set_proceso_actual(None)
                procesador.listos_ejecucion()
                aux = procesador.get_proceso_actual()
            if aux != None:
                tiempo_r = aux.get_tiempo_restante()
                q = procesador.get_proceso_actual().get_quantum()
                q -= 1
                if tiempo_r > 0 and q > 0: #No termino ni el quantum ni el tiempo restante
                    aux.set_quantum(q)
                    #print("quantum1 actual : "+str(aux.get_quantum()))
                    print(procesador.get_proceso_actual().get_quantum())
                    #print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                    procesador.bloqueados_listos()
                    procesador.imprime_cola_bloqueados()
                    procesador.imprime_cola_listos()
                elif tiempo_r > 0 and q == 0: # se acabo el quantum
                    #print("quantum actual : "+str(aux.get_quantum()))
                    #print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                    # se añade el proceso a la cola de listos
                    self.modificar_rafaga_total(aux,tiempo_r)
                    aux.set_estado(2) #LISTO
                    if aux.get_prioridad() == 1:
                        aux.set_quantum(5)
                    elif aux.get_prioridad() == 2:
                        aux.set_quantum(3)
                    elif aux.get_prioridad() == 3:
                        aux.set_quantum(None)
                    self.anade_proceso(aux)
                    self.imprime_cola_listos()
                    # Le aplicamos un expropiese venezolano
                    procesador.set_proceso_actual(None)
                    procesador.listos_ejecucion()
                    procesador.bloqueados_listos()
                    if procesador.get_proceso_actual() == None:
                        procesador.listos_ejecucion()
                    procesador.imprime_cola_bloqueados()
                    procesador.imprime_cola_listos()
                else:
                    if tiempo_r == 0:
                        #print("pasa a bloqueado o terminado")
                        #aca va a salir el proceso por que TR=0, entonces seteamos el quantum antes que salga
                        if procesador.get_proceso_actual().get_prioridad() == 1:
                            procesador.get_proceso_actual().set_quantum(5)
                        elif procesador.get_proceso_actual().get_prioridad() == 2:
                            procesador.get_proceso_actual().set_quantum(3)
                        elif procesador.get_proceso_actual().get_prioridad() == 3:
                            procesador.get_proceso_actual().set_quantum(None)
                        procesador.listos_ejecucion()
                        procesador.bloqueados_listos()
                        if procesador.get_proceso_actual() == None:
                            procesador.listos_ejecucion()
                        procesador.imprime_cola_bloqueados()
                        procesador.imprime_cola_listos()
            else:
                #se pasa primero de bloqueados a listos para cargar la cola de listos, por si estuviese vacia, total 
                #el procesador sabemos que esta vacio
                procesador.bloqueados_listos()
                procesador.listos_ejecucion()
                procesador.imprime_cola_bloqueados()
                procesador.imprime_cola_listos()
            #Magic here again
            print(procesador.cola1)
        else:
            if procesador.cola2 != [] or (procesador.get_proceso_actual() != None and procesador.get_proceso_actual().get_prioridad()==2): #rr 2
                procesador.set_estadoMLQ(2)
                quantum=3
                for x in procesador.cola2:
                    self.cola_listos.append(x)
                #Magic here
                if aux != None and aux.get_prioridad() == 3:
                    aux.set_estado(2) #listo
                    tiempo_r_fcfs = aux.get_tiempo_restante()
                    self.modificar_rafaga_total(aux,tiempo_r_fcfs)
                    self.cola_listos.append(aux)
                    procesador.set_proceso_actual(None)
                    procesador.listos_ejecucion()
                    aux = procesador.get_proceso_actual()
                if aux != None:
                    tiempo_r = aux.get_tiempo_restante()
                    q = procesador.get_proceso_actual().get_quantum()
                    q -= 1
                    if tiempo_r > 0 and q > 0: #No termino ni el quantum ni el tiempo restante
                        aux.set_quantum(q)
                        #print("quantum1 actual : "+str(aux.get_quantum()))
                        print(procesador.get_proceso_actual().get_quantum())
                        #print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                        procesador.bloqueados_listos()
                        procesador.imprime_cola_bloqueados()
                        procesador.imprime_cola_listos()
                    elif tiempo_r > 0 and q == 0: # se acabo el quantum
                        #print("quantum actual : "+str(aux.get_quantum()))
                        #print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                        # se añade el proceso a la cola de listos
                        self.modificar_rafaga_total(aux,tiempo_r)
                        aux.set_estado(2) #LISTO
                        if aux.get_prioridad() == 1:
                            aux.set_quantum(5)
                        elif aux.get_prioridad() == 2:
                            aux.set_quantum(3)
                        elif aux.get_prioridad() == 3:
                            aux.set_quantum(None)
                        self.anade_proceso(aux)
                        self.imprime_cola_listos()
                        # Le aplicamos un expropiese venezolano
                        procesador.set_proceso_actual(None)
                        procesador.listos_ejecucion()
                        procesador.bloqueados_listos()
                        if procesador.get_proceso_actual() == None:
                            procesador.listos_ejecucion()
                        procesador.imprime_cola_bloqueados()
                        procesador.imprime_cola_listos()
                    else:
                        if tiempo_r == 0:
                            #print("pasa a bloqueado o terminado")
                            #aca va a salir el proceso por que TR=0, entonces seteamos el quantum antes que salga
                            if procesador.get_proceso_actual().get_prioridad() == 1:
                                procesador.get_proceso_actual().set_quantum(5)
                            elif procesador.get_proceso_actual().get_prioridad() == 2:
                                procesador.get_proceso_actual().set_quantum(3)
                            elif procesador.get_proceso_actual().get_prioridad() == 3:
                                procesador.get_proceso_actual().set_quantum(None)
                            procesador.listos_ejecucion()
                            procesador.bloqueados_listos()
                            if procesador.get_proceso_actual() == None:
                                procesador.listos_ejecucion()
                            procesador.imprime_cola_bloqueados()
                            procesador.imprime_cola_listos()
                else:
                    #se pasa primero de bloqueados a listos para cargar la cola de listos, por si estuviese vacia, total 
                    #el procesador sabemos que esta vacio
                    procesador.bloqueados_listos()
                    procesador.listos_ejecucion()
                    procesador.imprime_cola_bloqueados()
                    procesador.imprime_cola_listos()
            else:
                if procesador.cola3!=[] or (procesador.get_proceso_actual() != None and procesador.get_proceso_actual().get_prioridad()==3):
                    procesador.set_estadoMLQ(3)
                    self.purge_list()
                    for x in procesador.cola3:
                        self.cola_listos.append(x)
                    procesador.listos_ejecucion()
                    procesador.bloqueados_listos()
                    if procesador.get_proceso_actual() == None:
                        procesador.listos_ejecucion()
                    procesador.imprime_cola_listos()
                    procesador.imprime_cola_bloqueados()
                else:
                    print(">>>> ACA NO TIENE QUE ENTRAR  <<<<")
                    print(">>>> ACA NO TIENE QUE ENTRAR  <<<<")
                    print("Solo entra en la 1ra vuelta")
                    print(">>>> ACA NO TIENE QUE ENTRAR  <<<<")
                    print(">>>> ACA NO TIENE QUE ENTRAR  <<<<")
                    procesador.bloqueados_listos()
                    procesador.listos_ejecucion()
                    procesador.imprime_cola_bloqueados()
                    procesador.imprime_cola_listos()

    def elimina_elemento(self, num):
        self.cola_listos.pop(num)
    def purge_list(self):
        self.cola_listos=[]
    def round_robin(self, quantum, procesador):
        aux = procesador.get_proceso_actual()
        if aux != None:
            tiempo_r = aux.get_tiempo_restante()
            q = procesador.get_proceso_actual().get_quantum()
            q -= 1
            if tiempo_r > 0 and q > 0: #No termino ni el quantum ni el tiempo restante
                aux.set_quantum(q)
                #print("quantum1 actual : "+str(aux.get_quantum()))
                print(procesador.get_proceso_actual().get_quantum())
                #print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                procesador.bloqueados_listos()
                procesador.imprime_cola_bloqueados()
                procesador.imprime_cola_listos()
            elif tiempo_r > 0 and q == 0: # se acabo el quantum
                #print("quantum actual : "+str(aux.get_quantum()))
                #print("Tiempo restante del proceso actual : " +str(aux.get_tiempo_restante()))
                # se añade el proceso a la cola de listos
                self.modificar_rafaga_total(aux,tiempo_r)
                aux.set_quantum(quantum)
                aux.set_estado(2) #LISTO
                self.anade_proceso(aux)
                self.imprime_cola_listos()
                # Le aplicamos un expropiese venezolano
                procesador.set_proceso_actual(None)
                procesador.listos_ejecucion()
                procesador.bloqueados_listos()
                if procesador.get_proceso_actual() == None:
                    procesador.listos_ejecucion()
                procesador.imprime_cola_bloqueados()
                procesador.imprime_cola_listos()
            else:
                if tiempo_r == 0:
                    #print("pasa a bloqueado o terminado")
                    #aca va a salir el proceso por que TR=0, entonces seteamos el quantum antes que salga
                    procesador.get_proceso_actual().set_quantum(quantum)
                    procesador.listos_ejecucion()
                    procesador.bloqueados_listos()
                    if procesador.get_proceso_actual() == None:
                        procesador.listos_ejecucion()
                    procesador.imprime_cola_bloqueados()
                    procesador.imprime_cola_listos()
        else:
            #se pasa primero de bloqueados a listos para cargar la cola de listos, por si estuviese vacia, total 
            #el procesador sabemos que esta vacio
            procesador.bloqueados_listos()
            procesador.listos_ejecucion()
            procesador.imprime_cola_bloqueados()
            procesador.imprime_cola_listos()
        return self.cola_listos

    #si band == True, significa que esta en SRTF, si band == False, significa que solo es SJF
    def sjf(self,procesador,band):
        primer_elemento = True
        pos_elem_menor = None
        pos = 0
        for i in self.cola_listos: #avanzamos toda la cola de listos
            rafaga = i.get_rafaga_tot()
            num_rafaga = i.get_num_rafaga_actual()
            elem_rafaga = rafaga[num_rafaga]
            if elem_rafaga[0] == "C" and primer_elemento: #solamente el primer elemento
                proceso_menor = i
                pos_elem_menor = pos
                tiempo_menor = int(elem_rafaga[1])
                primer_elemento = False
            elif elem_rafaga[0] == "C" and not(primer_elemento): #el resto de los elementos
                if tiempo_menor >= int(elem_rafaga[1]): #comparamos si tenemos el menor tiempo
                    proceso_menor = i
                    pos_elem_menor = pos
                    tiempo_menor = int(elem_rafaga[1])
            pos +=1

        #agregamos al principio de la cola de listos a nuestro proceso cuya rafaga de ejecucion sea la menor
        #Seria None si no hay procesos cuya rafaga a ejecutarse sea "CPU" o que no haya elementos en Cola de listos
        if pos_elem_menor != None: 
            self.cola_listos.pop(pos_elem_menor)
            self.cola_listos.insert(0,proceso_menor)

        #luego procedemos a llamar a las funciones de intercambio de colas
        if not band:
            procesador.listos_ejecucion()
            procesador.bloqueados_listos()
            if procesador.get_proceso_actual() == None:
                procesador.listos_ejecucion()


    #basicamente lo mismo que el SJF pero con expropiacion
    #si band == True, significa que esta en SRTF, si band == False, significa que solo es SJF
    def srtf(self,procesador,band):
        self.sjf(procesador,band)
        # 1ro verificar si el tiempo de ejecicion restante del proceso que esta en el procesador 
        #es menor al tiempo de ejecucion del proceso que esta en cola de listos (en la 1ra pos)
        cola_listos = self.get_cola_listos()
        proceso_actual = procesador.get_proceso_actual()
        if len(cola_listos) > 0 and proceso_actual != None:
            rafaga_tot = cola_listos[0].get_rafaga_tot()
            num_rafaga = cola_listos[0].get_num_rafaga_actual()
            tiempo_ejecucion = int(rafaga_tot[num_rafaga][1])
            tiempo_restante = proceso_actual.get_tiempo_restante()
            if  tiempo_restante > tiempo_ejecucion:
                #sacamos el proceso del procesador
                proceso_actual.set_estado(2) #LISTOS
                self.modificar_rafaga_total(proceso_actual,tiempo_restante)
                self.anade_proceso(proceso_actual)
                procesador.set_proceso_actual(None) 

        #insertamos el proximo proceso en el procesador
        procesador.listos_ejecucion()
        procesador.bloqueados_listos()
        if procesador.get_proceso_actual() == None:
            procesador.listos_ejecucion()

    def ordenar(self, algoritmo, quantum, procesador):
        if algoritmo == 0:
            self.fcfs(procesador)  
        if algoritmo == 1:
            self.round_robin(quantum, procesador)
        if algoritmo == 2:
            self.prioridades(procesador) 
        if algoritmo == 3:
            self.multinivel(procesador)
        if algoritmo == 4:
            self.sjf(procesador,False)
        if algoritmo == 5:
            self.srtf(procesador,True)

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
        # rafaga_total[num_rafaga] = "C"+str(tiempo_restante) code viejo
        rafaga_total[num_rafaga] = ("C",tiempo_restante)
        proceso.set_rafaga_total(rafaga_total)