from PyQt5.QtWidgets import QMainWindow
from apps.ui.w_estadistica1 import Ui_Estadistica1
from PyQt5 import QtGui, QtWidgets, QtCore



class W_Estadistica1(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ventana = Ui_Estadistica1()
		self.ventana.setupUi(self)
		self.dialogs = list()

		#-- aca genera la imagen en principal
		#pixmap = QtGui.QPixmap('apps/windows/Gantt.png')
		#self.ventana.label_estadistica1.setPixmap(pixmap)
		
		# -- 