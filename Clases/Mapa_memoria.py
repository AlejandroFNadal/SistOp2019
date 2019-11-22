

class Mapa_memoria:

    def mapa_memoria(self, tabla):
        
        clk=0
        # Solamente recorre la tabla y muestra los datos
        print("<<<<IMPRIME TABLA DE MEMORIA>>>>")
        for i in tabla:
            print("Clk: "+str(clk))
            for x in i:
                
                print("Id particion: " +str(x[0])+ "  tamaño: " +str(x[1]) + "Estado: "+ str(x[4]) )
            clk +=1