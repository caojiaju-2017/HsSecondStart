# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActiveUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 269)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.leDeviceID = QtWidgets.QLineEdit(Dialog)
        self.leDeviceID.setGeometry(QtCore.QRect(120, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leDeviceID.setFont(font)
        self.leDeviceID.setReadOnly(True)
        self.leDeviceID.setObjectName("leDeviceID")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.leRegisterCode = QtWidgets.QLineEdit(Dialog)
        self.leRegisterCode.setGeometry(QtCore.QRect(120, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leRegisterCode.setFont(font)
        self.leRegisterCode.setObjectName("leRegisterCode")
        self.backLabel = MyLabel(Dialog)
        self.backLabel.setGeometry(QtCore.QRect(20, 180, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backLabel.setFont(font)
        self.backLabel.setObjectName("backLabel")
        self.saveLabel = MyLabel(Dialog)
        self.saveLabel.setGeometry(QtCore.QRect(240, 180, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveLabel.setFont(font)
        self.saveLabel.setObjectName("saveLabel")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 321, 251))
        self.widget.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.widget.setObjectName("widget")
        self.backLabel.raise_()
        self.saveLabel.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.leDeviceID.raise_()
        self.label_2.raise_()
        self.leRegisterCode.raise_()
        self.backLabel.raise_()
        self.saveLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "设备ID"))
        self.leDeviceID.setText(_translate("Dialog", "0a0027000005"))
        self.label_2.setText(_translate("Dialog", "注册码"))
        self.backLabel.setText(_translate("Dialog", "TextLabel"))
        self.saveLabel.setText(_translate("Dialog", "TextLabel"))

from MyLabel import MyLabel
