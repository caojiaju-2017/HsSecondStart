#coding: utf-8

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel

from Service import *
from CallHandler import  CallHandler
from ByPlatform.Base.OutPutHelper import *
from ShareData import *
# from UIPackage.ActiveWindow import *
app = None
class MainWindow(QMainWindow):

    cmTSignal = pyqtSignal(int,str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # OutPutHelper.consolePrint("Terminal UI Load Finish1")
        self.setWindowTitle("client")
        # OutPutHelper.consolePrint("Terminal UI Load Finish2")
        # self.backLogFile("runlog.log")
        # OutPutHelper.consolePrint("Terminal UI Load Finish3")
        self.showFullScreen()
        # OutPutHelper.consolePrint("Terminal UI Load Finish4")
        self.setWindowIcon(QIcon('icons/icon.png'))
        # OutPutHelper.consolePrint("Terminal UI Load Finish5")
        #self.resize(900, 600)
        self.show()
        # OutPutHelper.consolePrint("Terminal UI Load Finish6")
        # 设置窗体背景颜色
        self.setStyleSheet("background-color:gray;")
        # OutPutHelper.consolePrint("Terminal UI Load Finish7")
        settings = QWebEngineSettings.globalSettings()
        # OutPutHelper.consolePrint("Terminal UI Load Finish8")
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        # OutPutHelper.consolePrint("Terminal UI Load Finish9")
        self.browser = QWebEngineView()
        # OutPutHelper.consolePrint("Terminal UI Load Finish10")
        # 注册通信信道
        self.channel  = QWebChannel()
        # OutPutHelper.consolePrint("Terminal UI Load Finish11")
        self.handler = CallHandler()
        # OutPutHelper.consolePrint("Terminal UI Load Finish12")
        self.handler.wndHandle = self
        # OutPutHelper.consolePrint("Terminal UI Load Finish13")
        self.channel .registerObject('backend', self.handler)
        self.browser.page().setWebChannel(self.channel )

        self.browser.load(QUrl("http://www.baidu.com"))

        self.setCentralWidget(self.browser)
        # OutPutHelper.consolePrint("Terminal UI Load Finish15")
        # 控件暂时不予显示，但是加载
        self.browser.setVisible(True)
        # OutPutHelper.consolePrint("Terminal UI Load Finish16")
        OutPutHelper.Logger_CallBack = LoggerUtil.writeFile
        OutPutHelper.consolePrint("Terminal UI Load Finish")

        #前端启动入口
        self.adService = Service(self)
        # self.cmTSignal.connect(self.adService.handleMessage)
        ShareData.Global_Win_Handle = self
        self.adService.startService()


    def backLogFile(self,filename):
        # 检查日志文件大小
        if not os.path.exists(filename):
            return

        # 如果超过3m，则备份
        logsize = os.path.getsize(filename)
        OutPutHelper.consolePrint("logFile size = %d"% logsize)

        if logsize < 3*1024*1024:
            return

        abc = TimeHelper.getCurrentDate()
        try:
            bakLog = abc + ".bak"
            shutil.move(filename,bakLog)
            shutil.rmtree(filename)
        except Exception as ex:
            return
        pass

    def switchAd(self):
        self.browser.load(QUrl("D:/Work/SVNRep/BYAdPlatform/4.Code/WinTerminalPyQT/Res/ffffffffffffffffffffffffffffffff/index_win.html"))
        self.setCentralWidget(self.browser)        
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit()
    sys.exit(app.exec_())


#https://blog.csdn.net/saga1979/article/details/51734001
