from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_configuracion import Ui_Configuracion



class W_Configuracion(QMainWindow):
	def __init__(self, parent=None):
		super(W_Configuracion, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_Configuracion()
		self.ventana.setupUi(self)