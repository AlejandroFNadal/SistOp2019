class Procesador:  # contendra gran parte de las tareas generales
    def __init__(self):
        self.procesos_listos = []
        self.proceso_actual=None
    def add_proceso(self, proceso):
        self.procesos_listos.append(proceso)

    def show_procesos(self):
        print("ID    Pro_Tam    Prioridad  Tiempo de Arribo  Secuencia")
        for x in self.procesos_listos:
            x.muestra_proceso()
    def get_proceso_actual(self):
        return self.proceso_actual
    def set_proceso_actual(self,proc)
        self.proceso_actual=proc