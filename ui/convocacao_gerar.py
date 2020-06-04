# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convocacao_gerar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 560)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.docText = QtWidgets.QTextBrowser(self.centralwidget)
        self.docText.setObjectName("docText")
        self.verticalLayout_2.addWidget(self.docText)
        self.wordButton = QtWidgets.QPushButton(self.centralwidget)
        self.wordButton.setObjectName("wordButton")
        self.verticalLayout_2.addWidget(self.wordButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.emailText = QtWidgets.QTextBrowser(self.centralwidget)
        self.emailText.setObjectName("emailText")
        self.verticalLayout.addWidget(self.emailText)
        self.emailButton = QtWidgets.QPushButton(self.centralwidget)
        self.emailButton.setObjectName("emailButton")
        self.verticalLayout.addWidget(self.emailButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerar Convocação"))
        self.label.setText(_translate("MainWindow", "Documento"))
        self.wordButton.setText(_translate("MainWindow", "Gerar arquivo word"))
        self.label_2.setText(_translate("MainWindow", "E-mail"))
        self.emailButton.setText(_translate("MainWindow", "Copiar texto do e-mail"))

