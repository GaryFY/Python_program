#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket#导入 socket 模块

s = socket.socket()#创建 socket 对象
host = socket.gethostname()#获取本地主机名
port = 12345#设置端口好

s.connect((host, port))#socket.connect(hostname,port)打开一个TCP连接到主机为hostname端口的port的服务器
print s.recv(1024)
s.close()#关闭连接