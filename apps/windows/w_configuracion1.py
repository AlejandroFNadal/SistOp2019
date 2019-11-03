from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_configuracion1 import Ui_configuracion1

from apps.windows.w_particionFija import W_ParticionFija
import re
from PyQt5 import QtCore

from crearDB import session, Presets
#from apps.windows.w_principal import W_Main

class W_Configuracion1(QMainWindow):
	def __init__(self, parent=None):
		super(W_Configuracion1, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_configuracion1()
		self.ventana.setupUi(self)
		self.dialogs = list()
		self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

		self.ventana.lineEdit_Nombre.setText(" ")#nombreConf
		self.ventana.spinBoxTamMemo.setValue(1)
		self.ventana.spinBoxTamSo.setValue(5)
		self.ventana.radioButtonFija.setAutoExclusive(True)
		self.ventana.radioButtonFija.setChecked(False)
		self.ventana.radioButtonVariable.setAutoExclusive(True)
		self.ventana.radioButtonVariable.setChecked(True)
		
		self.ventana.spinBox_cantParticion.setValue(2)
		self.ventana.spinBox_cantParticion.setMinimum(2)
		self.ventana.spinBox_cantParticion.setEnabled(False)

		self.ventana.btn_aceptar.clicked.connect(self.config)
		self.ventana.btn_reiniciar.clicked.connect(self.reiniciar)
		
		#detectar si se presiono un radiobutton
		self.ventana.radioButtonFija.toggled.connect(lambda:self.cambiarSpinbox(self.ventana))
		self.ventana.radioButtonVariable.toggled.connect(lambda:self.cambiarSpinbox(self.ventana))
			
		

	def cambiarSpinbox(self,vent):
		if vent.radioButtonFija.isChecked():
			vent.spinBox_cantParticion.setEnabled(True)
		if vent.radioButtonVariable.isChecked():
			vent.spinBox_cantParticion.setEnabled(False)
	
	def reiniciar(self):
		ventana = W_Configuracion1()
		ventana.show()

	

	def config(self):

		p=re.compile(' *')
		aux = self.ventana.lineEdit_Nombre.text()
		print(p.fullmatch(aux))
		
		
		if int(self.ventana.spinBox_cantParticion.value()) > 1 and p.fullmatch(aux)== None:
			nombreConf = self.ventana.lineEdit_Nombre.text()
			tamanoMemoria = int(self.ventana.spinBoxTamMemo.text())
			algoritmo = self.ventana.selectAlg.currentText()
			tamanoSO = int(self.ventana.spinBoxTamSo.text())
			if self.ventana.radioButtonFija.isChecked() == True:
				particion = "fija"
				ventana = W_ParticionFija(ventana=self.ventana)#le paso al constructor la ventana entera
				self.dialogs.append(ventana)
				ventana.show()
			else:
				particion = "variable"
				

			datos = [nombreConf, tamanoMemoria, algoritmo, tamanoSO, particion]
			self.grabarPresetBD(datos)
			self.close()
		else:
			if int(self.ventana.spinBox_cantParticion.value() <= 1):
				self.ventana.spinBox_cantParticion.setStyleSheet("color : red")
	
	def grabarPresetBD(self,datos):#agrega datos a la bd

		p = Presets()
		#p.id=6
		p.descripcion = datos[0]
		#p.tam_mem = 12
		session.add(p)
		session.commit()
		
		"""presets = session.query(Presets).all()
		self.mostrarDesc(presets)"""

		print(p.descripcion)
		#aca falta hacer que grabe en la BD
	def reiniciar(self):
		self.ventana.lineEdit_Nombre.setText(" ")
		self.ventana.spinBoxTamMemo.setValue(1)
		self.ventana.spinBoxTamSo.setValue(5)
		self.ventana.radioButtonFija.setAutoExclusive(False)
		self.ventana.radioButtonFija.setChecked(False)
		self.ventana.radioButtonVariable.setAutoExclusive(False)
		self.ventana.radioButtonVariable.setChecked(False)
		self.ventana.spinBox_cantParticion.setValue(1)

