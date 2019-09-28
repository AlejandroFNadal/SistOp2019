class Proceso:  # Contiene los datos esenciales de un proceso
    def __init__(self, datos):
        self.id = datos[0]
        self.pro_tam = datos[1]
        self.prioridad = datos[2]
        self.tiempo_arribo = datos[3]
        self.rafaga_tot = datos[4]
        self.rafaga_usada = None
        self.estado = None
        self.tiempo_espera = None
        self.tiempo_ejecucion = None
        self.tiempo_inicio_ejecucion = None
        self.particion = None

    def muestra_proceso(self):
        print(str(self.id) +
              "       " +
              str(self.pro_tam) +
              "       " +
              str(self.prioridad) +
              "       " +
              str(self.tiempo_arribo) +
              "       " +
              str(self.rafaga_tot))