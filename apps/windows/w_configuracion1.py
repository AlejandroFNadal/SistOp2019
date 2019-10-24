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
		#self.ventana.tanbla.hide() ver ocultar tabla en configuracion.

	


	def config(self):
		#if self.radioButtonFija.isCheked(True):
		#ventana = W_ParticionFija()
		#self.dialogs.append(ventana)
		#ventana.show()

		nombreConf = self.ventana.lineEdit_Nombre.text()
		tamanoMemoria = int(self.ventana.spinBoxTamMemo.text())
		algoritmo = self.ventana.selectAlg.currentText()
		tamanoSO = int(self.ventana.spinBoxTamSo.text())
		if self.ventana.radioButtonFija.isChecked() == True:
			particion = "fija"
			ventana = W_ParticionFija(ventana=self.ventana)#le paso al constructor la ventana entera
			self.dialogs.append(ventana)
			ventana.show()
		elif self.radioButtonVariable.isChecked():
			particion = "variable"

		datos = [nombreConf, tamanoMemoria, algoritmo, tamanoSO, particion]
		print(datos)
	
