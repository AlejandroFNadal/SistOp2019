IDPart=0
Inicio=1
Fin=2
Estado=3
Proceso=4
Tamano=5
IntCompact=6
print("Ingrese tamano de memoria");
tamMemoria=int(input())
print("Ingrese cantidad de particiones");
cantParticiones=int(input())

sistOp=tamMemoria//10
idParticionActual=0
posicionActualMemoria=sistOp
#Crear memoria vacia
memoria=[]
tablaParticiones=[]
tablaProcesos=[]
i = 0

def imprimeProcesos(tabla):
    print("Tabla de Procesos")
    print("ID    Particion    Tamano")
    print("-------------------------------------")
    for i in tabla:
        print(i)
    print("----------------------------------------")

def bestFit(tabla,sizeProceso):
    mejorParticion=-1 #MaxValue
    tamanoMejorParticion=10000
    for i in tabla:
        if i[3] == False:
            print("Particion "+str(i[0])+"... Analizando")
            if i[5] >= sizeProceso and i[5] <= tamanoMejorParticion:
                mejorParticion=i[0]
                tamanoMejorParticion=i[Tamano]
    if mejorParticion==-1:
        return False
    else:
        print(tamanoMejorParticion)
        tabla[mejorParticion][3]=True
        tabla[mejorParticion][4]= len(tablaProcesos)
        tablaProcesos.append([tabla[mejorParticion][4],mejorParticion,sizeProceso])
        tabla[mejorParticion][IntCompact]=tabla[mejorParticion][Tamano]-sizeProceso
        imprimeProcesos(tablaProcesos)
        return True
    

def imprimeTabla(tabla):
    print("Tabla de Particiones")
    print("ID    Inicio    Fin    Estado     Proceso  Tamano   Compactacion int")
    print("-------------------------------------")
    for i in tabla:
        print("        ".join(str(x) for x in i))
    print("----------------------------------------")
def imprimememoria(mem):
    print("Memoria")
    print("-------------------------------")
    print(mem)
    print("-------------------------------")
          
for i in range(0,sistOp):
        memoria.append("S")
for i in range(sistOp,tamMemoria):
    memoria.append("_")
imprimememoria(memoria)

tamanoRestanteMemoria=tamMemoria-sistOp
continuar = True
while continuar and cantParticiones > 0:
    print("Desea crear otra particion? Y/N")
    decision=input()
    if decision == "Y":
        print("Ingresar tamano de particion")
        tamanoNuevaParticion=int(input())
        if tamanoNuevaParticion <= (tamanoRestanteMemoria-cantParticiones) and tamanoNuevaParticion > 0:#esto se asegura de dejar aunque sea un byte para cada particion restante.
            tablaParticiones.append([idParticionActual,posicionActualMemoria,posicionActualMemoria+tamanoNuevaParticion-1,False,-1, tamanoNuevaParticion,-1])
            for i in range(posicionActualMemoria,posicionActualMemoria+tamanoNuevaParticion):
                memoria[i]=idParticionActual
            posicionActualMemoria+=tamanoNuevaParticion
            cantParticiones-=1
            idParticionActual+=1
            
        else:
            if tamanoNuevaParticion > (tamanoRestanteMemoria-cantParticiones):
                print("Particion muy grande. Error")
            else:
                print("Particion demasiado pequena")
            
    else:
        continuar=False
    imprimememoria(memoria)
    imprimeTabla(tablaParticiones)


continuar = True

while continuar == True:
    print("Ingresar Tamaño proceso")
    nuevoProcesoTamano=int(input())
    if bestFit(tablaParticiones,nuevoProcesoTamano) == True:
        print("Proceso insertado con exito")
    else:
        print("No Hay espacio. Compactando")
        compactar()
        if bestFit(tablaParticiones,nuevoProcesoTamano) == True:
            print("Proceso insertado con exito")
        else:
            print("No hay espacio. Imposible insertar")
    imprimememoria(memoria)
    imprimeTabla(tablaParticiones)
    print("Desea agregar otro proceso?")
    if input()!="y":
        continuar = False
