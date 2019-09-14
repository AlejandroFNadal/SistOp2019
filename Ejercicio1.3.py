
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
        print("Taba Procesos creada exitosamente")
    try:
        cursor.execute("CREATE TABLE part_Libres (id INTEGER PRIMARY KEY AUTOINCREMENT, dir_inicio INTEGER, tamaño INTEGER)")
    except sqlite3.OperationalError:
        print("Taba Particiones libres ya existe.")
    else:
        print("Taba Particiones libres creada exitosamente")
    try:
        cursor.execute("CREATE TABLE part_Ocupadas (id INTEGER PRIMARY KEY AUTOINCREMENT, dir_inicio INTEGER, tamaño INTEGER, procesos_id INTEGER NOT NULL, FOREIGN KEY (procesos_id) REFERENCES procesos(id) )")
    except sqlite3.OperationalError:
        print("Taba Particiones ocupadas ya existe.")
    else:
        print("Taba Particiones ocupadas creada exitosamente")

    # COMPROBACION DE QUE ESTE RESERVADO PARA EL SISTEMA OPERATIVO
        
    cursor.execute("SELECT * FROM procesos WHERE id == 1")
    sist = cursor.fetchone()
        
    if sist is None:
        tam_memoria = int(input(("\nIntroduce el tamaño de la memoria: ")))
        sistOp = tam_memoria //10
        dir_inicio_l = (sistOp) + 1

        espacio_lib = tam_memoria - sistOp

        sentencia1 = "INSERT INTO procesos(id, tamaño) VALUES (null,?)"
        cursor.execute(sentencia1,[sistOp])
        sentencia2 ="INSERT INTO part_Libres(id, dir_inicio, tamaño) VALUES (null, ?, ?)"
        cursor.execute(sentencia2,[dir_inicio_l,espacio_lib])

        sentencia3 = "INSERT INTO part_Ocupadas(id, dir_inicio, tamaño, procesos_id) VALUES (null, ?, ?, ?)"
        cursor.execute(sentencia3,[1, sistOp, 1])
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
    sentencia = "INSERT INTO procesos(id, tamaño) VALUES (?, ?)"
    cursor.execute(sentencia, [id_us,tam_us])
    print("Se ha agregado exitosamente")

    conexion.commit()
    conexion.close()   

    
#AGREGAR PROCESO A LA MEMORIA

def agregar_proceso():
    
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    tam = 0
    id_us = int(input("\nIngrese la id del proceso que desea cargar: "))
    sent = "SELECT * FROM procesos WHERE id == ?"
    cursor.execute(sent,[id_us])
    procesos = cursor.fetchone()
      # HAY QUE CONTROLAR SI EXISTE EL PROCESO
    try:   
        cursor.execute("SELECT * FROM part_Libres")
        memoria_lib = cursor.fetchone()
        cursor.execute("SELECT * FROM part_Ocupadas")
        list_memoria_ocupada = cursor.fetchall()
        for mem in list_memoria_ocupada:
            tam += mem[2]
    
        d_ini = tam+1

      # Se controla que el tamaño de la memoria es suficiente para el proceso
        if memoria_lib[2]>0:
            if procesos[1] <= memoria_lib[2]:
                proc = "INSERT INTO part_Ocupadas(id, dir_inicio, tamaño, procesos_id) VALUES (null, ?, ?, ?)"
                cursor.execute(proc, [d_ini, procesos[1], procesos[0]])
                # Actualizamos las particiones libres
                nuevo_tam = memoria_lib[2] - procesos[1]
                nueva_dir = memoria_lib[1] + procesos[1] + 1
                lib = "UPDATE part_Libres SET dir_inicio = ?, tamaño = ? WHERE id == 1"
                cursor.execute(lib, [nueva_dir, nuevo_tam])
                print("Proceso agregado correctamente.")
            else:
                print("Error: Memoria insuficiente para agregar ese proceso.")
        else:
            print("Error: No hay memoria disponible para agregar un proceso.")
    except:
        print("El proceso {} no esta cargado.".format(id_us))
        cond = input("\nDesea agregarlo? (Y/N): ")
        if cond == "Y":
            crear_proceso()

    conexion.commit()
    conexion.close()

# IMPRIMIR TABLAS
def tabla_part_libres():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM part_Libres")
    tabla = cursor.fetchall()

    print("+{:-<52}+".format(""))
    print("|{:^52}|".format("Tabla de Particiones Libres"))
    print("+{:-<20}+{:-<20}+{:-<10}+".format("", "", ""))
    print("|{:^20}|{:^20}|{:^10}|".format("ID Partición", "Dirección inicio", "Tamaño"))
    print("+{:-<20}+{:-<20}+{:-<10}+".format("", "", ""))

    for id, dir_inicio, tamaño in tabla:
        print("|{:^20}|{:^20}|{:^10}|".format(id, dir_inicio, tamaño))
    
    print("+{:-<20}+{:-<20}+{:-<10}+".format("", "", ""))


def tabla_part_ocupadas():
    conexion = sqlite3.connect("memoria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM part_Ocupadas")
    tabla = cursor.fetchall()

    print("+{:-<73}+".format(""))
    print("|{:^73}|".format("Tabla de Particiones Ocupadas"))
    print("+{:-<20}+{:-<20}+{:-<10}+{:-<20}+".format("", "", "", ""))
    print("|{:^20}|{:^20}|{:^10}|{:^20}|".format("ID Partición", "Dirección inicio", "Tamaño", "ID Proceso"))
    print("+{:-<20}+{:-<20}+{:-<10}+{:-<20}+".format("", "", "", ""))

    for id, dir_inicio, tamaño, procesos_id in tabla:
        print("|{:^20}|{:^20}|{:^10}|{:^20}|".format(id, dir_inicio, tamaño, procesos_id))
    
    print("+{:-<20}+{:-<20}+{:-<10}+{:-<20}+".format("", "", "", ""))

#Proceso principal

conexion = sqlite3.connect("memoria.db")
cursor = conexion.cursor()
print("\nBienvenido al gestor de memoria")
cond = input("\nDesea operar con una base de datos nueva?(Y/N): ")
if cond == "Y":
    crear_db()
    


while True:
    print("\n")
    tabla_part_libres()
    print("\n")
    tabla_part_ocupadas()
    opcion = input("\nIntroduce una opcion:\n[1] Crear un proceso\n[2] Agregar un proceso a la memoria\n[3] Salir del programa\n\n")
    if opcion == "1":
        crear_proceso()
    elif opcion == "2":
        agregar_proceso()        
    elif opcion == "3":
        break
    else:
        print("Opcion incorrecta")


conexion.close()