#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading,json
from PyQt5.QtCore import QCoreApplication

from Loger.LoggerUtil import *

from Config.Config import *
from PyQt5.QtCore import pyqtSignal
from ByPlatform.Base.OutPutHelper import *

program_name = "mainWindow"

class Service(object):
    def __init__(self,  whandle):
        self.wndHandle = whandle

        self.cfgHandle = None
        pass
    
    def startService(self):
        # LoggerUtil.globalHandle.info("start service")
        OutPutHelper.consolePrint("Start Local Service")

        # 读取配置文件---
        self.cfgHandle = LocalConfig.readConfig()
        OutPutHelper.consolePrint("Read Config Finish")
        # LoggerUtil.globalHandle.info("read config finish")

    def restart_program(self):
        OutPutHelper.consolePrint("Program Restart self")
        python = sys.executable
        os.execl(python, python, * sys.argv)