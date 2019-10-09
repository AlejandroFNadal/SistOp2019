from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_principal import Ui_MainWindow

from apps.windows.w_cargarProceso import W_cargarProceso

from apps.windows.w_configuracion1 import W_Configuracion1 

class W_Main(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ventana = Ui_MainWindow()
		self.ventana.setupUi(self)


		self.dialogs = list()

		self.ventana.actionCrear_procesos.triggered.connect(self.asd)
		self.ventana.actionConfiguracion_2.triggered.connect(self.menuConfiguracion1)

	def asd(self):
		ventana = W_cargarProceso()
		self.dialogs.append(ventana)
		ventana.show()
	
	def menuConfiguracion1(self):
		ventana = W_Configuracion1()
		self.dialogs.append(ventana)
		ventana.show()
