import sqlite3
from sqlite3 import Error
from Clases.Procesos import *
from Clases.Procesador import *
from Clases.Interface import *


# Este main solo representa una prueba de las clases existentes, no se
# planea implementar de esta forma.
if __name__ == '__main__':
    conexion = Interface()
    conn = conexion.create_connection(
        "/root/Documents/UTN/SistOp2019/SistOp.db")
    Core = Procesador()
    conexion.show_menu()

    # conexion.retrieve_data(Core)
    # a=Proceso(1,30,10,10,10)
    # Core.add_proceso(a)
    # Core.show_procesos()

    # curr=conn.cursor()
    #print(curr.execute("SELECT * FROM Procesos2"))
