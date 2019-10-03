import sys
class Memoria:
    def __init__(self,tamano,tipo_particion):
        self.tamano=tamano
        self.lista_particiones=[]
        self.tipo_particion=tipo_particion#True es fija,False es variable
        self.algoritmo_asignacion=None #1.BestF, 2 FirstF, 3 WorstF
    def comprobar_memoria(self,proc):
        if self.tipo_particion and self.algoritmo_asignacion == 1:# es fija, bestF
            diferencia=sys.maxsize
            best_part=None
            for part in self.lista_particiones:
                aux=part.get_tamano() - proc.get_tamano_proc()
                if part.get_tamano() > proc.get_tamano_proc() and part.get_estado():#particion libre
                    if aux < diferencia:
                        diferencia = aux
                        best_part = part.get_id_par()
            if best_part != None:
                part.asignar_proceso(proc)
            
            
            
                
                 
            
class Particion:
    def __init__(self,idp, tamano, dir_in,dir_fin):
        self.id_par=idp
        self.tamano_part=tamano
        self.dir_in=dir_in
        self.dir_fin=dir_fin
        self.estado=False #ocupada o libre
    def get_estado(self):
        return self.estado
    def get_tamano(self):
        return self.tamano_part
    def get_id_par(self):
        return self.get_id_par
    