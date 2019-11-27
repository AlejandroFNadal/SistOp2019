# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instruccionesDeUso.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_instruccionesDeUso(object):
    def setupUi(self, instruccionesDeUso):
        instruccionesDeUso.setObjectName("instruccionesDeUso")
        instruccionesDeUso.resize(499, 627)
        self.centralwidget = QtWidgets.QWidget(instruccionesDeUso)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 10, 471, 551))
        self.textBrowser.setObjectName("textBrowser")
        instruccionesDeUso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(instruccionesDeUso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 26))
        self.menubar.setObjectName("menubar")
        instruccionesDeUso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(instruccionesDeUso)
        self.statusbar.setObjectName("statusbar")
        instruccionesDeUso.setStatusBar(self.statusbar)

        self.retranslateUi(instruccionesDeUso)
        QtCore.QMetaObject.connectSlotsByName(instruccionesDeUso)

    def retranslateUi(self, instruccionesDeUso):
        _translate = QtCore.QCoreApplication.translate
        instruccionesDeUso.setWindowTitle(_translate("instruccionesDeUso", "Instrucciones de Uso"))
        self.textBrowser.setHtml(_translate("instruccionesDeUso", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Instrucciones de Uso</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Consideracion: </span><span style=\" font-size:8pt;\">Debe existir al menos una configuracion de memoria para poder crear batch de procesos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Para crear una memoria</span><span style=\" font-size:8pt;\">, ventana principal seleccionar menu --&gt; configuraciones o precionar el boton nueva memoria.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Para crear batch de procesos</span><span style=\" font-size:8pt;\">, ventana principal menu --&gt; crear procesos o precionar el boton Crear Procesos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
