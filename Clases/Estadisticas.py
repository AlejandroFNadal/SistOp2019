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
        dic_TE = {}
        list_TE = []
        # Tiempo de retorno
        dic_TR = {}
        list_TR =[]
        # tiempo de CPU
        cpu = 0
        #Lista de colores
        list_colors_TE = []
        list_colors_TR = []
        # np.random.rand(3,)
        # funcion para buscar en la lista
        def buscar(self,valor,lista):
            res = False
            for dic in lista:
                if dic.has_key(valor):
                    res = True
            return res

        def sumar(self, key, lista):
            for l in lista:
                if l['id_p'] == key:
                    l['tiempo'] +=1
                
        


        for mat in cubo:
            for f in mat:
                if f[1] == 2: #LISTO
                    if buscar(f[0], list_TE):
                        sumar(f[0],list_TE)
                    else:
                        dic_TE = {}
                        dic_TE['id_p'] = f[0]
                        dic_TE['tiempo'] = 1
                        list_colors_TE.append(np.random.rand(3,))
                        list_TE.append(dic_TE)

                if f[1] != 4: # Terminado
                    if f[0] in list_TR:
                        dic_TR['tiempo'] +=1
                    else:
                        dic_TR = {}
                        dic_TR['id_p'] = f[0]
                        dic_TR['tiempo'] = 1
                        list_colors_TE.append(np.random.rand(3,))
                    list_TR.append(dic_TR)
                if f[1] == 5:
                    cpu +=1
            
        
        # Recorro las listas
        print (" TIEMPO DE ESPERA ")
        for i in list_TE:
            for key in i:
                print(key, ":", i[key])
        print(" TIEMPO RETORNO ")
        #for l in list_TR:
         #   print("Proceso: " + str(l['id_p']) + " "+ str(l['tiempo']))
        print("CPU total = "+ str(cpu))

    
    