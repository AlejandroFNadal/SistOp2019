from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow



from apps.ui.w_principal import Ui_MainWindow

from apps.windows.w_cargarProceso import W_cargarProceso

from apps.windows.w_configuracion1 import W_Configuracion1 

from apps.windows.w_gantt import W_image_gantt

from Clases.Procesador import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crearDB import session, Proceso, Presets, Particiones, Base


engine = create_engine('sqlite:///SistOp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


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
		self.ventana.btn_gantt.clicked.connect(self.mostrarGantt)

		self.ventana.spinBox_quantum.setEnabled(False)
		
		
		presets = session.query(Presets).all()
				
		#for p in presets: #recorre presets y lista descripcion
		self.mostrarDesc(presets)
		#self.ventana.comboBox_seleccionPreConf.addItem(str(p.descripcion))
		self.mostrarProc()
		
		

		self.ventana.comboBox_seleccionAlgoritmo.addItems(["FCFS", "RR", "Prioridades", "MLQ", "SJF", "SRTF"])
		self.ventana.comboBox_seleccionAlgoritmo.currentTextChanged.connect(self.habilitarQuantum)

		self.ventana.comboBox_cargarProceso.currentTextChanged.connect(self.listar)
		self.ventana.comboBox_seleccionPreConf.currentTextChanged.connect(self.listarConf)

		
		self.habilitarQuantum()
		self.listar()
		self.listarConf()
		#setCurrentIndex
	#----- fin constructor ----#


	def mostrarDesc(self, presets):
		for p in presets: #recorre presets y lista descripcion
			
			self.ventana.comboBox_seleccionPreConf.addItem(str(p.descripcion))

		self.listarConf()
	
	def mostrarProc(self):
		desc = self.ventana.comboBox_seleccionPreConf.currentText()

		procesos = session.query(Proceso).filter(Proceso.desc_memoria == desc).distinct(Proceso.id_batch).all()
		lista_proc=[]
		for p in procesos:
			if p.id_batch not in lista_proc:
				lista_proc.append(p.id_batch)
				self.ventana.comboBox_cargarProceso.addItem(p.id_batch)
		
		self.listar()

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
		self.ventana.comboBox_cargarProceso.clear()
		procesos = session.query(Proceso).all()
		
		self.mostrarProc()

	def habilitarQuantum(self):
		i=self.ventana.comboBox_seleccionAlgoritmo.currentText()
		if i == "RR":
			self.ventana.spinBox_quantum.setEnabled(True)
		else:
			self.ventana.spinBox_quantum.setEnabled(False)	
	
	def mostrarGantt(self):
		ventanaConfig = W_image_gantt()
		self.dialogs.append(ventanaConfig)
		ventanaConfig.show()

	def salir(self):
		self.close()

	def ayuda(self):
		pass

	def AcercaDe(self):
		pass


	def comenzar(self):
		algoritmoP = self.ventana.comboBox_seleccionAlgoritmo.currentText()
		if algoritmoP == "FCFS":
			algoritmoP=0
			quantum = 0
		elif algoritmoP =="RR":
			algoritmoP=1
			quantum = self.ventana.spinBox_quantum.value()
		elif algoritmoP == "Prioridades":
			algoritmoP = 2
			quantum = self.ventana.spinBox_quantum.value()
		elif algoritmoP == "MLQ":
			algoritmoP = 3
			quantum = self.ventana.spinBox_quantum.value()
		elif algoritmoP == "SJF":
			algoritmoP = 4
			quantum = self.ventana.spinBox_quantum.value()
		elif algoritmoP == "SRTF":
			algoritmoP = 5
			quantum = self.ventana.spinBox_quantum.value()
		
		
		# Realizar una busqueda en la BD para traer el preset que conincida con el ingresado
		desc_config = self.ventana.comboBox_seleccionPreConf.currentText()
		
		preset = session.query(Presets).filter(Presets.descripcion == desc_config).all()

		# Realizar busqueda en la BD para traer y armar una lista con todos los procesos correspondientes al batch
		desc_procesos = self.ventana.comboBox_cargarProceso.currentText()
		procesos = session.query(Proceso).filter(Proceso.id_batch == desc_procesos).all()
		
		# Realizar busqueda en BD para traer el bach de las particiones
		particiones = session.query(Particiones).filter(Particiones.batch == desc_config).all()
		
		# Pasamos al procesador
		core = Procesador()
		
		print("Algoritmo: " +str(algoritmoP), "Quantum: " +str(quantum), "Procesos: ")
		for i in particiones:
			 print("id particion " +str(i.id_part))
		core.Simular(preset[0], procesos,particiones, algoritmoP, quantum)
		'''
		print("Algoritmo: " +str(algoritmoP), "Quantum: " +str(quantum), "Procesos: ")
		for i in particiones:
			 print("id particion " +str(i.id_part))
		print("Fin")
		#print(algoritmoP)
		'''

	def listar(self):
		i = self.ventana.comboBox_cargarProceso.currentText()
		#self.ventana.tableWidget.clear()
		self.ventana.tableWidget.clearContents()
		for x in range(0,self.ventana.tableWidget.rowCount()+1):
			self.ventana.tableWidget.removeRow(x)
		self.ventana.tableWidget.removeRow(0)#No sabemos porque es necesario rehacer esto
		q = session.query(Proceso).filter(Proceso.id_batch == i).all()
		for l in q:
			rowPosition = self.ventana.tableWidget.rowCount()
			self.ventana.tableWidget.insertRow(rowPosition)
			self.ventana.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(l.id_proc)))
			self.ventana.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(l.tiempo_arribo)))
			self.ventana.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(l.prioridad)))
			self.ventana.tableWidget.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(l.tam_proc)))
			self.ventana.tableWidget.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(l.rafagaCPU)))

	def listarConf(self):
		self.mostrarProc()
		print("cambio combo")
		f = self.ventana.comboBox_seleccionPreConf.currentText()

		a = session.query(Presets).filter(Presets.descripcion == f).all()
		
		for x in range(0,self.ventana.tableWidget_2.columnCount()+1):
			self.ventana.tableWidget_2.removeColumn(x)
		columnPosition = self.ventana.tableWidget_2.columnCount()
		self.ventana.tableWidget_2.insertColumn(columnPosition)
		for p in a:
			if p.algoritmo_as==1:
				texto="BF"
			if p.algoritmo_as==2:
				texto="FF"
			if p.algoritmo_as==3:
				texto="WF"
			self.ventana.tableWidget_2.setItem(columnPosition , 0, QtWidgets.QTableWidgetItem(texto))
			self.ventana.tableWidget_2.setItem(columnPosition , 1, QtWidgets.QTableWidgetItem(str(p.fija_variable)))
			self.ventana.tableWidget_2.setItem(columnPosition , 2, QtWidgets.QTableWidgetItem(str(p.sistOpMem)))
			self.ventana.tableWidget_2.setItem(columnPosition , 3, QtWidgets.QTableWidgetItem(str(p.cant_part)))