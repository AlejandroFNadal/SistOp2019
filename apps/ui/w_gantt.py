# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gantt.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_image_gantt(object):
    def setupUi(self, image_gantt):
        image_gantt.setObjectName("image_gantt")
        image_gantt.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(image_gantt)
        self.centralwidget.setObjectName("centralwidget")
        self.label_gantt = QtWidgets.QLabel(self.centralwidget)
        self.label_gantt.setGeometry(QtCore.QRect(10, 15, 761, 511))
        self.label_gantt.setText("")
        self.label_gantt.setObjectName("label_gantt")
        image_gantt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(image_gantt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        image_gantt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(image_gantt)
        self.statusbar.setObjectName("statusbar")
        image_gantt.setStatusBar(self.statusbar)

        self.retranslateUi(image_gantt)
        QtCore.QMetaObject.connectSlotsByName(image_gantt)

    def retranslateUi(self, image_gantt):
        _translate = QtCore.QCoreApplication.translate
        image_gantt.setWindowTitle(_translate("image_gantt", "Gantt"))
