from matplotlib import pyplot
import numpy as np

#               Tiempo de espera de cada proceso
# es el tiempo en el que esta en el estado "Listo"
#               Tiempo de retorno
# tiempo que transcurre desde la creacion del proceso hasta que termina la ejecucion del mismo
#           Porcentaje de utilizacion de CPU
# tiempo en que la CPU esta ocupada
class Estadisticas:
    def est(self,cubo):
        # Tiempo de espera
        
        list_TE = []
        # Tiempo de retorno
        
        list_TR =[]
        # tiempo de CPU
        cpu = 0
        #Lista de colores
        list_colors_TE = []
        list_colors_TR = []
        # np.random.rand(3,)
        # funcion para buscar en la lista
        
                 
        


        for mat in cubo:
            for f in mat:
                if f[1] != 4: # Terminado
                    if self.buscar(f[0],list_TR):
                        self.sumar(f[0],list_TR)
                    else:
                        dic_TR = {}
                        dic_TR['id_p'] = f[0]
                        dic_TR['tiempo'] = 1
                        list_colors_TR.append(np.random.rand(3,))
                        list_TR.append(dic_TR)
                       
                if f[1] == 2: #LISTO
                    if self.buscar(f[0], list_TE):
                        self.sumar(f[0],list_TE)
                    else:
                        dic_TE = {}
                        dic_TE['id_p'] = f[0]
                        dic_TE['tiempo'] = 1
                        list_colors_TE.append(np.random.rand(3,))
                        list_TE.append(dic_TE)

                
                if f[1] == 5:
                    cpu +=1
        
        # Dibujamos el porcentaje de Tiempo de Espera de cada proceso
        self.dibujar(list_TE,list_colors_TE,'Tiempo de Espera')
        # Dibujamos el porcentaje de Tiempo de Retorno
        self.dibujar(list_TR,list_colors_TR,'Tiempo de Retorno')
        
        # Recorro las listas
        
        print (" TIEMPO DE ESPERA ")
        for i in list_TE:
            for key in i:
                print(key, ":", i[key])
                
        print(" TIEMPO RETORNO ")
        for l in list_TR:
            for key in l:
                print(key, ":", l[key])
        print("CPU total = "+ str(cpu))


    def buscar(self,valor,lista):
            res = False
            for dic in lista:
                if dic['id_p']==valor:
                    res = True
            return res
    
    def sumar(self, key, lista):
            for l in lista:
                if l['id_p'] == key:
                    l['tiempo'] +=1
    
    def dibujar(self, lista, lista_colores, titulo):
        # se realiza una lista para las id y otra para los tiempos
        l_id = []
        l_tiempo = []
        for l in lista:
            l_id.append('P'+str(l['id_p']))
            l_tiempo.append(l['tiempo'])
        
        pyplot.pie(l_tiempo, colors= lista_colores,labels = l_id, autopct='%1.1f%%' )
        pyplot.axis('equal')
        pyplot.title(titulo)
        pyplot.show()
        
