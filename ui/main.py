# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(153, 129)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.convocacaoButton = QtWidgets.QPushButton(self.centralwidget)
        self.convocacaoButton.setObjectName("convocacaoButton")
        self.verticalLayout.addWidget(self.convocacaoButton)
        self.ataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ataButton.setObjectName("ataButton")
        self.verticalLayout.addWidget(self.ataButton)
        self.departamentosButton = QtWidgets.QPushButton(self.centralwidget)
        self.departamentosButton.setObjectName("departamentosButton")
        self.verticalLayout.addWidget(self.departamentosButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reuniões"))
        self.convocacaoButton.setText(_translate("MainWindow", "Gerar Convocação"))
        self.ataButton.setText(_translate("MainWindow", "Gerar Ata"))
        self.departamentosButton.setText(_translate("MainWindow", "Editar Departamentos"))

