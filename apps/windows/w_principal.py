from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_principal import Ui_MainWindow

from apps.windows.w_cargarProceso import W_cargarProceso

from apps.windows.w_configuracion1 import W_Configuracion1 

#importar sqlite

class W_Main(QMainWindow):
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


	def crearProceso(self):
		ventana = W_cargarProceso()
		self.dialogs.append(ventana)
		ventana.show()
	
	def menuConfiguracion1(self):
		ventana = W_Configuracion1()
		self.dialogs.append(ventana)
		ventana.show()

	def salir(self):
		self.close()

	def ayuda(self):
		pass

	def AcercaDe(self):
		pass

	def comenzar(self):
		pass
