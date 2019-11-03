from Clases.ColaListos import ColaListos
from Clases.Procesos import *
from Clases.Memoria import *
import time
class Procesador:  # contendra gran parte de las tareas generales
    def __init__(self):
        self.reloj_total = 0
        self.procesos_listos = ColaListos()
        self.proceso_actual = None
        self.proceso_io=None
        self.cola_nuevos = []
        self.cola_bloqueados = []
        self.cola_terminados = []
        self.cubo = []  # matriz 3d que contiene cada suceso en la simulacion, usada para estadisticas

        # esto se deberia pasar luego a otra clase
        self.tabla_memoria = []

    def add_proceso(self, proceso):
        self.procesos_listos.anade_proceso(proceso)

    def show_procesos(self):
        print("ID    Pro_Tam    Prioridad  Tiempo de Arribo  Secuencia")
        # auxiliar que contiene la cola de listos
        proc_list_aux = self.procesos_listos.get_cola_listos()
        for x in proc_list_aux:
            x.muestra_proceso()

    def get_proceso_actual(self):
        return self.proceso_actual

    def set_proceso_actual(self, proc):
        self.proceso_actual = proc

    def cargar_cola_nuevos(self, procesos):#Term0.1
        print("Cargando cola nuevos")
        conteliminador=0
        for x in procesos:
            print("Proceso "+str(x.id_proc)+" Arribo "+str(x.tiempo_arribo))
            if x.tiempo_arribo == self.reloj_total:
                auxdatos=[x.id_proc,x.tam_proc,x.prioridad,x.rafagaCPU,x.tiempo_arribo]
                auxproc=Procesos(auxdatos)
                self.cola_nuevos.append(auxproc)
                procesos.pop(conteliminador)
            print("Contador "+str(conteliminador))
            conteliminador+=1
        return procesos

    def cargar_cola_listos(self, algoritmo, procesos, particiones,memoria,quantum):
        print("Cargar cola listos")
        print("Cola listos actual:" +str(self.procesos_listos.get_cola_listos()))
        for proc in self.cola_nuevos:
            if memoria.comprobar_memoria(proc):
                self.procesos_listos.anade_proceso(proc)
                self.imprime_cola_listos()
        self.procesos_listos.ordenar(algoritmo,quantum,self)


    # de bloqueados a listos
    # De esta forma se implementa que solo hay un dispositivo E/S
    def bloqueados_listos(self, procesos_listos, cola_bloqueados):
        aux=0
        if cola_bloqueados !=[]:
            proc=cola_bloqueados[0]
            pos=proc.get_num_rafaga_actual()
            sig_elem_rafaga=proc.get_rafaga_tot()[pos+1]#cambiamos su tiempo restante
            if sig_elem_rafaga[0]=="C" and proc.get_tiempo_restante()==0:  
                proc.set_estado(2)#cambiamos su estado a listo
                proc.increment_num_rafaga_actual()
                procesos_listos.append(proc)#lo anadimos a la cola de listos
                self.cola_bloqueados.pop(0)#lo sacamos de la cola de bloqueados
        
        #aca chequeamos para pasar de listos a bloqueados
        cont=0
        for proc in procesos_listos.get_cola_listos():
            pos=proc.get_num_rafaga_actual()
            actual_elem_rafaga=proc.get_rafaga_tot()[pos]
            if actual_elem_rafaga[0]!="C" and proc.get_tiempo_restante()==0:
                proc.set_tiempo_restante=int(proc.get_rafaga_tot(pos+1)[1])
                cola_bloqueados.append(proc)
                procesos_listos.elimina_elemento(cont)
            cont+=1  
    def generar_tabla(self):
        aux=[]
        for x in self.procesos_listos.get_cola_listos():
            id=x.get_id()
            estado=x.get_estado()
            aux.append([id,estado]) #faltan las particiones aca
        self.cubo.append(aux)
    def cuenta_tiempo(self): #por ahora solo descuenta tiempo del primero de bloqueados
        if self.cola_bloqueados != []:
            self.cola_bloqueados[0].decrementar_tiempo_restante() #si es cero, la transicion se hara en bloqueados_listos
        if self.proceso_actual != None:
            self.proceso_actual.decrementar_tiempo_restante() #Si es cero, la transicion se hace en listoa
    
    def Simular(self, preset, procesos, particiones):
        intprocesos = procesos  # para manejar paso por copia en lugar de referencia
        alg_planificacion = preset.algoritmo_as  # agregar luego como un valor de preset, traer de la BD
        cola_listos_principal = ColaListos()
        quantum=5
        mem1=Memoria(preset.tamMemoria,preset.fija_variable,preset.algoritmo_as,preset.sistOpMem) #tamano, fija_variable
        if alg_planificacion == 3:  # MQL
            CL1 = ColaListos()
            CL2 = ColaListos()
            CL3 = ColaListos()
        while intprocesos != [] and self.procesos_listos.isvacio():
            intprocesos=self.cargar_cola_nuevos(intprocesos)#esta llamada deberia funcionar ya
            print()
            self.cargar_cola_listos(alg_planificacion, intprocesos, particiones,mem1,quantum)
            self.bloqueados_listos(self.procesos_listos, self.cola_bloqueados)
            self.generar_tabla()
            self.cuenta_tiempo()
            print("CLK: "+str(self.reloj_total))
            self.reloj_total+=1
            time.sleep(1)
        # preset es una lista de preconfiguraciones, procesos
        # es lista de objetos del tipo proceso y particiones es una lista de objetos del tipo particiones
        #DEBUGGING FUNCTIONS
    def imprime_cola_listos(self):
        print("Procesos listos")
        for x in self.procesos_listos.get_cola_listos():
            print(x.get_id())