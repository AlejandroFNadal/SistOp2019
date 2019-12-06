# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadistica2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Estadistica2(object):
    def setupUi(self, Estadistica2):
        Estadistica2.setObjectName("Estadistica2")
        Estadistica2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Estadistica2)
        self.centralwidget.setObjectName("centralwidget")
        Estadistica2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Estadistica2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Estadistica2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Estadistica2)
        self.statusbar.setObjectName("statusbar")
        Estadistica2.setStatusBar(self.statusbar)

        self.retranslateUi(Estadistica2)
        QtCore.QMetaObject.connectSlotsByName(Estadistica2)

    def retranslateUi(self, Estadistica2):
        _translate = QtCore.QCoreApplication.translate
        Estadistica2.setWindowTitle(_translate("Estadistica2", "Tiempo De Ejecucion"))
