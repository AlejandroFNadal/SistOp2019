from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_particionFija import Ui_ParticionFija
from apps.ui.w_configuracion import Ui_Configuracion

class W_ParticionFija(QMainWindow):
	def __init__(self, parent=None, ventana=None): #recibe la ventana entera
		super(W_ParticionFija, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_ParticionFija()
		self.ventana.setupUi(self)

		self.cant_mem_rest = int( int(ventana.spinBoxTamMemo.text()) - (int(ventana.spinBoxTamMemo.text())*( int(ventana.spinBoxTamSo.text()))/100 ) )
		self.ventana.label_NombreConf.setText(ventana.lineEdit_Nombre.text()) #seteo los campos
		self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
		#self.ventana.label_CantParticion.setText(ventana.spinBox_cantParticion.text()) #no esta implementado todavia
		#self.ventana.label_NumParticion.setText("1") 									#no esta implementado todavia
		self.cant_part_rest = int(ventana.spinBox_cantParticion.text())-1 # se le resta 1 por que una particion es del SO
		
		#esto uso para poder reiniciar
		self.cant_part = self.cant_part_rest
		self.cant_mem = self.cant_mem_rest

		self.ventana.btn_agregar.clicked.connect(self.agregarParticion)
		self.ventana.btn_terminar.clicked.connect(self.terminar)
		self.ventana.btn_reiniciar.clicked.connect(self.reiniciar)

	def agregarParticion(self):
		tam_part = int(self.ventana.sB_tamParticion.text())
		#hay que testear mas fino lo de abajo
		if self.cant_part_rest > 1:
			#sumo cant part a tamanio de particion para que cada particion tenga como minimo 1 kb
			if (self.cant_mem_rest - (self.cant_part_rest + tam_part)) >= 0:
				self.cant_mem_rest = self.cant_mem_rest - tam_part
				self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
				self.cant_part_rest -= 1
				print("- Particion creada de ",tam_part," Kb") 
				print("- Memoria restante: ", self.cant_mem_rest)
				print("- Particiones restantes: ", self.cant_part_rest)
				print("\n")
			else:
				print("<<< El tamaño colocado para la particion supera el disponible en la memoria >>>")

			#para colocar en la ultima particion toda la memoria restante
			if self.cant_part_rest == 1:
				print("- Particion creada de ",self.cant_mem_rest," Kb")
				self.cant_mem_rest = 0
				self.cant_part_rest -= 1 
				print("- Memoria restante: ", self.cant_mem_rest)
				print("- Particiones restantes: ", self.cant_part_rest)
				print("\n")
		else:
			print("<<< Cantidad maxima de particiones colocadas >>> " )
			self.close()

	def reiniciar(self):
		self.cant_mem_rest = self.cant_mem
		self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
		self.cant_part_rest = self.cant_part

	def terminar(self):
		#Aca deberiamos tener en cuenta si el usuario no completo las particiones.
		#Podriamos hacer que si pulsa en terminar las particiones se creen automaticas
		#con igual tamaño todas (o casi todas, la ultima podria tener un poquito mas)
		
		tam_part = self.cant_mem_rest//self.cant_part_rest
		#1
		while self.cant_part_rest > 1:
			print("- Particion creada de ",tam_part," Kb")
			self.cant_mem_rest = self.cant_mem_rest - tam_part
			self.cant_part_rest -= 1 
			print("- Memoria restante: ", self.cant_mem_rest)
			print("- Particiones restantes: ", self.cant_part_rest)
			print(" ")

		#2
		if self.cant_part_rest == 1:
			print("- Particion creada de ",self.cant_mem_rest," Kb")
			self.cant_mem_rest = 0
			self.cant_part_rest -= 1 
			print("- Memoria restante: ", self.cant_mem_rest)
			print("- Particiones restantes: ", self.cant_part_rest)
		
		"""
		otra forma podria ser creando la primera particion mas grande que las otras de la siguiente forma

		tam_part_1 = self.cant_mem_rest - tam_part*self.cant_part_rest 
		print("- Particion creada de ",tam_part_1," Kb")
		self.cant_mem_rest = self.cant_mem_rest - tam_part_1
		self.cant_part_rest -= 1 
		print("- Memoria restante: ", self.cant_mem_rest)
		print("- Particiones restantes: ", self.cant_part_rest)
		
		Esta segunda forma iria abajo de #1 y el mientras seria mientras fuese mayor a 0
		y lo que esta abajo de #2 no iria.
		No esta testeado.
		"""
		self.close()