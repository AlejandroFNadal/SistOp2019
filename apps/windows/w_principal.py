from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_principal import Ui_MainWindow

from apps.windows.w_cargarProceso import W_cargarProceso

from apps.windows.w_configuracion1 import W_Configuracion1 

from crearDB import session, Proceso, Presets


class W_Main(QMainWindow):
	#---- inicio constructor ---#
	def __init__(self):
		QMainWindow.__init__(self)
		self.ventana = Ui_MainWindow()
		self.ventana.setupUi(self)


		self.dialogs = list()

		self.ventana.actionCrear_procesos.triggered.connect(self.crearProceso)
		self.ventana.actionConfiguracion_2.triggered.connect(self.menuConfiguracion1)
		self.ventana.actionSalir.triggered.connect(self.salir)
		self.ventana.actionAyuda.triggered.connect(self.ayuda)
		self.ventana.actionAcerca_de.triggered.connect(self.AcercaDe)
		self.ventana.btn_comenzar.clicked.connect(self.comenzar)
		
		self.ventana.pushButton.clicked.connect(self.actualizar)

		self.ventana.spinBox_quantum.setEnabled(False)
		
		

		procesos = session.query(Proceso).all()
		presets = session.query(Presets).all()

		
		
		#for p in presets: #recorre presets y lista descripcion
		self.mostrarDesc(presets)
		#self.ventana.comboBox_seleccionPreConf.addItem(str(p.descripcion))
		self.mostrarProc(procesos)
		
		

		self.ventana.comboBox_seleccionAlgoritmo.addItems(["FCFS", "RR", "MVQ"])
		self.ventana.comboBox_seleccionAlgoritmo.currentTextChanged.connect(self.habilitarQuantum)
		
		
		for p in procesos:#prueba: recorre procesos y lista los procesos, aca estoy probando q onda
			rowPosition = self.ventana.tableWidget.rowCount()
			self.ventana.tableWidget.insertRow(rowPosition)
			self.ventana.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(p.id_proc)))
			self.ventana.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(p.tiempo_arribo)))

	#----- fin constructor ----#


	def mostrarDesc(self, presets):
		for p in presets: #recorre presets y lista descripcion
			
			self.ventana.comboBox_seleccionPreConf.addItem(str(p.descripcion))
	
	def mostrarProc(self, procesos):
		lista_proc =[]
		for p in procesos:
    		 lista_proc.append(p.id_batch)
		lista_ord = dict.fromkeys(lista_proc).keys()
		for l in lista_ord:
    			self.ventana.comboBox_cargarProceso.addItem(str(l))

	def crearProceso(self):
		ventana = W_cargarProceso()
		self.dialogs.append(ventana)
		ventana.show()
	
	def menuConfiguracion1(self):
		ventanaConfig = W_Configuracion1()
		self.dialogs.append(ventanaConfig)
		ventanaConfig.show()
		
	def actualizar(self):
		presets = session.query(Presets).all()
		self.ventana.comboBox_seleccionPreConf.clear()
		for p in presets: #recorre presets y lista descripcion
			
			self.ventana.comboBox_seleccionPreConf.addItem(str(p.descripcion))
		procesos = session.query(Proceso).all()
		self.ventana.comboBox_cargarProceso.clear()
		self.mostrarProc(procesos)

	def habilitarQuantum(self, i):
		if i == "RR":
			self.ventana.spinBox_quantum.setEnabled(True)
	

	def salir(self):
		self.close()

	def ayuda(self):
		pass

	def AcercaDe(self):
		pass

	def comenzar(self):
		pass
