#!/usr/bin/python
# -*- coding:utf-8 -*-


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from ByPlatform.Base.OutPutHelper import *
import sys
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from ByPlatform.Base.UtilHelper import *
from UIDesigner.ActiveUI import Ui_Dialog
from ByPlatform.Base.OutPutHelper import *
# from ByPlatform.StorageHelper.StorageHelper import *
from ByPlatform.EncryptionHelper.EncryptionHelper import *
import pickle

class ActiveWindow(QDialog,Ui_Dialog):
    """docstring for myDialog"""
    def __init__(self, arg=None):
        super(ActiveWindow, self).__init__(arg)
        self.setupUi(self)

        # self.setWindowIcon(QIcon(r'Res\logo.png'))
        self.setWindowTitle("软件注册")

        self.newLicense = None
        self.initControl()

        self.leDeviceID.setText("h-sen@foxmail.com")
        self.leRegisterCode.setText("de71dd83d792834b1b76e3f8e864e30a")

    def initControl(self):
        self.setObjectName("ActiveWindow")
        self.setStyleSheet("#ActiveWindow{background-color: #F2F2F2;}")

        maxSize = 40
        self.backLabel.MyLabelPressedSignal.connect(self.goBack)
        png = QPixmap(r'Res\back.png').scaled(QSize(maxSize,maxSize))
        self.backLabel.setAlignment(Qt.AlignCenter)
        self.backLabel.setPixmap(png)
        self.backLabel.setStyleSheet(
            "#backLabel{border-radius:6px; background:rgba(200, 200, 200,0); color:white;}" + "#backLabel:hover{background:rgb(255,128,64);}")

        self.saveLabel.MyLabelPressedSignal.connect(self.saveData)
        png = QPixmap(r'Res\save.png').scaled(QSize(maxSize,maxSize))
        self.saveLabel.setAlignment(Qt.AlignCenter)
        self.saveLabel.setPixmap(png)
        self.saveLabel.setStyleSheet(
            "#saveLabel{border-radius:6px; background:rgba(200, 200, 200,0); color:white;}" + "#saveLabel:hover{background:rgb(255,128,64);}")
        #
        # # self.erweimaLabel.MyLabelPressedSignal.connect(self.saveData)
        # png = QPixmap(r'Res\contact.jpg').scaled(self.erweimaLabel.size())
        # self.erweimaLabel.setAlignment(Qt.AlignCenter)
        # self.erweimaLabel.setPixmap(png)
        # self.erweimaLabel.setStyleSheet(
        #     "#erweimaLabel{border-radius:6px; background:rgba(200, 200, 200,0); color:white;}" + "#erweimaLabel:hover{background:rgb(255,128,64);}")
        #

        # self.leAccountPasswd.setEchoMode(QLineEdit_EchoMode=Qt.Pass===========)
        self.leDeviceID.setStyleSheet(
            "#leDeviceID{border:2px groove gray;border-radius:4px; background:rgba(255, 255, 255,1); color:black;}" + "#leDeviceID:hover{background:rgb(255, 255, 255);}")

        self.leRegisterCode.setStyleSheet(
            "#leRegisterCode{border:2px groove gray;border-radius:4px; background:rgba(255, 255, 255,1); color:black;}" + "#leRegisterCode:hover{background:rgb(255, 255, 255);}")


        pass

    def saveData(self):
        emailAddress = self.leDeviceID.text()
        registerCode = self.leRegisterCode.text()

        emailAddress = "b%sy"% emailAddress
        emailAddress = emailAddress.lower()
        snCode = EncryptionHelper.Md5String(emailAddress)

        if snCode == registerCode:
        # if 1 == 1:
            self.accept()
        else:
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "错误",
                                            "注册码错误",
                                            QMessageBox.Yes)

        # self.accept()


    def setData(self,licenseData):
        if not licenseData:
            return

        self.leDeviceID.setText(licenseData.email)
        self.leRegisterCode.setText(licenseData.lisencekey)

    def addSubUrl(self):
        # self.lvSubList.
        # self.subUrlList.append()
        self.lvSubList.addItem(self.leSubUrl.text())
        pass

    def listItemDoubleClicked(self, item):
        # 提示信息弹窗，你选择的信息
        # self.lvSubList.removeItemWidget(item)
        # OutPutHelper.consolePrint("listItemDoubleClicked")
        # del item
        # abItem = self.lvSubList.currentIndex()
        # rowIndex = QModelIndex().row()
        OutPutHelper.consolePrint(item.text())
        self.leSubUrl.setText(item.text())
        self.lvSubList.takeItem(self.lvSubList.currentIndex().row())
    def goBack(self):
        self.reject()
        pass
