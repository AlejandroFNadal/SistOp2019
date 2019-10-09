from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_cargarProceso import Ui_cargarProceso

class W_cargarProceso(QMainWindow):
	def __init__(self, parent=None):
		super(W_cargarProceso, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_cargarProceso()
		self.ventana.setupUi(self)

		self.ventana.btn_AgregarProceso.clicked.connect(self.agregarProceso)


	def agregarProceso(self):
		#ventana = W_cargarProceso()
		#self.dialogs.append(ventana)
		#ventana.show()
		print("hola mudo")
		print(self.ventana.spinBox_Arribo.value())