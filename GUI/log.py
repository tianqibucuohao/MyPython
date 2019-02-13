# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:15:54 2019

@author: Administrator
"""

from PyQt5 import QtCore, QtGui, uic, QtWidgets
 
qtCreatorFile = "UI\\mainwindow.ui" # Enter file here.

if (__name__ == "__main__"):
    ui = uic.loadUi(qtCreatorFile)
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(qtCreatorFile)
    #MainWindow.show()
    #sys.exit(app.exec_())
