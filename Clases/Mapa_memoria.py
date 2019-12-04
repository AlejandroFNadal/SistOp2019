import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from config import FILE_MAPA

class Mapa_memoria:

    
	def mapa_memoria(self, tabla):
		ult_col = 0
		clk=0
		for i in tabla:
			# Declaring a figure "gnt" 
			fig, gnt = plt.subplots()
			# Setting Y-axis limits 
			gnt.set_ylim(0, 50) 

			# Setting X-axis limits 
			gnt.set_xlim(0, 160) 

			# Setting labels for x-axis and y-axis 
			gnt.set_xlabel('Tamaño particiones') 
			gnt.set_ylabel('Particiones') 

			# Setting ticks on y-axis 
			gnt.set_yticks([15]) 
			# Labelling tickes of y-axis 
			gnt.set_yticklabels(['p'])

			# Setting graph attribute 
			gnt.grid(True) 
			Alt = (15,9) #Parametro para ubicar en el eje y, y la altura que tendra
			
			# Solamente recorre la tabla y muestra los datos
			print("<<<<IMPRIME TABLA DE MEMORIA>>>>")

			print("Clk: "+str(clk))
			leyenda = []
			for x in i:
				print("====")
				color = self.get_color(x['id_par'])
				tam= (x['dir_ini'], x['tama']) #Donde inicia la particion y su tamaño
				print("Dir inicio: " +str(x['dir_ini'])+ "  tamaño: " +str(x['tama']) + " Estado: "+ str(x['estado']) + " Proceso " +str(x['proceso']) )
				if x['estado']:
					gnt.broken_barh([tam], Alt, color = color)
					leyenda.append(mpatches.Patch(color = color, label ='P'+ str(x['proceso'])))
				else:
					gnt.broken_barh([tam], Alt, color = '#FBFCF7')
					#leyenda.append(mpatches.Patch(color = color, label ='P'+ str(x['proceso'])))
				#plt.pause(0.5)
				ult_col += 1
			plt.legend(handles=leyenda)
			print("Ruta mapa: " + FILE_MAPA+str(clk)+'.png')
			plt.savefig(FILE_MAPA +str(clk)+'.png')
			clk +=1
	#plt.show()
        
    
     
	def get_color(self,ult_col):
		ultimo_color = ult_col
		lista_colores = ['#C14242', '#3FBF7F', '#3FBFBF', '#BF3FBF','#DA842E', '#2E2EDA', '#F7F768',
			'#EF84D1','#C4E07F', '#DC9883']
		if ultimo_color >9:
			l = ultimo_color %10
		else:
			l = ultimo_color
		return lista_colores[l]
        
    



"""
    leyenda = []
    for proceso in PROCESOS:
        gnt.broken_barh(proceso['tamanios'], proceso['altura'], color=proceso['color']) 
        leyenda.append(mpatches.Patch(color=proceso['color'], label=proceso['descripcion']))
        #plt.pause(1.5)

    plt.legend(handles=leyenda)


    plt.show()
    """