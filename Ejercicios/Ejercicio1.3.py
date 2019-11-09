
import sqlite3

# creacion de BD
def crear_db():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()

    # CREACION DE LAS TABLAS
    try:
        cursor.execute("CREATE TABLE procesos (id INTEGER PRIMARY KEY UNIQUE, tamaño INTEGER)")
    except sqlite3.OperationalError:
        print("Tabla procesos ya existe.")
    else:
        print("Tabla Procesos creada exitosamente")
    try:
        cursor.execute("CREATE TABLE part_Libres (id INTEGER PRIMARY KEY AUTOINCREMENT, dir_inicio INTEGER,dir_final INTEGER, tamaño INTEGER)")
    except sqlite3.OperationalError:
        print("Tabla Particiones libres ya existe.")
    else:
        print("Tabla Particiones libres creada exitosamente")
    try:
        cursor.execute("CREATE TABLE part_Ocupadas (id INTEGER PRIMARY KEY AUTOINCREMENT, dir_inicio INTEGER, dir_final INTEGER, tamaño INTEGER, procesos_id INTEGER NOT NULL UNIQUE, FOREIGN KEY (procesos_id) REFERENCES procesos(id) )")
    except sqlite3.OperationalError:
        print("Tabla Particiones ocupadas ya existe.")
    else:
        print("Tabla Particiones ocupadas creada exitosamente")

    # COMPROBACION DE QUE ESTE RESERVADO PARA EL SISTEMA OPERATIVO
        
    cursor.execute("SELECT * FROM procesos WHERE id == 1")
    sist = cursor.fetchone()
        
    if sist is None:
        tam_memoria = int(input(("\nIntroduce el tamaño de la memoria: ")))
        sistOp = tam_memoria //10
        dir_inicio_l = (sistOp) + 1
        dir_final_l = tam_memoria
        espacio_lib = tam_memoria - sistOp

        sentencia1 = "INSERT INTO procesos(id, tamaño) VALUES (null,?)"
        cursor.execute(sentencia1,[sistOp])
        sentencia2 ="INSERT INTO part_Libres(id, dir_inicio, dir_final, tamaño) VALUES (null, ?, ?, ?)"
        cursor.execute(sentencia2,[dir_inicio_l,dir_final_l,espacio_lib])
        
        sentencia3 = "INSERT INTO part_Ocupadas(id, dir_inicio, dir_final, tamaño, procesos_id) VALUES (null, ?, ?, ?, ?)"
        cursor.execute(sentencia3,[1,sistOp, sistOp, 1])
    else:
        print("Espacio ya reservado para el Sistema Operativo")
    conexion.commit()
    conexion.close()


# CREAR PROCESOS

def crear_proceso():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
     
    id_us=int(input("\nIngrese la id del proceso: "))
    tam_us = int(input("\nIngrese el tamaño del proceso: "))
    # Se controla que el proceso no este generado aun
    try:
        sentencia = "INSERT INTO procesos(id, tamaño) VALUES (?, ?)"
        cursor.execute(sentencia, [id_us,tam_us])
        print("Se ha agregado exitosamente")
    except sqlite3.IntegrityError:
        print("El proceso {} ya existe.".format(id_us))

    conexion.commit()
    conexion.close()   

    
#AGREGAR PROCESO A LA MEMORIA

def agregar_proceso():
    # Esta basado en el algoritmo Best-Fit
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    tam = 0
    id_us = int(input("\nIngrese la id del proceso que desea cargar: "))
    sent = "SELECT * FROM procesos WHERE id == ?"
    cursor.execute(sent,[id_us])
    procesos = cursor.fetchone()
    # HAY QUE CONTROLAR SI EXISTE EL PROCESO
    try:   
        m = "SELECT * FROM part_Libres WHERE tamaño >= ? ORDER BY dir_inicio ASC"
        cursor.execute(m,[procesos[1]])
        memoria_lib = cursor.fetchone()
        # Se controla que el tamaño de la memoria es suficiente para el proceso
        if memoria_lib is not None:
            cursor.execute("SELECT * FROM part_Ocupadas")
            list_memoria_ocupada = cursor.fetchall()          
    
            d_ini = memoria_lib[1]
            d_fin = d_ini + procesos[1]
            
            # Insertamos en las particiones ocupadas    
            proc = "INSERT INTO part_Ocupadas(id, dir_inicio, dir_final, tamaño, procesos_id) VALUES (null, ?, ?, ?, ?)"
            cursor.execute(proc, [d_ini, d_fin, procesos[1], procesos[0]])

            # Actualizamos las particiones libres
            nuevo_tam = memoria_lib[3] - procesos[1]
            nueva_dir = memoria_lib[1] + procesos[1] + 1
            if nuevo_tam != 0:
                lib = "UPDATE part_Libres SET dir_inicio = ?, tamaño = ? WHERE id == ?"
                cursor.execute(lib, [nueva_dir, nuevo_tam, memoria_lib[0]])
            else:
                cursor.execute('DELETE FROM part_Libres WHERE id == ?',(memoria_lib[0],))
            print("\nProceso agregado correctamente.")
                
        else:
                print("\nError: No hay memoria disponible para agregar el proceso.")
    except sqlite3.IntegrityError:
        print("\nEl proceso {} ya esta cargado en memoria.".format(id_us))
    except TypeError:
        print("\nEl proceso {} no esta cargado.".format(id_us))
        cond = input("\nDesea agregarlo? (Y/N): ")
        if cond == "Y":
            crear_proceso() 
    conexion.commit()
    conexion.close()

# COMPACTAR MEMORIA

def compactar():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    band = True
    # Este bucle controla que cada vez que se realice una compactacion, se vuelva a realizar una consulta y generar una nueva lista de 
    # particiones libres
    while band:
        cursor.execute("SELECT * FROM part_Libres ORDER BY dir_inicio ASC")
        m_libre = cursor.fetchall()
        band = False
        id_l = 0
        d_ini =0
        d_fin=0
        tam = 0
        for i in m_libre:
            if i[1] == (d_fin +1):
                d_fin = i[2]
                tam += i[3]
                lib = "UPDATE part_Libres SET dir_final = ?, tamaño = ? WHERE id == ?"
                cursor.execute(lib, [d_fin, tam, id_l])
                cursor.execute('DELETE FROM part_Libres WHERE id == ?',(i[0],))
                band = True
                break
       
            id_l = i[0]
            d_ini = i[1]
            d_fin = i[2]
            tam = i[3]
        conexion.commit()
    print("\nCompacto realizado.")

    conexion.close()

#ELIMINAR PROCESOS
def eliminar_proceso(): 
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    eliminar = int(input("Ingrese el id del proceso a eliminar: "))
    # Se verifica que el proceso no sea el correspondiente al SO
    if eliminar != 1:
        # Buscamos el proceso
        cursor.execute('SELECT * FROM part_Ocupadas WHERE procesos_id == ?',(eliminar,))
        proceso = cursor.fetchone()
        # Se verifica que dicho proceso este cargado en memoria
        if proceso is not None:
            tam = proceso[3]
            d_ini = proceso[1]
            d_final = proceso[2]
            cursor.execute('DELETE FROM part_Ocupadas WHERE procesos_id == ?',(eliminar,))
            # INSERTAMOS LA NUEVA PARTICION LIBRE                
            lib = "INSERT INTO part_Libres(id, dir_inicio, dir_final, tamaño) VALUES (null, ?, ?, ?)"
            cursor.execute(lib,[d_ini,d_final,tam])
           
            conexion.commit()
            print("El proceso {} se ha eliminado correctamente.".format(eliminar))
        else:
            print("El proceso {} no existe en memoria.".format(eliminar))
    else:
        print("El proceso del Sistema operativo no puede ser eliminado")
    
    conexion.close()

# IMPRIMIR TABLAS
def tabla_part_libres():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM part_Libres")
    tabla = cursor.fetchall()

    print("+{:-<73}+".format(""))
    print("|{:^73}|".format("Tabla de Particiones Libres"))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<10}+".format("", "", "", ""))
    print("|{:^20}|{:^20}|{:^20}|{:^10}|".format("ID Partición", "Dirección inicio", "Dirección final", "Tamaño"))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<10}+".format("", "", "", ""))

    for id, dir_inicio, dir_final, tamaño in tabla:
        print("|{:^20}|{:^20}|{:^20}|{:^10}|".format(id, dir_inicio, dir_final, tamaño))
    
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<10}+".format("", "", "", ""))


def tabla_part_ocupadas():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM part_Ocupadas")
    tabla = cursor.fetchall()

    print("+{:-<94}+".format(""))
    print("|{:^94}|".format("Tabla de Particiones Ocupadas"))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<10}+{:-<20}+".format("", "", "", "", ""))
    print("|{:^20}|{:^20}|{:^20}|{:^10}|{:^20}|".format("ID Partición", "Dirección inicio", "Dirección final", "Tamaño", "ID Proceso"))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<10}+{:-<20}+".format("", "", "", "", ""))

    for id, dir_inicio, dir_final, tamaño, procesos_id in tabla:
        print("|{:^20}|{:^20}|{:^20}|{:^10}|{:^20}|".format(id, dir_inicio, dir_final, tamaño, procesos_id))
    
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<10}+{:-<20}+".format("", "", "", "", ""))

#Proceso principal

conexion = sqlite3.connect("memoria.db")
cursor = conexion.cursor()
print("\nBienvenido al gestor de memoria")
cond = input("\nDesea operar con una base de datos nueva?(Y/N): ")
if cond == "Y" or "y":
    crear_db()
    


while True:
    print("\n")
    tabla_part_libres()
    print("\n")
    tabla_part_ocupadas()
    opcion = input("\nIntroduce una opcion:\n[1] Crear un proceso\n[2] Agregar un proceso a la memoria\n[3] Eliminar proceso\n[4] Compactar memoria\n[5] Salir del programa\n\n")
    if opcion == "1":
        crear_proceso()
    elif opcion == "2":
        agregar_proceso()        
    elif opcion == "3":
        eliminar_proceso()
    elif opcion == "4":
        compactar()         
    elif opcion == "5":
        break
    else:
        print("Opcion incorrecta")


conexion.close()