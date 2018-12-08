#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging, sys
#https://blog.csdn.net/langb2014/article/details/53397164
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

class LoggerUtil(object):
    globalHandle = logging.getLogger("AdService")
    # formatter = logging.Formatter('%(asctime)s %(threadName)-8s %(levelname)-8s  [%(module)s->%(funcName)s->%(lineno)d] : %(message)s')
    formatter = logging.Formatter('%(message)s')
    FILE_NAME = "runlog.log"
    # file_handler = logging.FileHandler(FILE_NAME)
    file_handler = TimedRotatingFileHandler(filename=FILE_NAME, when="D", interval=1, backupCount=7)

    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值

    # 为logger添加的日志处理器
    globalHandle.addHandler(file_handler)
    globalHandle.addHandler(console_handler)
    globalHandle.setLevel(logging.INFO)

    @staticmethod
    def writeFile(logstr, logstrFormat):
        LoggerUtil.globalHandle.info(logstrFormat)
        pass

    @staticmethod
    def clearLog():
        # LoggerUtil.globalHandle.c
        return
#
#    @staticmethod
#    def writeDebug(msg):
#        LoggerUtil.globalHandle.setLevel(logging.INFO)
#        LoggerUtil.globalHandle.debug(msg)
#        
#    @staticmethod
#    def writeInfo(msg):
#        LoggerUtil.globalHandle.setLevel(logging.INFO)
#        LoggerUtil.globalHandle.info(msg)
#
#    @staticmethod
#    def writeWarning(msg):
#        LoggerUtil.globalHandle.setLevel(logging.INFO)
#        LoggerUtil.globalHandle.warn(msg)
#
#    @staticmethod
#    def writeError(msg):
#        LoggerUtil.globalHandle.setLevel(logging.INFO)
#        LoggerUtil.globalHandle.error(msg)       
#       
#    @staticmethod
#    def writeFatal(msg):
#        LoggerUtil.globalHandle.setLevel(logging.INFO)
#        LoggerUtil.globalHandle.fatal(msg)       
#  
#    @staticmethod
#    def writeCritical(msg):
#        LoggerUtil.globalHandle.setLevel(logging.INFO)
#        LoggerUtil.globalHandle.critical(msg)       
     
     
#fmt中允许使用的变量可以参考下表。
#
#%(name)s Logger的名字
#
#%(levelno)s 数字形式的日志级别
#
#%(levelname)s 文本形式的日志级别
#
#%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
#
#%(filename)s 调用日志输出函数的模块的文件名
#
#%(module)s 调用日志输出函数的模块名|
#  formatter = logging.Formatter('%(asctime)s %(threadName)-8s %(levelname)-8s  [%(module)s->%(funcName)s->%(lineno)d] : %(message)s')
#%(funcName)s 调用日志输出函数的函数名|
#
#%(lineno)d 调用日志输出函数的语句所在的代码行
#
#%(created)f 当前时间，用UNIX标准的表示时间的浮点数表示|
#
#%(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数|
#
#%(asctime)s 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
#
#%(thread)d 线程ID。可能没有
#
#%(threadName)s 线程名。可能没有
#
#%(process)d 进程ID。可能没有
#
#%(message)s 用户输出的消息     
     
