import sys
class Memoria:
    def __init__(self,tamano,tipo_particion):
        self.tamano=tamano
        self.lista_particiones=[]
        self.tipo_particion=tipo_particion#True es fija,False es variable
        self.algoritmo_asignacion=None #1.BestF, 2 FirstF, 3 WorstF
        self.lista_vacios = []
        self.ultimo_id = 0
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
                self.lista_particiones[best_part].asignar_proceso(proc) #falta hacer asignar_proceso
            
        if self.tipo_particion and self.algoritmo_asignacion == 2: # es fija, FIrstF
            first_part = None
            pos = 0
            while first_part == None and ( pos < len(self.lista_particiones) ):
                if self.lista_particiones[pos].get_tamano() > proc.get_tamano_proc() and self.lista_particiones[0].get_estado():
                    first_part = self.lista_particiones[pos].get_id_par()
                pos += 1                
            if first_part != None:
                self.lista_particiones[first_part].asignar_proceso(proc)

        if not self.tipo_particion and self.algoritmo_asignacion == 2: # es variable, FirstF
            band = False
            pos = 0
            while  band == False and (pos < len(self.lista_vacios) ):
                if self.lista_vacios[pos][2] > proc.get_tamano_proc():
                    part_nueva = Particion(self.ultimo_id,proc.get_id(),proc.get_tamano_proc(),self.lista_vacios[pos][0],self.lista_vacios[pos][1],True)
                    pos_LO = 0 #pos_LO = posicion lista ordenada
                    while pos_LO < len(self.lista_particiones) and part_nueva.get_dir_in() >= self.lista_particiones[pos_LO].get_dir_fin():
                        pos_LO =+ 1
                    self.lista_particiones.insert(pos_LO,part_nueva)
                    band = True
                pos +=1
            if band == False:
                self.compactar_memoria()
                #falta repetir lo de arriba
            self.generar_lista_vacios()

        if not self.tipo_particion and self.algoritmo_asignacion == 3: # es variable, worstF
            aux_variable = sorted(self.lista_vacios, key = self.obt_tam_part, reversed = True )
            band_asignacion = False
            if aux_variable[0][3] > proc.get_tamano_proc():
                part_nueva = Particion(self.ultimo_id,proc.get_id(),proc.get_tamano_proc(),aux_variable[0][0],aux_variable[0][1],True)
                pos_LO = 0 #pos_LO = posicion lista ordenada
                while pos_LO < len(self.lista_particiones) and part_nueva.get_dir_in() >= self.lista_particiones[pos_LO].get_dir_fin():
                    pos_LO =+ 1
                    if part_nueva.get_dir_in() < self.lista_particiones[pos_LO].get_dir_fin():
                        band_asignacion = True

                if band_asignacion:
                    self.lista_particiones.insert(pos_LO,part_nueva)
                    self.generar_lista_vacios()
            else:
                self.compactar_memoria()
                #falta repetir lo de arriba

    def generar_lista_vacios(self):
        pos = 0
        while pos < len(self.lista_particiones) - 1: #si esta en la lista de particiones, es porque la particion esta ocupada
            if (self.lista_particiones[pos+1].get_dir_in() - self.lista_particiones[pos].get_dir_fin()) > 1:
                dirIn = self.lista_particiones[pos].get_dir_fin() + 1
                dirFin = self.lista_particiones[pos+1].get_dir_in()-1
                self.lista_vacios.append([dirIn,dirFin,dirFin-dirIn+1])
            pos += 1

            
    def obt_tam_part(self,elem):
        return elem[2]

    def compactar_memoria(self):
        pass


class Particion:
    def __init__(self,idp, idproc, tamano, dir_in,dir_fin):
        self.id_par=idp
        self.id_proc = idproc
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
    def asignar_proceso(self,idp):
        self.id_proc = idp
        self.estado = True
