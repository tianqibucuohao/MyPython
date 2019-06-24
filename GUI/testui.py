# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\MyPython\GUI\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEditAcc = QtWidgets.QLineEdit(Dialog)
        self.lineEditAcc.setGeometry(QtCore.QRect(170, 60, 113, 20))
        self.lineEditAcc.setObjectName("lineEditAcc")
        self.lineEditPwd = QtWidgets.QLineEdit(Dialog)
        self.lineEditPwd.setGeometry(QtCore.QRect(180, 110, 113, 20))
        self.lineEditPwd.setObjectName("lineEditPwd")
        self.acc = QtWidgets.QLabel(Dialog)
        self.acc.setGeometry(QtCore.QRect(40, 60, 71, 31))
        self.acc.setObjectName("acc")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.acc.setText(_translate("Dialog", "Accout"))
        self.label.setText(_translate("Dialog", "pwd"))

