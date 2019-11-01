from PyQt5.QtWidgets import QMainWindow
from apps.ui.w_cargarProceso import Ui_cargarProceso
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crearDB import Presets, Base, Particiones, Proceso

engine = create_engine('sqlite:///SistOp2.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class W_cargarProceso(QMainWindow):
	def __init__(self, parent=None):
		self.first_load=True
		super(W_cargarProceso, self).__init__(parent)
		#QMainWindow.__init__(self)
		self.ventana = Ui_cargarProceso()
		self.ventana.setupUi(self)
		self.ventana.label_2.setVisible(0)
		self.ventana.btn_AgregarProceso.clicked.connect(self.agregarProceso)
		self.ventana.btn_Reiniciar.clicked.connect(self.reiniciarProceso)
		self.ventana.btn_terminar.clicked.connect(self.terminar)

	def agregarProceso(self):
		#ventana = W_cargarProceso()
		#self.dialogs.append(ventana)
		#ventana.show()
		rafaga=self.ventana.lineEdit_rcpu.text()
		p=re.compile('(((E\d)|(C\d)|(S\d))-)*(C\d)') #expresion regular de las rafaga
		nombre=self.ventana.lineEdit_Nombre.text()	
		
		if self.first_load and p.fullmatch(rafaga) != None:
			self.first_load=False
			self.ventana.lineEdit_Nombre.setEnabled(False)
		arribo=self.ventana.spinBox_Arribo.value()
		tamano_proc=self.ventana.sBTamanoProceso.value()
		prio=self.ventana.sB_Prioridad.value()
		
		if p.fullmatch(rafaga) == None:
			self.ventana.lineEdit_rcpu.setStyleSheet("color : red")
			self.ventana.label_2.setVisible(1)
		else:
			self.ventana.label_2.setVisible(0)
			datos=[nombre,arribo,prio,tamano_proc,rafaga]
			new_proceso = Proceso(id_batch = nombre, tam_proc = tamano_proc, prioridad = prio, rafagaCPU = rafaga, tiempo_arribo = arribo)
			rafaga=self.ventana.lineEdit_rcpu.clear()
			arribo=self.ventana.spinBox_Arribo.setValue(0)
			tamano_proc=self.ventana.sBTamanoProceso.setValue(1)
			prio=self.ventana.sB_Prioridad.setValue(1)
			return datos
		

	def reiniciarProceso(self):
		rafaga=self.ventana.lineEdit_rcpu.clear()
		nombre=self.ventana.lineEdit_Nombre.clear()
		self.ventana.lineEdit_Nombre.setEnabled(True)
		arribo=self.ventana.spinBox_Arribo.setValue(0)
		tamano_proc=self.ventana.sBTamanoProceso.setValue(1)
		prioridad=self.ventana.sB_Prioridad.setValue(1)
	
	def terminar(self):
		self.close()
#	
	#def clave():
    	#cv = session.query(Proceso).order_by(Proceso.id.desc()).first()
		#if cv is not None 
#