import sqlite3
from sqlite3 import Error
 
class Procesador:#contendra gran parte de las tareas generales
    def __init__(self):
    	self.procesos_listos=[]
    def add_proceso(self,proceso):
        self.procesos_listos.append(proceso)
    def show_procesos(self):
        print("ID    MemSize    Input   CPUTime    Output")
        for x in self.procesos_listos:
            x.muestra_proceso()

class Proceso: #Contiene los datos esenciales de un proceso
    def __init__(self,datos):
    	self.id=datos[0]
    	self.memSize=datos[1]
    	self.InSize=datos[2]
    	self.CPUSize=datos[3]
    	self.OutSize=datos[4]
    def muestra_proceso(self):
        print(str(self.id)+"       "+str(self.memSize)+"       "+str(self.InSize)+"       "+str(self.CPUSize)+"       "+str(self.OutSize))

class Interface:
    def create_connection(self,db_file):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print("Successfully connected to Database")
        except Error as e:
            print(e)
        return self.conn
    def show_menu(self):
        print("1.Seleccionar parametros iniciales")
        print("2.Mostrar lista de parametros iniciales preexistentes")
	#def retrieve_data(self):
    def retrieve_data(self,procesador):
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT * FROM Procesos")
        rows=self.cur.fetchall()
        for row in rows:
            a=Proceso(row)
            procesador.add_proceso(a)
            
        
#Este main solo representa una prueba de las clases existentes, no se planea implementar de esta forma.
if __name__ == '__main__':
    conexion=Interface()
    conn=conexion.create_connection("/root/Documents/UTN/SistOp2019/SistOp.db")
    Core=Procesador()
    conexion.retrieve_data(Core)
    #a=Proceso(1,30,10,10,10)
    #Core.add_proceso(a)
    Core.show_procesos()
        
    #curr=conn.cursor()
    #print(curr.execute("SELECT * FROM Procesos2"))
