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
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 401, 561))
        self.frame_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(39, 80, 321, 421))
        self.frame_4.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 81, 20))
        self.label_3.setObjectName("label_3")
        self.tamMem_8 = QtWidgets.QLabel(self.frame_4)
        self.tamMem_8.setGeometry(QtCore.QRect(10, 90, 111, 41))
        self.tamMem_8.setObjectName("tamMem_8")
        self.tamSo_2 = QtWidgets.QLabel(self.frame_4)
        self.tamSo_2.setGeometry(QtCore.QRect(10, 150, 111, 41))
        self.tamSo_2.setObjectName("tamSo_2")
        self.tamMem_2 = QtWidgets.QLabel(self.frame_4)
        self.tamMem_2.setGeometry(QtCore.QRect(10, 50, 111, 41))
        self.tamMem_2.setObjectName("tamMem_2")
        self.tamMem_9 = QtWidgets.QLabel(self.frame_4)
        self.tamMem_9.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.tamMem_9.setObjectName("tamMem_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 370, 91, 28))
        self.pushButton_4.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 370, 91, 28))
        self.pushButton_5.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.btn_terminar = QtWidgets.QPushButton(self.frame_4)
        self.btn_terminar.setGeometry(QtCore.QRect(220, 370, 91, 28))
        self.btn_terminar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_terminar.setObjectName("btn_terminar")
        self.spinBoxTamMemo = QtWidgets.QSpinBox(self.frame_4)
        self.spinBoxTamMemo.setGeometry(QtCore.QRect(150, 60, 71, 41))
        self.spinBoxTamMemo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBoxTamMemo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxTamMemo.setObjectName("spinBoxTamMemo")
        self.spinBoxTamMemo_2 = QtWidgets.QSpinBox(self.frame_4)
        self.spinBoxTamMemo_2.setGeometry(QtCore.QRect(150, 110, 71, 41))
        self.spinBoxTamMemo_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBoxTamMemo_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxTamMemo_2.setObjectName("spinBoxTamMemo_2")
        self.spinBoxTamMemo_3 = QtWidgets.QSpinBox(self.frame_4)
        self.spinBoxTamMemo_3.setGeometry(QtCore.QRect(150, 160, 71, 41))
        self.spinBoxTamMemo_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBoxTamMemo_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxTamMemo_3.setObjectName("spinBoxTamMemo_3")
        self.spinBoxTamMemo_4 = QtWidgets.QSpinBox(self.frame_4)
        self.spinBoxTamMemo_4.setGeometry(QtCore.QRect(150, 210, 71, 41))
        self.spinBoxTamMemo_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBoxTamMemo_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxTamMemo_4.setObjectName("spinBoxTamMemo_4")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        cargarProceso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cargarProceso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 26))
        self.menubar.setObjectName("menubar")
        cargarProceso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cargarProceso)
        self.statusbar.setObjectName("statusbar")
        cargarProceso.setStatusBar(self.statusbar)

        self.retranslateUi(cargarProceso)
        QtCore.QMetaObject.connectSlotsByName(cargarProceso)

    def retranslateUi(self, cargarProceso):
        _translate = QtCore.QCoreApplication.translate
        cargarProceso.setWindowTitle(_translate("cargarProceso", "MainWindow"))
        self.label_3.setText(_translate("cargarProceso", "RCPU:"))
        self.tamMem_8.setText(_translate("cargarProceso", "Prioridad:"))
        self.tamSo_2.setText(_translate("cargarProceso", "Tamano:"))
        self.tamMem_2.setText(_translate("cargarProceso", "Arribo:"))
        self.tamMem_9.setText(_translate("cargarProceso", "NombreConf:"))
        self.pushButton_4.setText(_translate("cargarProceso", "Agregar"))
        self.pushButton_5.setText(_translate("cargarProceso", "Reiniciar"))
        self.btn_terminar.setText(_translate("cargarProceso", "Terminar"))
        self.label_7.setText(_translate("cargarProceso", "Proceso"))