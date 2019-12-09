from matplotlib import pyplot
import numpy as np
from config import FILE_TE, FILE_TR

#               Tiempo de espera de cada proceso
# es el tiempo en el que esta en el estado "Listo"
#               Tiempo de retorno
# tiempo que transcurre desde la creacion del proceso hasta que termina la ejecucion del mismo
#           Porcentaje de utilizacion de CPU
# tiempo en que la CPU esta ocupada
class Estadisticas:
    def est_T_R(self,cubo):
        
        # Tiempo de retorno
        
        list_TR =[]
        # tiempo de CPU
        cpu = 0
        #Lista de colores
        
        list_colors_TR = []
        # tiempo total de ejecucion
        clk = 0
                 

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
                       
                                
                if f[1] == 5:
                    cpu +=1
            clk +=1
        #Calculamos el porcentaje de uso de la CPU
        porc_cpu = (cpu*100)/clk

        

        # Dibujamos el porcentaje de Tiempo de Retorno
        self.dibujar_retorno(list_TR,list_colors_TR,'Tiempo de Retorno',clk,porc_cpu, FILE_TR)
        
        # Recorro las listas
        
        #print (" TIEMPO DE ESPERA ")
        #for i in list_TE:
        #    for key in i:
        #        print(key, ":", i[key])
                
        print(" TIEMPO RETORNO ")
        for l in list_TR:
            for key in l:
                print(key, ":", l[key])
        print("CPU total = "+ str(cpu))

    
    def est_T_E(self,cubo):
        # Tiempo de espera
        
        list_TE = []
        # tiempo de CPU
        cpu = 0
        #Lista de colores
        list_colors_TE = []
        
        # tiempo total de ejecucion
        clk = 0
                 

        for mat in cubo:
            for f in mat:
                
                       
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
            clk +=1
        #Calculamos el porcentaje de uso de la CPU
        porc_cpu = (cpu*100)/clk
        # Dibujamos el porcentaje de Tiempo de Espera de cada proceso
        self.dibujar_espera(list_TE,list_colors_TE,'Tiempo de Espera',clk,porc_cpu, FILE_TE)

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
    
    def func(self,pct,valores):
        absoluto = int(pct/100.*np.sum(valores))
        return "{:.1f}%\n({:d})".format(pct, absoluto)
    
    def dibujar_espera(self, lista, lista_colores, titulo,clk,porc_cpu, FILE):
        # se realiza una lista para las id y otra para los tiempos
        l_id = []
        l_tiempo = []
        for l in lista:
            l_id.append('P'+str(l['id_p']))
            l_tiempo.append(l['tiempo'])

        pyplot.figure(200) 
        pyplot.pie(l_tiempo, colors= lista_colores,labels = l_id, autopct=lambda pct: self.func(pct, l_tiempo) )
        pyplot.axis('equal')
        pyplot.title(titulo+'\n\nTiempo total = '+str(clk)+' Porcentaje CPU = '+str(round(porc_cpu,2))+'%')
        pyplot.savefig(FILE)
        print("fin")
    
    def dibujar_retorno(self, lista, lista_colores, titulo,clk,porc_cpu, FILE):
        # se realiza una lista para las id y otra para los tiempos
        l_id = []
        l_tiempo = []
        for l in lista:
            l_id.append('P'+str(l['id_p']))
            l_tiempo.append(l['tiempo'])

               
        pyplot.pie(l_tiempo, colors= lista_colores,labels = l_id, autopct=lambda pct: self.func(pct, l_tiempo) )
        pyplot.axis('equal')
        pyplot.title(titulo+'\n\nTiempo total = '+str(clk)+' Porcentaje CPU = '+str(round(porc_cpu,2))+'%')
        pyplot.savefig(FILE)
        
