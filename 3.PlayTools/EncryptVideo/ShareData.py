#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 0 表示乐山商业银行 ；1 表示四川中国银行 2 表示郑州中国银行  3 表示贵州中国银行
class HomeType(object):
    LeShan = 0
    SiChuanZhongHang = 1
    ZhengzhouHang = 2
    GuizhouHang = 3
    Testing = 99
class ShareData(object):
    Global_Win_Handle = None
    Current_Channel_Code = "ffffffffffffffffffffffffffffffff"
    AppScene = HomeType.Testing