from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from crearDB import Presets, Base, Particiones, Proceso
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apps.ui.w_particionFija import Ui_ParticionFija
from apps.ui.w_configuracion import Ui_Configuracion

engine = create_engine('sqlite:///SistOp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()



class W_ParticionFija(QMainWindow):
	def __init__(self, parent=None, ventana=None): #recibe la ventana entera
		super(W_ParticionFija, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_ParticionFija()
		self.ventana.setupUi(self)
		self.mem_SO = int((int(ventana.spinBoxTamMemo.text())*( int(ventana.spinBoxTamSo.text()))/100 ) )
		self.cant_mem_rest = int( int(ventana.spinBoxTamMemo.text()) - self.mem_SO	 )
		self.ventana.label_NombreConf.setText(ventana.lineEdit_Nombre.text()) #seteo los campos
		self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
		self.ventana.label_cantPart.setText(str(ventana.spinBox_cantParticion.text())) 	
		self.ventana.label_mensaje.setVisible(0)

		self.cant_part_rest = int(ventana.spinBox_cantParticion.text()) # se le resta 1 por que una particion es del SO
		self.lista_particiones = []
		#esto uso para poder reiniciar
		self.cant_part = self.cant_part_rest
		self.cant_mem = self.cant_mem_rest

		self.ventana.label_numPart.setText(str(1 + self.cant_part - self.cant_part_rest))

		self.ventana.btn_agregar.clicked.connect(self.agregarParticion)
		self.ventana.btn_terminar.clicked.connect(self.terminar)
		self.ventana.btn_reiniciar.clicked.connect(self.reiniciar)

	def get_lista_particiones(self):
		return self.lista_particiones

	def reset_lista_particiones(self):
		self.lista_particiones = []

	def anade_particion(self,part):
		self.lista_particiones.append(part)

# PERMITE GUARDAR SIN CREAR PARTICION, PARA LOS NUEVOS CAMBIOS DA ERROR
	def agregarParticion(self):
		tam_part = int(self.ventana.sB_tamParticion.text())
		if self.cant_part_rest > 1:
			#sumo cant part a tamanio de particion para que cada particion tenga como minimo 1 kb
			if (self.cant_mem_rest - (self.cant_part_rest + tam_part)) >= 0:
				self.cargar_lista(tam_part)
				self.cant_mem_rest = self.cant_mem_rest - tam_part
				self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
				self.cant_part_rest -= 1
				self.ventana.label_numPart.setText(str(1 + self.cant_part - self.cant_part_rest))
				 
				#aca lo que hace es ir tomando cada tam de particion y agregar a la fila
				#tratar de construir una funcion que haga esto y llamar para que quede mas limpio... helppp
				rowPosition = self.ventana.tW_ParticionFija.rowCount()
				self.ventana.tW_ParticionFija.insertRow(rowPosition)
				self.ventana.tW_ParticionFija.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(tam_part)))

				print("- Memoria restante: ", self.cant_mem_rest)
				print("- Particiones restantes: ", self.cant_part_rest)
				print("\n")
			else:
				self.ventana.label_mensaje.setText("Particion supera el max de memoria disponible")
				print("<<< El tamaño colocado para la particion supera el disponible en la memoria >>>")

			if self.cant_part_rest == 1:
				self.ultima_part()

		elif self.cant_part_rest == 1:
			self.ultima_part()
		else:
			self.ventana.label_mensaje.setText("Cantidad maxima de particiones colocadas")
			self.ventana.label_mensaje.setVisible(1)
			print("<<< Cantidad maxima de particiones colocadas >>> " )

	def reiniciar(self):
		self.cant_mem_rest = self.cant_mem
		self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
		self.cant_part_rest = self.cant_part
		self.ventana.label_numPart.setText(str(1 + self.cant_part - self.cant_part_rest))
		self.ventana.tW_ParticionFija.clearContents()
		for x in range(0,self.ventana.tW_ParticionFija.rowCount()+1):
			self.ventana.tW_ParticionFija.removeRow(x)
		self.ventana.tW_ParticionFija.removeRow(0)#No sabemos porque es necesario rehacer esto
		for x in range(0,self.ventana.tW_ParticionFija.rowCount()+1):
			self.ventana.tW_ParticionFija.removeRow(x)
		self.ventana.tW_ParticionFija.removeRow(0)#No sabemos porque es necesario rehacer esto

		#no se por que tengo q hacer 2 veces el for, de esa forma se limpia si o si
		self.reset_lista_particiones()

	def terminar(self):
		#Aca deberiamos tener en cuenta si el usuario no completo las particiones.
		#Podriamos hacer que si pulsa en terminar las particiones se creen automaticas
		#con igual tamaño todas (o casi todas, la ultima podria tener un poquito mas)
		if self.cant_part_rest>0:
			tam_part = self.cant_mem_rest//self.cant_part_rest
		#1
		while self.cant_part_rest > 1:
			if (tam_part*self.cant_part_rest) == self.cant_part_rest:
				self.cargar_lista(tam_part)
				self.cant_mem_rest = self.cant_mem_rest - tam_part
				self.cant_part_rest -= 1 
				print("- Memoria restante: ", self.cant_mem_rest)
				print("- Particiones restantes: ", self.cant_part_rest)
				print(" ")
			else:
				self.cargar_lista((tam_part+1))
				self.cant_mem_rest = self.cant_mem_rest - (tam_part+1)
				self.cant_part_rest -= 1 
				print("- Memoria restante: ", self.cant_mem_rest)
				print("- Particiones restantes: ", self.cant_part_rest)
				print(" ")


		#2
		if self.cant_part_rest == 1:
			self.ultima_part()

		self.pasar_datos()
		self.close()


	def pasar_datos(self):
		for i in self.get_lista_particiones():
			part = Particiones()
			part.batch = i[0]
			part.tam_part = i[1]
			part.dir_ini = i[2]
			part.dir_fin = i[3]
			session.add(part)
			print("batch - tamPart - dir_in - dir_fin")
			print(i)
		session.commit()
		self.reset_lista_particiones()

	def ultima_part(self):
		self.cargar_lista(self.cant_mem_rest) #mi tam_part seria la cant de mem restante
		rowPosition = self.ventana.tW_ParticionFija.rowCount()
		self.ventana.tW_ParticionFija.insertRow(rowPosition)
		self.ventana.tW_ParticionFija.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(self.cant_mem_rest)))
		self.cant_mem_rest = 0
		self.cant_part_rest -= 1
		self.ventana.label_MemoriaRes.setText(str(self.cant_mem_rest))
		self.ventana.label_numPart.setText(str(1 + self.cant_part - self.cant_part_rest))
		print("- Memoria restante: ", self.cant_mem_rest)
		print("- Particiones restantes: ", self.cant_part_rest)
		print("\n")
		self.ventana.label_mensaje.setText("Ultima particion autocompletada")
		self.ventana.label_mensaje.setVisible(1)
		print("<<< Cantidad maxima de particiones colocadas >>> " )

	def cargar_lista(self,tam_part):
		batch = self.ventana.label_NombreConf.text()
		dir_in = ((self.cant_mem - self.cant_mem_rest) + self.mem_SO)
		dir_fin = (dir_in + tam_part)
		datos_part = [batch,tam_part,dir_in,dir_fin]
		self.anade_particion(datos_part)
		