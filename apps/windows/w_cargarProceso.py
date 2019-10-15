from PyQt5.QtWidgets import QMainWindow
from apps.ui.w_cargarProceso import Ui_cargarProceso
import re
class W_cargarProceso(QMainWindow):
	def __init__(self, parent=None):
		self.first_load=True
		super(W_cargarProceso, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_cargarProceso()
		self.ventana.setupUi(self)
		self.ventana.label_2.setVisible(0)
		self.ventana.btn_AgregarProceso.clicked.connect(self.agregarProceso)


	def agregarProceso(self):
		#ventana = W_cargarProceso()
		#self.dialogs.append(ventana)
		#ventana.show()
		rafaga=self.ventana.lineEdit_rcpu.text()
		p=re.compile('(((E\d)|(C\d)|(S\d))-)*(C\d)') #expresion regular de las rafaga
		if self.first_load and p.fullmatch(rafaga) != None:
			nombre=self.ventana.lineEdit_Nombre.text()
			self.first_load=False
			self.ventana.lineEdit_Nombre.setEnabled(False)
		arribo=self.ventana.spinBox_Arribo.value()
		tamano_proc=self.ventana.sBTamanoProceso.value()
		prioridad=self.ventana.sB_Prioridad.value()
		if p.fullmatch(rafaga) == None:
			self.ventana.lineEdit_rcpu.setStyleSheet("color : red")
			self.ventana.label_2.setVisible(1)
		else:
			self.ventana.label_2.setVisible(0)
			datos=[nombre,arribo,prioridad,tamano_proc,rafaga]
			return datos