#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSlot
from ByPlatform.Base.OutPutHelper import *
class CallHandler(QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wndHandle = None
    @pyqtSlot(result=str)
    def currentPlayComplete(self):
        OutPutHelper.consolePrint("Recieve ADSwitch Event from html5")
        self.wndHandle.cmTSignal.emit(90001, None)
        return 'hello, Python'
