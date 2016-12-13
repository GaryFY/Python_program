#!/usr/bin/python3
#获得格式化的日期asctime()
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
