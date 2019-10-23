from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_configuracion1 import Ui_configuracion1

from apps.windows.w_particionFija import W_ParticionFija



class W_Configuracion1(QMainWindow):
	def __init__(self, parent=None):
		super(W_Configuracion1, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_configuracion1()
		self.ventana.setupUi(self)
		self.dialogs = list()
		self.ventana.btn_aceptar.clicked.connect(self.config)


	def config(self):
		#if self.radioButtonFija.isCheked(True):
		ventana = W_ParticionFija()
		self.dialogs.append(ventana)
		ventana.show()
	
