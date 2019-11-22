class Mapa_memoria:

    def mapa_memoria(self, tabla):
        

        # Solamente recorre la tabla y muestra los datos
        for i in tabla:
            print("<<<<IMPRIME TABLA DE MEMORIA>>>>")
            for x in i:
                id = x[0]
                print("Id particion: " +str(id))