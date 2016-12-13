### 下载页面的图片 ###
import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'(?:(?:[0,1])?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1])?\d?\d|2[0-4]\d|25[0-5])'# ?匹配前面一次或没有
    iplist = re.findall(p,html)
    
    for each in iplist:
        print(each)
    
    '''
    for each in iplist:
        filename = each.split("/")[-1]# 最后一个是文件名
        urllib.request.urlretrieve(each,filename,None)
    '''
    
if __name__ ==  '__main__':
    url = "http://cn-proxy.com"
    get_img(open_url(url))
