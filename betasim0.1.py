import sqlite3
from sqlite3 import Error
 
class Procesador:#contendra gran parte de las tareas generales
    def __init__(self):
    	self.procesos_listos=[]
    def add_proceso(self,proceso):
        self.procesos_listos.append(proceso)
    def show_procesos(self):
        print("ID    Pro_Tam    Prioridad  Tiempo de Arribo  Secuencia")
        for x in self.procesos_listos:
            x.muestra_proceso()

class Proceso: #Contiene los datos esenciales de un proceso
    def __init__(self,datos):
    	self.id=datos[0]
    	self.Pro_tam=datos[1]
    	self.Prioridad=datos[2]
    	self.TiempoArribo=datos[3]
    	self.Secuencia=datos[4]
    def muestra_proceso(self):
        print(str(self.id)+"       "+str(self.Pro_tam)+"       "+str(self.Prioridad)+"       "+str(self.TiempoArribo)+"       "+str(self.Secuencia))

class Interface:
    def __init__(self):
        self.conn = None
    def create_connection(self,db_file):
        """ create a database connection to a SQLite database """
        
        try:
            self.conn = sqlite3.connect(db_file)
            print("Successfully connected to Database")
        except Error as e:
            print(e)
        return self.conn
    def compruebaParticion(self,tamano,inicio,fin,memoria):
        #Esta funcion comprueba si la particion fija introducida puede caber en donde se la puso. Falta hacer
        return True
    def cargar_preset(self):
        ##Esta funcion devuelve una lista con tres sublistas. La sublista preset, la sublista particiones y la sublista procesos.
        currentPreset=self.retrieve_cantidadPresets()+1
        particiones=[]
        procesos=[]
        tempParticion=[]
        data=[] #lista a devolver
        continuar=True
        memoria=[]#Lista que describe la memoria byte por byte
        print("Inserte una descripcion de su preconfiguracion")
        descripcion=input()
        print("Ingrese la cantidad de memoria en bytes")
        tamMemoria=int(input())
        for i in range(0,tamMemoria):
            memoria.append("_")
        print("Inserte el porcentaje de memoria perteneciente al sistema operativo")
        sistopmem=int(input())
        for i in range(0,round(tamMemoria*sistopmem/100)):
            memoria[i]="S"
        print("Ingrese el algoritmo de asignacion de procesos a particiones. 1:BestFit 2: FirstFit 3:Worstfit")
        algoritmo=int(input())
        print("Particiones fijas o variables:[f/V]")#En CLI, la mayuscula implica que es una opcion automatica
        fija_variable=input()
        
        if fija_variable == "f":

            #Aca se cargan particiones fijas
            idparticion=0
            memoriaRestante=tamMemoria-(tamMemoria*sistopmem/100)
            print("Ingrese numero de particiones")
            numero_particiones=int(input())
            while continuar:
                print("Ingrese tamano particion")
                tempTamParticion=int(input())
                print("Ingrese punto de inicio de particion")
                puntoInicio=int(input())
                print("Ingrese punto de fin")
                puntoFin=int(input())
                if self.compruebaParticion(tempTamParticion,puntoInicio,puntoFin,memoria):
                    particiones.append([idparticion,tempTamParticion,puntoInicio,puntoFin])
                else:
                    print("Ingresar particion mas chica")
                print("Desea ingresar otra particion[y/n]")
                idparticion+=1
                if input()=="n":
                    continuar=False
            print(particiones)
            
        else:
            fija_variable="v"
            numero_particiones=0
        data.append([currentPreset,descripcion,tamMemoria,sistopmem,fija_variable,numero_particiones,algoritmo])
        data.append(particiones)
        #Aca se cargan procesos
        continuar=True
        idproceso=0
        while continuar:
            print("Ingrese tamano proceso")
            psize=int(input())
            print("Ingrese prioridad: 1-3")
            prioridad=int(input())
            print("Ingrese tiempo de arribo a la cola de listos")
            tiempoArribo=int(input())
            print("Ingrese secuencia de eventos. C es CPU, I es entrada, O es salida. Ej: C10-I3-C5-S23")
            secuencia=input()
            procesos.append([idproceso,psize,prioridad,tiempoArribo,secuencia])
            print("Quiere agregar otro proceso [y/n]")
            if input() != "y":
                continuar=False
        data.append(procesos)
        return data
    def show_menu(self):
        print("1.Crear nueva preconfiguracion")
        print("2.Mostrar lista de parametros iniciales preexistentes")
        decision=int(input())
        if decision == 1:
            preset=self.cargar_preset()
            self.guardarEnBDPreset(preset)
    def retrieve_data(self,procesador):
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT * FROM Procesos")
        rows=self.cur.fetchall()
        for row in rows:
            a=Proceso(row)
            procesador.add_proceso(a)
    def retrieve_cantidadPresets(self):
        self.cur=self.conn.cursor()
        return self.cur.execute("SELECT COUNT(*) FROM Preset").fetchall()[0][0]
    def guardarEnBDPreset(self,datos):
        self.cur=self.conn.cursor()
        print(datos[0])
        self.cur.execute("INSERT INTO Preset(id,desc,memoria,porc_so,fija_variable,cant_part,algoritmo) VALUES(?,?,?,?,?,?,?)",(datos[0][0],datos[0][1],datos[0][2],datos[0][3],datos[0][4],datos[0][5],datos[0][6]))
        self.conn.commit()
            
        
#Este main solo representa una prueba de las clases existentes, no se planea implementar de esta forma.
if __name__ == '__main__':
    conexion=Interface()
    conn=conexion.create_connection("/root/Documents/UTN/SistOp2019/SistOp.db")
    Core=Procesador()
    conexion.show_menu()
    
    #conexion.retrieve_data(Core)
    #a=Proceso(1,30,10,10,10)
    #Core.add_proceso(a)
    #Core.show_procesos()
        
    #curr=conn.cursor()
    #print(curr.execute("SELECT * FROM Procesos2"))
