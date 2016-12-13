### 下载页面的图片 ###
import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p =r'<img class="BDE_Image" src="([^"]+\.jpg)"'# ^"除了",+重复多次
    imglist = re.findall(p,html)
    '''
    for each in imglist:
        print(each)
    '''
    for each in imglist:
        filename = each.split("/")[-1]# 最后一个是文件名
        urllib.request.urlretrieve(each,filename,None)
    
if __name__ ==  '__main__':
    url = "http://tieba.baidu.com/p/4886392799"
    get_img(open_url(url))
