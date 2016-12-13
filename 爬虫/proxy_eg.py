### 使用代理IP进行访问 ###

import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
# 代理IP列表
iplist = ['124.88.67.30:83','60.194.100.51:80','110.18.241.9:3128']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
# 定制、创建一个opener
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')]
# 安装opener
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
