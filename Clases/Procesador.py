from ColaListos import ColaListos
from Memoria import *

class Procesador:  # contendra gran parte de las tareas generales
    def __init__(self):
        self.reloj_total = 0
        self.procesos_listos = ColaListos()
        self.proceso_actual = None
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

    def crear_particion(self, tamano): pass

    def compactar_memoria(self): pass

    def comprobar_memoria(self, proceso, fija_variable):
        if fija_variable == 1:
            print("Bananas")
    def cargar_cola_nuevos(self, procesos):#Term0.1
        for x in procesos:
            if x.get_tiempo_arribo() == self.reloj_total:
                self.cola_nuevos.append(x)

    def cargar_cola_listos(self, algoritmo, procesos, particiones,memoria):
        for proc in self.cola_nuevos:
            if memoria.comprobar_memoria(proc):
                self.procesos_listos.anade_proceso(proc)

    # ambas interacciones, ida y vuelta
    def bloqueados_listos(self, procesos_listos, cola_bloqueados): pass
    def generar_tabla(self): pass
    def cuenta_tiempo(self): pass

    def Simular(self, preset, procesos, particiones):
        intprocesos = procesos  # para manejar paso por copia en lugar de referencia
        alg_planificacion = preset[7]  # agregar luego como un valor de preset, traer de la BD
        cola_listos_principal = ColaListos()
        mem1=Memoria(preset[2],preset[4]) #tamano, fija_variable
        if alg_planificacion == 3:  # MQL
            CL1 = ColaListos()
            CL2 = ColaListos()
            CL3 = ColaListos()
        while intprocesos != []:
            self.cargar_cola_nuevos(intprocesos)#esta llamada deberia funcionar ya
            self.cargar_cola_listos(alg_planificacion, intprocesos, particiones,mem1)
            self.bloqueados_listos(self.procesos_listos, self.cola_bloqueados)
            self.generar_tabla()
            self.cuenta_tiempo()

            self.reloj_total+=1

        # preset es una lista de preconfiguraciones, procesos
        # es lista de objetos del tipo proceso y particiones es una lista de objetos del tipo particiones
