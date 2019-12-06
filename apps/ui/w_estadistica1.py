# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadistica1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Estadistica1(object):
    def setupUi(self, Estadistica1):
        Estadistica1.setObjectName("Estadistica1")
        Estadistica1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Estadistica1)
        self.centralwidget.setObjectName("centralwidget")
        Estadistica1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Estadistica1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Estadistica1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Estadistica1)
        self.statusbar.setObjectName("statusbar")
        Estadistica1.setStatusBar(self.statusbar)

        self.retranslateUi(Estadistica1)
        QtCore.QMetaObject.connectSlotsByName(Estadistica1)

    def retranslateUi(self, Estadistica1):
        _translate = QtCore.QCoreApplication.translate
        Estadistica1.setWindowTitle(_translate("Estadistica1", "Tiempo De Espera"))
