from PyQt5.QtWidgets import QMainWindow
from apps.ui.w_gantt import Ui_image_gantt
from PyQt5 import QtGui, QtWidgets, QtCore



class W_image_gantt(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ventana = Ui_image_gantt()
		self.ventana.setupUi(self)
		self.dialogs = list()

		#-- aca genera la imagen en principal
		pixmap = QtGui.QPixmap('apps/windows/Gantt.png')
		self.ventana.label_gantt.setPixmap(pixmap)
		
		# -- 
