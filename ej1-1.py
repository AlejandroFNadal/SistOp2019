#Simular la administración de la asignación de memoria particionada fija con particiones de DIFERENTES tamaños.
#Pedir memoria contigua que simule la memoria RAM de la máquina. El 10 % de dicha memoria será destina al núcleo
#del Sistema Operativo. Ingresar la cantidad de particiones fijas en la cuál se dividirá la memoria de Usuario.
#Generar el Id de la partición automáticamente. Actualizar las la tabla de particiones. La tabla de particiones
#contendrá la siguiente información (id partición, dirección de comienzo de la partición, estado de la partición).
#Mostrar la información contenida en la tabla de particiones.
#Ejercicio Practico 1.1 Sist Op
print("Ingrese tamano de memoria")
tamMemoria=int(input())
print("Ingrese cantidad de particiones")
cantParticiones=int(input())

sistOp=tamMemoria//10
cantParticiones-=1 #Considerando que el espacio de sistema es una particion tambien
idParticionActual=1
posicionActualMemoria=sistOp
#Crear memoria vacia
memoria=[]
tablaParticiones=[]
i = 0

def imprimeTabla(tabla):
    print("Tabla de Particiones")
    print("ID    Inicio    Fin")
    print("-------------------------------------")
    print(tabla)
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
    print("Desea crear otra particion? Y/N") #Seria asignar tamaño a particion?
    decision=input()
    if decision == "Y":
        print("Ingresar tamano de particion")
        tamanoNuevaParticion=int(input())
        if tamanoNuevaParticion <= (tamanoRestanteMemoria-cantParticiones) and tamanoNuevaParticion > 0:#esto se asegura de dejar aunque sea un byte para cada particion restante.
            tablaParticiones.append([idParticionActual,posicionActualMemoria,posicionActualMemoria+tamanoNuevaParticion])
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

    
