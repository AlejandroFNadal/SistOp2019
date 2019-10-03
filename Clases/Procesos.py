class Proceso:  # Contiene los datos esenciales de un proceso
    def __init__(self, datos):
        self.id = datos[0]
        self.tamano_proc = datos[1]
        self.prioridad = datos[2]
        self.tiempo_arribo = datos[3]
        self.rafaga_tot = datos[4]
        self.rafaga_usada = None
        self.estado = None
        self.tiempo_espera = None
        self.tiempo_ejecucion = None
        self.tiempo_inicio_ejecucion = None
        self.particion = None
        self.tiempo_restante=None
        self.quantum=None
    def get_tiempo_arribo(self):
        return self.tiempo_arribo
    def get_prioridad(self):
        return self.prioridad
    def get_tamano_proc(self):
        return self.tamano_proc
    def muestra_proceso(self):
        print(str(self.id) +
              "       " +
              str(self.tamano_proc) +
              "       " +
              str(self.prioridad) +
              "       " +
              str(self.tiempo_arribo) +
              "       " +
              str(self.rafaga_tot))