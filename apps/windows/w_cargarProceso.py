from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_cargarProceso import Ui_cargarProceso

class W_cargarProceso(QMainWindow):
	def __init__(self, parent=None):
		self.first_load=True
		super(W_cargarProceso, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_cargarProceso()
		self.ventana.setupUi(self)

		self.ventana.btn_AgregarProceso.clicked.connect(self.agregarProceso)


	def agregarProceso(self):
		#ventana = W_cargarProceso()
		#self.dialogs.append(ventana)
		#ventana.show()
		if self.first_load:
			nombre=self.ventana.lineEdit_Nombre.text()
			self.first_load=False
			self.ventana.lineEdit_Nombre.setEnabled(False)
		arribo=self.ventana.spinBox_Arribo.value()
		tamano_proc=self.ventana.sBTamanoProceso.value()
		prioridad=self.ventana.sB_Prioridad.value()
		rafaga=self.ventana.lineEdit_rcpu.text()
		datos=[nombre,arribo,prioridad,tamano_proc,rafaga]
		print(datos)