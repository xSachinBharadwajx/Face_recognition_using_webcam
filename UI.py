# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Face_blob import *
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    F=Face_blob()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start_Web_Cam = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Web_Cam.setGeometry(QtCore.QRect(100, 30, 161, 61))
        self.Start_Web_Cam.setObjectName("Start_Web_Cam")
        self.Start_Web_Cam.clicked.connect(self.swc)

        self.Collect_Data_button = QtWidgets.QPushButton(self.centralwidget)
        self.Collect_Data_button.setGeometry(QtCore.QRect(100, 170, 161, 61))
        self.Collect_Data_button.setObjectName("Collect_Data_button")
        self.Collect_Data_button.clicked.connect(self.cd)
        
        self.Enter_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter_Name.setGeometry(QtCore.QRect(100, 120, 161, 31))
        self.Enter_Name.setText("")
        self.Enter_Name.setObjectName("Enter_Name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 125, 81, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # OUR own code
    def swc(self):
        self.F.startwebcam()
    
    def cd(self):
        Name = self.Enter_Name.text()
        if Name is not None and Name != '':
            self.F.startwebcam(train=True,Name=Name)
        else:
            msg = QMessageBox()
            msg.setText("Enter a Valid Name")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_Web_Cam.setText(_translate("MainWindow", "Start Web Cam"))
        self.Collect_Data_button.setText(_translate("MainWindow", "Collect Data"))
        self.label.setText(_translate("MainWindow", "Enter Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

