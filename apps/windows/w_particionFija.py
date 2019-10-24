from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_particionFija import Ui_ParticionFija
from apps.ui.w_configuracion import Ui_Configuracion

class W_ParticionFija(QMainWindow):
	def __init__(self, parent=None, ventana=None): #recibe la ventana entera
		super(W_ParticionFija, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_ParticionFija()
		self.ventana.setupUi(self)

		self.ventana.label_NombreConf.setText(ventana.lineEdit_Nombre.text()) #seteo los campos
		self.ventana.label_MemoriaRes.setText(ventana.spinBoxTamMemo.text())
		"""self.ventana.btn_aceptar.clicked.connect(self.agregarParticion)

	def agregarParticion(self):
		cant_mem = int(self.ventana.spinBoxTamMemo.text())
		cant_part = int(self.ventana.spinBox_cantParticion.text())
		tam_part = int(self.sB_tamParticion.text())

		if cant_part>0 and (cant_mem - (cant_part + tam_part)): #sumo cant part a tamanio de particion para que cada particion tenga como minimo 1 kb
			pass
"""