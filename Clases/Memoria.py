class Memoria:
    def __init__(self,tamano,tipo_particion):
        self.tamano=tamano
        self.lista_particiones=None 
        self.tipo_particion=tipo_particion#True es fija,False es variable
        self.algoritmo_asignacion=None #1.BestF, 2 FirstF, 3 WorstF
    def comprobar_memoria(self,tamano):
        pass