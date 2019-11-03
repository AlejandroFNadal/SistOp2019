import sys
class Memoria:
    def __init__(self,tamano,tipo_particion):
        self.tamano=tamano
        self.lista_particiones=[]
        self.tipo_particion=tipo_particion#fija o variable, en texto
        self.algoritmo_asignacion=None #1.BestF, 2 FirstF, 3 WorstF
        self.lista_vacios = []
        self.ultimo_id = 0
    def asign_bestfit_fija(self,proc):
        
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
                return True
            else: 
                return False
    def asign_firstfit_fija(self,proc):
        first_part = None
        pos = 0
        while first_part == None and ( pos < len(self.lista_particiones) ):
            if self.lista_particiones[pos].get_tamano() > proc.get_tamano_proc() and self.lista_particiones[0].get_estado():
                first_part = self.lista_particiones[pos].get_id_par()
            pos += 1                
        if first_part != None:
            self.lista_particiones[first_part].asignar_proceso(proc)
            return True
        else:
            return False
    def asign_firstfit_variable(self,proc):
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
            self.generar_lista_vacios()
        return band
    def asign_worstfit_variable(self,proc):
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
                return True
        else:
            return False
        
    def comprobar_memoria(self,proc):
        state=False #variable que indica si hubo exito en asignacion de memoria
        if self.tipo_particion=="fija" and self.algoritmo_asignacion == 1:# es fija, bestF
            state=self.asign_bestfit_fija(proc)
        if self.tipo_particion=="fija" and self.algoritmo_asignacion == 2: # es fija, FIrstF
            state=self.asign_firstfit_fija(proc)
        if self.tipo_particion=="variable"and self.algoritmo_asignacion == 2: # es variable, FirstF
            if self.asign_firstfit_variable(proc) == False: #No hubo lugar donde crear particion
                self.compactar_memoria()
                if self.asign_firstfit_variable(proc) == True: 
                    state=True
                else:
                    state=False
            else:
                state=True
        if self.tipo_particion =="variable" and self.algoritmo_asignacion == 3: # es variable, worstF
            if self.asign_worstfit_variable(proc)==False:
                self.compactar_memoria()
                if self.asign_worstfit_variable(proc)==False:
                    state =False
                else:
                    state=True
            else:
                state=True
        return state #Nos devolveria false si no tuvo exito, y True si tuvo exito

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

    def compactar_memoria(self):  #supongo que la lista_vacios esta ordenada
        pos = 0
        while pos < ( len(self.lista_vacios) -1):
            if self.lista_vacios[pos][0] == ( self.lista_vacios[pos+1][0] -1 ): #Ale: aca estamos restando -1 a un
                self.lista_vacios[pos][1] = self.lista_vacios[pos+1][1] # asignamos a la direccion de fin del primer elemento la direccion de fin del segundo elemento
                self.lista_vacios[pos][2] = self.lista_vacios[pos][2] + self.lista_vacios[pos+1][2] #realizamos una suma de los tamaños
                self.lista_vacios.pop(pos+1)
            else:
                pos =+ 1

        #Se suma POS unicamente si no compacto entre 2 elementos
        #por que si compacto entre 2 elementos estaria eliminando un elemento de lista vacios
        #y si elimino un elemento de ahi, estaria decrementando en 1  en len(self.lista_vacios)

class Particion:
    def __init__(self,idp, idproc, tamano, dir_in,dir_fin, estado):
        self.id_par=idp
        self.id_proc = idproc
        self.tamano_part=tamano
        self.dir_in=dir_in
        self.dir_fin=dir_fin
        self.estado=estado #ocupada o libre
    def get_estado(self):
        return self.estado
    def get_tamano(self):
        return self.tamano_part
    def get_id_par(self):
        return self.get_id_par
    def asignar_proceso(self,idp):
        self.id_proc = idp
        self.estado = True
    def get_dir_fin(self):
        return self.dir_fin
    def get_dir_in(self):
        return self.dir_in
