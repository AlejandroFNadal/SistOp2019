from PyQt5.QtWidgets import QMainWindow
from apps.ui.w_cargarProceso import Ui_cargarProceso
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crearDB import Presets, Base, Particiones, Proceso

engine = create_engine('sqlite:///SistOp.db')
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
<<<<<<< HEAD
		nombre=self.ventana.lineEdit_Nombre.text()
		#r = session.query(Proceso).order_by(Proceso.id_proc.desc()).first()
		#if r is not None:
    	#		cv += r[0]
		#else:
    	#		cv = 1
=======
		nombre=self.ventana.lineEdit_Nombre.text()	
>>>>>>> master
		
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
			new_proceso = Proceso(id_batch = str(nombre), tam_proc = int(tamano_proc), prioridad = int(prio), rafagaCPU = str(rafaga), tiempo_arribo = int(arribo))
			session.add(new_proceso)
			session.commit()
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
	'''
	def clave(self):
    	r = session.query(Proceso).order_by(Proceso.id_proc.desc()).first()
		if r is None:
    		cv += r[0]
	'''	
