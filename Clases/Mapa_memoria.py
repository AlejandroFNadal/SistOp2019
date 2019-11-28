import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Mapa_memoria:

    def mapa_memoria(self, tabla):
        
        clk=0
        # Solamente recorre la tabla y muestra los datos
        print("<<<<IMPRIME TABLA DE MEMORIA>>>>")
        for i in tabla:
            print("Clk: "+str(clk))
            for x in i:
                print("====")
                print("Id particion: " +str(x['id_par'])+ "  tamaño: " +str(x['tama']) + "Estado: "+ str(x['estado']) + " Proceso" +str(x['proceso']) )
            clk +=1