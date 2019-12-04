from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtGui, QtWidgets, QtCore
from apps.ui.w_cargarProceso import Ui_cargarProceso
import re
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker
from crearDB import Presets, Base, Particiones, Proceso

engine = create_engine('sqlite:///SistOp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class W_cargarProceso(QMainWindow):
	def __init__(self, parent=None):
		self.first_load=True
		super(W_cargarProceso, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_cargarProceso()
		self.ventana.setupUi(self)
		#self.ventana.label_2.setVisible(0)
		self.ventana.label_error_tam.setVisible(0)
		self.ventana.btn_AgregarProceso.clicked.connect(self.agregarProceso)
		self.ventana.btn_Reiniciar.clicked.connect(self.reiniciarProceso)
		self.ventana.btn_terminar.clicked.connect(self.terminar)
		self.ventana.btn_add.clicked.connect(self.add_row)
		self.ventana.btn_rm.clicked.connect(self.delete)
		
		presets = session.query(Presets).all()
		self.mostrarDesc(presets)

		self.ventana.comboBox_seleccionPreConf.currentTextChanged.connect(self.listarTam)
		self.listarTam()
		

	#--fin constructor--

		
	def mostrarDesc(self, presets):
		for p in presets: #recorre presets y lista descripcion
			
			self.ventana.comboBox_seleccionPreConf.addItem(str(p.descripcion))
		#self.listarTam()

	def listarTam(self): # Lista configuracion de memoria y tamaño maximo de la particion fija y variable
		descripcionMemoria = self.ventana.comboBox_seleccionPreConf.currentText()#preset
		mem = session.query(Presets).filter(Presets.descripcion == descripcionMemoria).one()
		if mem.fija_variable == "fija":
			tamano = session.query(Particiones).filter(Particiones.batch == descripcionMemoria).order_by(desc(Particiones.tam_part)).first()
			self.ventana.label_tamMax.setText(str(tamano.tam_part))
		else:
			 self.ventana.label_tamMax.setText(str(mem.tamMemoria - mem.sistOpMem))
		
		self.ventana.label_particion.setText(str(mem.fija_variable))
		

	def agregarProceso(self):
						
						#rafaga=self.ventana.lineEdit_rcpu.text()
						#p=re.compile('(((E\d)|(C\d)|(S\d))-)*(C\d)') #expresion regular de las rafaga
						#crea una lista vacia luego recorre la tabla y va creando una tupla
						rafaga = ""
						#recorro la tabla de rafagas y voy armando el string
						for row in range(self.ventana.tW_procesos.rowCount()):
							if self.ventana.tW_procesos.cellWidget(row, 0).currentText() == "CPU":
								accion = "C"
							else:
								accion = "E"

							raf = self.ventana.tW_procesos.cellWidget(row, 1).value()
							if rafaga == "":
								rafaga = accion  + str(raf)
							else:
								rafaga = rafaga + "-" + accion  + str(raf)
						print( rafaga )
						
						nombre=self.ventana.lineEdit_Nombre.text()	
						
						if self.first_load and rafaga != None:
							self.first_load=False
							self.ventana.lineEdit_Nombre.setEnabled(False)
						arribo=self.ventana.spinBox_Arribo.value()
						tamano_proc=self.ventana.sBTamanoProceso.value()
						prio=self.ventana.sB_Prioridad.value()
						descripcionMemoria = self.ventana.comboBox_seleccionPreConf.currentText()#preset
						mem = session.query(Presets).filter(Presets.descripcion == descripcionMemoria).first()
						if mem.fija_variable == "fija":
							consult = session.query(Particiones).filter(Particiones.batch == descripcionMemoria).order_by(desc(Particiones.tam_part)).first()
							tamano_m = consult.tam_part
						else:
							 tamano_m = (mem.tamMemoria - mem.sistOpMem)
				
						
				
						if rafaga == None:
							print("carga exitosa")
						elif tamano_proc <= tamano_m:
							#self.ventana.label_2.setVisible(0)
							self.ventana.label_error_tam.setVisible(0)
							datos=[nombre,tamano_proc,prio,rafaga,arribo, descripcionMemoria]
							
							self.cargarProcBD(datos)
							
							#rafaga=self.ventana.lineEdit_rcpu.clear()
							arribo=self.ventana.spinBox_Arribo.setValue(0)
							tamano_proc=self.ventana.sBTamanoProceso.setValue(1)
							prio=self.ventana.sB_Prioridad.setValue(1)
						else:
							 #print("Error tamaño")
							 self.ventana.label_error_tam.setVisible(1)
					
	def add_row(self):# agrega una fila a la tabla
		rowPosition = self.ventana.tW_procesos.rowCount()
		if rowPosition >= 11:
			QMessageBox.about(self, "Alerta", "El maximo de filas es de 11")#agrga un alert
			return 0
		if rowPosition == 0:
			self.insert_row(tipo = "CPU", rowPosition = rowPosition)
		elif rowPosition > 0:
			self.insert_row(tipo = "E/S", rowPosition = rowPosition)
			self.insert_row(tipo = "CPU", rowPosition = rowPosition + 1)

		
	
	def insert_row(self, tipo, rowPosition):

		#cuenta las filas
		 
		#inserta en la ultima fila
		self.ventana.tW_procesos.insertRow(rowPosition)
		#crea una variable del tipo combobox
		#agrega el combo box en la posicion de la fila
		x = QtWidgets.QComboBox()
		y = QtWidgets.QSpinBox()


		x.addItem(tipo)
		
		if tipo == "E/S":
			y.setMinimum(0)
		else:
			y.setMinimum(1)
		y.setMaximum(99)

		self.ventana.tW_procesos.setCellWidget(rowPosition, 0, x)	
		self.ventana.tW_procesos.setCellWidget(rowPosition, 1, y)
		self.ventana.tW_procesos.resizeColumnsToContents()




	# Funcion para Boton
	def delete(self):
		

		items_selected = [item.row() for item in self.ventana.tW_procesos.selectedIndexes()]

		for i in reversed(range(self.ventana.tW_procesos.rowCount())):
			if i in items_selected:
				self.ventana.tW_procesos.removeRow(i)

	def reiniciarProceso(self):
		rafaga=self.ventana.lineEdit_rcpu.clear()
		nombre=self.ventana.lineEdit_Nombre.clear()
		self.ventana.lineEdit_Nombre.setEnabled(True)
		arribo=self.ventana.spinBox_Arribo.setValue(0)
		tamano_proc=self.ventana.sBTamanoProceso.setValue(1)
		prioridad=self.ventana.sB_Prioridad.setValue(1)



	
	def terminar(self):
		self.close()
	
	#Metodo para cargar en base de datos
	def cargarProcBD(self, datos):
		p = Proceso()
		p.id_batch = datos[0]
		p.tam_proc = datos[1]
		p.prioridad = datos[2]
		p.rafagaCPU = datos[3]
		p.tiempo_arribo = datos[4]
		p.desc_memoria = datos[5]
		session.add(p)
		session.commit()
	
	
