# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 817)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_seleccionPreConf = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_seleccionPreConf.setGeometry(QtCore.QRect(210, 110, 291, 22))
        self.comboBox_seleccionPreConf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_seleccionPreConf.setObjectName("comboBox_seleccionPreConf")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 171, 20))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 210, 631, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 30, 621, 281))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 161, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox_seleccionAlgoritmo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_seleccionAlgoritmo.setGeometry(QtCore.QRect(210, 150, 291, 22))
        self.comboBox_seleccionAlgoritmo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_seleccionAlgoritmo.setObjectName("comboBox_seleccionAlgoritmo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 30, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 270, 191, 151))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        self.btn_comenzar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_comenzar.setGeometry(QtCore.QRect(490, 610, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_comenzar.setFont(font)
        self.btn_comenzar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_comenzar.setObjectName("btn_comenzar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.spinBox_quantum = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_quantum.setGeometry(QtCore.QRect(620, 150, 71, 41))
        self.spinBox_quantum.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_quantum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_quantum.setMinimum(1)
        self.spinBox_quantum.setMaximum(10)
        self.spinBox_quantum.setObjectName("spinBox_quantum")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 150, 61, 20))
        self.label_5.setObjectName("label_5")
        self.comboBox_cargarProceso = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_cargarProceso.setGeometry(QtCore.QRect(710, 110, 261, 22))
        self.comboBox_cargarProceso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_cargarProceso.setObjectName("comboBox_cargarProceso")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 110, 171, 20))
        self.label_6.setObjectName("label_6")
        self.btn_retroceder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_retroceder.setGeometry(QtCore.QRect(270, 610, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_retroceder.setFont(font)
        self.btn_retroceder.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_retroceder.setObjectName("btn_retroceder")
        self.btn_avanzar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_avanzar.setGeometry(QtCore.QRect(700, 610, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_avanzar.setFont(font)
        self.btn_avanzar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_avanzar.setObjectName("btn_avanzar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1000, 19, 20, 681))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionsdfsdfafda = QtWidgets.QAction(MainWindow)
        self.actionsdfsdfafda.setObjectName("actionsdfsdfafda")
        self.actionConfiguracion_2 = QtWidgets.QAction(MainWindow)
        self.actionConfiguracion_2.setObjectName("actionConfiguracion_2")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionCrear_procesos = QtWidgets.QAction(MainWindow)
        self.actionCrear_procesos.setObjectName("actionCrear_procesos")
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbrir)
        self.menuMenu.addAction(self.actionGuardar)
        self.menuMenu.addAction(self.actionCrear_procesos)
        self.menuMenu.addAction(self.actionConfiguracion_2)
        self.menuMenu.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Planificador de Procesos"))
        self.label.setText(_translate("MainWindow", "Seleccione preconfiguracion"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arribo"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prioridad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tamano"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "RCPU"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Procesos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Simulacion"))
        self.label_2.setText(_translate("MainWindow", "Seleccione algoritmo"))
        self.label_3.setText(_translate("MainWindow", "Planificador de Procesos"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Algoritmo"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "TipoParticion"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "TamSO"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "CantPart"))
        self.btn_comenzar.setText(_translate("MainWindow", "Comenzar"))
        self.label_4.setText(_translate("MainWindow", "Memoria"))
        self.label_5.setText(_translate("MainWindow", "Quantum:"))
        self.label_6.setText(_translate("MainWindow", "Seleccione carga de proceso"))
        self.btn_retroceder.setText(_translate("MainWindow", "<<<<"))
        self.btn_avanzar.setText(_translate("MainWindow", ">>>>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionsdfsdfafda.setText(_translate("MainWindow", "sdfsdfafda"))
        self.actionConfiguracion_2.setText(_translate("MainWindow", "Configuracion"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionCrear_procesos.setText(_translate("MainWindow", "Crear procesos"))
