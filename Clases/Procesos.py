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
        self.num_rafaga_actual=None
    def get_rafaga_tot(self):
        return self.rafaga_tot
    def set_tiempo_restante(self,x):
        self.tiempo_restante = x
    def decrementar_tiempo_restante(self):
        if self.tiempo_restante >=0:
            self.tiempo_restante=-1
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
    def get_tiempo_restante(self):
        return self.tiempo_restante
    def set_estado(self,x):
        self.estado=x
    def get_num_rafaga_actual(self):
        return self.num_rafaga_actual
    def increment_num_rafaga_actual(self):
        self.num_rafaga_actual=+1
    def get_id(self):
        return self.id
    def get_estado(self):
        return self.estado