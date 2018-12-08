#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import socket
import struct
import time
import psutil
import uuid
from ByPlatform.Base.OutPutHelper import *
class Util(object):
    @staticmethod
    def getSign(params, signKey):
        # 构建参数对象，并提取sign参数
        paramList = []

        for key in params:
            paramList.append((key,params[key]))

        # 参数排序
        paramList = sorted(paramList,key=lambda  x:x[0])

        # 转字符串
        signString = ""
        for oneParam in paramList:
            key = oneParam[0]
            value = oneParam[1]
            if not value:
                value  = "None"
            signString = signString + key + "=" + value

        # 添加产品KEY
        signString = signString + signKey       
       
        # print(signString)
        m1 = hashlib.md5()

        try:
            m1.update(signString.encode(encoding='utf-8'))
        except:
            m1.update(signString)
        return m1.hexdigest()    
    
    @staticmethod
    def getHostIp():
        # return "192.168.1.208"
        myname = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        return myaddr

    @staticmethod
    def getHostMac():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    @staticmethod
    def getHostCpuUseage():
        return str(int(psutil.cpu_percent(1)))

    @staticmethod
    def getHostDiskUseage():
        return "79"

    @staticmethod
    def getHostMemoryUseage():
        phymem = psutil.virtual_memory()
        used = int(phymem.used/1024/1024)
        total = int(phymem.total/1024/1024)
        percent = used*1.00/total
        return str(int(percent))

        
