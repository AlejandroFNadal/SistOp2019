class Procesos:  # Contiene los datos esenciales de un proceso
    def __init__(self, datos):
        self.id = datos[0]
        self.tamano_proc = datos[1]
        self.prioridad = datos[2]
        self.tiempo_arribo = datos[4]
        self.rafaga_tot = datos[3]
        self.rafaga_usada = None
        self.estado = None
        self.tiempo_espera = None
        self.tiempo_ejecucion = None
        self.tiempo_inicio_ejecucion = None
        self.particion = None
        self.tiempo_restante = 0
        self.quantum = None
        self.num_rafaga_actual = 0

    # Setters
    def set_tiempo_restante(self, x):
        self.tiempo_restante = x

    def set_id(self, value):
        self.id = value

    def set_estado(self, x):
        self.estado = x

    def set_particion_proc(self, val):
        self.particion = val

    def set_quantum(self, q):
        self.quantum = q

    def set_rafaga_total(self,rafaga):
        self.rafaga_tot=rafaga
    # Getters
    def get_rafaga_tot(self):
        return self.rafaga_tot

    def get_tiempo_arribo(self):
        return self.tiempo_arribo

    def get_prioridad(self):
        if self.prioridad == None:
            return -1
        else:
            return self.prioridad

    def get_tamano_proc(self):
        return self.tamano_proc

    def get_tiempo_restante(self):
        return self.tiempo_restante

    def get_id(self):
        return self.id

    def get_estado(self):
        return self.estado

    def get_num_rafaga_actual(self):
        return self.num_rafaga_actual

    def get_particion_proc(self):
        return self.particion

    def get_quantum(self):
        return self.quantum

    # Funciones
    def muestra_proceso(self):
        print(str(self.id) +
              "   tamano_proc:    " +
              str(self.tamano_proc) +
              "  prioridad:     " +
              str(self.prioridad) +
              "   tiempo_arribo:     " +
              str(self.tiempo_arribo) +
              "  rafaga_tot:     " +
              str(self.rafaga_tot))

    def increment_num_rafaga_actual(self):
        self.num_rafaga_actual += 1

    def decrementar_tiempo_restante(self):
        if self.tiempo_restante >= 0:
            self.tiempo_restante -= 1

    def split_rafaga_tot(self):
        self.rafaga_tot = self.rafaga_tot.split("-")
