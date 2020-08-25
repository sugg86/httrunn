#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29
# @Author  : mcc
# @Site    :
# @File    : main.py
# @Notes   : 运行
# @Software: PyCharm

import pytest,time,os

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))    # 取当前时间
    pytest.main(["-s","-v","--html=OUTPUTS/reports/pytest.html","--alluredir=OUTPUTS/allure".format(now)])
    # 调用命令生成报告（Windows下面的方法）----------需要下载allure.exe
os.system(".\\configpackage\\allure-2.7.0\\bin\\allure generate OUTPUTS/allure/ -o OUTPUTS/allure/html/report-{0}".format(now))