# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargarProceso.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cargarProceso(object):
    def setupUi(self, cargarProceso):
        cargarProceso.setObjectName("cargarProceso")
        cargarProceso.resize(452, 629)
        self.centralwidget = QtWidgets.QWidget(cargarProceso)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_AgregarProceso = QtWidgets.QPushButton(self.centralwidget)
        self.btn_AgregarProceso.setGeometry(QtCore.QRect(60, 470, 91, 28))
        self.btn_AgregarProceso.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_AgregarProceso.setObjectName("btn_AgregarProceso")
        self.sB_Arribo = QtWidgets.QLabel(self.centralwidget)
        self.sB_Arribo.setGeometry(QtCore.QRect(60, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sB_Arribo.setFont(font)
        self.sB_Arribo.setObjectName("sB_Arribo")
        self.spinBox_Arribo = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Arribo.setGeometry(QtCore.QRect(200, 160, 71, 41))
        self.spinBox_Arribo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_Arribo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_Arribo.setObjectName("spinBox_Arribo")
        self.btn_terminar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_terminar.setGeometry(QtCore.QRect(270, 470, 91, 28))
        self.btn_terminar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_terminar.setObjectName("btn_terminar")
        self.btn_Reiniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Reiniciar.setGeometry(QtCore.QRect(160, 470, 91, 28))
        self.btn_Reiniciar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_Reiniciar.setObjectName("btn_Reiniciar")
        self.sBTamanoProceso = QtWidgets.QSpinBox(self.centralwidget)
        self.sBTamanoProceso.setGeometry(QtCore.QRect(200, 300, 71, 41))
        self.sBTamanoProceso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sBTamanoProceso.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sBTamanoProceso.setMinimum(1)
        self.sBTamanoProceso.setObjectName("sBTamanoProceso")
        self.sB_Prioridad = QtWidgets.QSpinBox(self.centralwidget)
        self.sB_Prioridad.setGeometry(QtCore.QRect(200, 230, 71, 41))
        self.sB_Prioridad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sB_Prioridad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sB_Prioridad.setMinimum(1)
        self.sB_Prioridad.setMaximum(3)
        self.sB_Prioridad.setObjectName("sB_Prioridad")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tamMem_8 = QtWidgets.QLabel(self.centralwidget)
        self.tamMem_8.setGeometry(QtCore.QRect(60, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tamMem_8.setFont(font)
        self.tamMem_8.setObjectName("tamMem_8")
        self.lineEdit_rcpu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rcpu.setGeometry(QtCore.QRect(200, 360, 211, 41))
        self.lineEdit_rcpu.setObjectName("lineEdit_rcpu")
        self.tamSo_2 = QtWidgets.QLabel(self.centralwidget)
        self.tamSo_2.setGeometry(QtCore.QRect(60, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tamSo_2.setFont(font)
        self.tamSo_2.setObjectName("tamSo_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 360, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tamMem_2 = QtWidgets.QLabel(self.centralwidget)
        self.tamMem_2.setGeometry(QtCore.QRect(60, 100, 61, 41))
        self.tamMem_2.setObjectName("tamMem_2")
        self.lineEdit_Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Nombre.setGeometry(QtCore.QRect(140, 110, 171, 22))
        self.lineEdit_Nombre.setObjectName("lineEdit_Nombre")
        cargarProceso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cargarProceso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 26))
        self.menubar.setObjectName("menubar")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        cargarProceso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cargarProceso)
        self.statusbar.setObjectName("statusbar")
        cargarProceso.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(cargarProceso)
        QtCore.QMetaObject.connectSlotsByName(cargarProceso)

    def retranslateUi(self, cargarProceso):
        _translate = QtCore.QCoreApplication.translate
        cargarProceso.setWindowTitle(_translate("cargarProceso", "Cargar Proceso"))
        self.btn_AgregarProceso.setText(_translate("cargarProceso", "Agregar"))
        self.sB_Arribo.setText(_translate("cargarProceso", "Arribo:"))
        self.btn_terminar.setText(_translate("cargarProceso", "Terminar"))
        self.btn_Reiniciar.setText(_translate("cargarProceso", "Reiniciar"))
        self.label_7.setText(_translate("cargarProceso", "Proceso"))
        self.tamMem_8.setText(_translate("cargarProceso", "Prioridad:"))
        self.tamSo_2.setText(_translate("cargarProceso", "Tamaño:"))
        self.label_4.setText(_translate("cargarProceso", "RCPU:"))
        self.tamMem_2.setText(_translate("cargarProceso", "Nombre:"))
        self.menuAyuda.setTitle(_translate("cargarProceso", "Ayuda"))
