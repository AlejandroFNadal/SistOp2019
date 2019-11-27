from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from apps.ui.w_instruccionesDeUso import Ui_instruccionesDeUso

class W_instruccionesDeUso(QMainWindow):
	#---- inicio constructor ---#
	def __init__(self):
		QMainWindow.__init__(self)
		self.ventana = Ui_instruccionesDeUso()
		self.ventana.setupUi(self)
		
		self.dialogs = list()