from PyQt5.QtWidgets import QMainWindow
from apps.ui.w_estadistica2 import Ui_Estadistica2
from PyQt5 import QtGui, QtWidgets, QtCore



class W_Estadistica2(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ventana = Ui_Estadistica2()
		self.ventana.setupUi(self)
		self.dialogs = list()

		#-- aca genera la imagen en principal
		#pixmap = QtGui.QPixmap('apps/windows/Gantt.png')
		#self.ventana.label_gantt.setPixmap(pixmap)
		
		# -- 