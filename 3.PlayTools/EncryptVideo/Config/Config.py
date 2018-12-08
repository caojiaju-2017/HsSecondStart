#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser, uuid, codecs, time, datetime, pickle, os
from ShareData import *
BASE_CONFIG = 0
LICENSE_CONFIG = 1
ALL_CONFIG = 2
from ByPlatform.Base.NetHelper.NetHelper import *
class LocalConfig(object):
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.baseInfo = None
        self.licenceInfo = None
        self.remoteFtpInfo = None
    
    @staticmethod
    def readConfig():
        rtnLcd = LocalConfig()
        try:

            # 定义配置文件名
            cfgFileName = "config-dev.ini"
            if ShareData.AppScene == HomeType.GuizhouHang:
                cfgFileName = "config-gz.ini"
            elif ShareData.AppScene == HomeType.LeShan:
                cfgFileName = "config-ls.ini"

            # 读取基本配置
            rtnLcd.config.readfp(codecs.open(cfgFileName,"r","utf-8-sig"))
            rtnLcd.baseInfo= LocalConfigData.BaseInfo()
            rtnLcd.baseInfo.ServerIP = rtnLcd.config.get("Base","ServerIP")
            rtnLcd.baseInfo.ServerPort = rtnLcd.config.get("Base","ServerPort")
            # rtnLcd.baseInfo.Name = rtnLcd.config.get("Base","Name")
            rtnLcd.baseInfo.LocalIp = NetHelper.getHostIp()
            rtnLcd.baseInfo.LocalServerPort = int(rtnLcd.config.get("Base","LocalServerPort"))
            rtnLcd.baseInfo.OrgCode = rtnLcd.config.get("Base","OrgCode")
            rtnLcd.baseInfo.Version = rtnLcd.config.get("Base","Version")

            rtnLcd.baseInfo.HeartBeatSep = int(rtnLcd.config.get("Base", "heartbeatsep"))
        except Exception as ex:
            pass
        try:
            rtnLcd.baseInfo.ApplyProgramSep = int(rtnLcd.config.get("Base", "applyprogramsep"))
        except Exception as ex:
            pass

        # 读取二进制配置
        # rtnLcd.licenceInfo = LocalConfigData.LicenseInfo.loadBinaryConfig()
        
        
        return rtnLcd

    def updateOrg(self, orgcode):
        #        更新终端归属单位
        if self.baseInfo == None:
            return
            
        self.baseInfo.OrgCode = orgcode
        
        self.config.set("Base", "OrgCode", orgcode)   
        self.config.write(codecs.open("config.ini", "w"))

    def updateVersion(self, newVer):
        #        更新终端归属单位
        if self.baseInfo == None:
            return

        self.baseInfo.Version = newVer

        self.config.set("Base", "Version", newVer)
        self.config.write(codecs.open("config.ini", "w"))

    def updateName(self, name):
        return
        #        更新终端归属单位
        # if self.baseInfo == None or name == None:
        #     return
        #
        # self.baseInfo.Name = name
        #
        # self.config.set("Base", "name", name)
        # self.config.write(codecs.open("config.ini", "w", "utf-8"))

    def updateLincese(self, license):
        if self.licenceInfo == None:
            return
            
        self.licenceInfo.License = license
        self.saveConfig(LICENSE_CONFIG)
        
    def updateOfflineDate(self):
        if self.licenceInfo == None:
            return
            
        self.licenceInfo.OfflineLoginDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.saveConfig(LICENSE_CONFIG)
    
    def checkOfflineOffdate(self):
        # 检查是否还允许离线播放
        
        # 提取当前日期
        currentDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        
        # 如果当前日期小于 配置中的最后离线登陆日期，则直接返回错误----通常是人为修改系统时间所致
        if self.licenceInfo.OfflineLoginDate and self.licenceInfo.OfflineLoginDate > currentDate:
            return False
        
        if self.licenceInfo.OfflineLoginDate == None or self.licenceInfo.OfflineLoginDate == "":
            if self.licenceInfo.MaxOfflineAllow > 0:
                self.licenceInfo.OfflineLoginDate = currentDate
                self.saveConfig(LICENSE_CONFIG)
            return True
        
        cfgDate = datetime.datetime.strptime(self.licenceInfo.OfflineLoginDate, '%Y-%m-%d')
        delta = datetime.timedelta(days=self.licenceInfo.MaxOfflineAllow)
        n_days = cfgDate + delta
        allowLastDate = n_days.strftime('%Y-%m-%d')
        if allowLastDate >= currentDate:
            return True
        
        return False
    
    def saveConfig(self, type):
        if type == LICENSE_CONFIG:
            self.saveLicenseConfig()
        # elif type == BASE_CONFIG:
        #     self.saveBaseConfig()
        else:
            self.saveLicenseConfig()

    def saveLicenseConfig(self):
        self.licenceInfo.saveConfig()

class LocalConfigData(object):
    def __init__(self):
        # self.baseInfo = None
        # self.licenceInfo = None
        pass

    class BaseInfo(object):
        def __init__(self):
            self.ServerIP= None
            self.ServerPort = -1
            self.Name = None
            self.LocalIp = None
            self.LocalServerPort = -1
            self.OrgCode = None
            self.Version = None
            self.HeartBeatSep = 300

if __name__ == '__main__':
    # main()

    pass