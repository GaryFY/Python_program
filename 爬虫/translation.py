### 函数功能：利用有道词典进行翻译 ###

import urllib.request
import urllib.parse# 用于编码
import json# 字符串包含字典（封装好的）
import time

while True:
    content = input("请输入需要翻译的内容(输入”q!退出程序“)：")
    if content == 'q':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    '''
    data = {}
    # 通过查看from data
    data['type'] = 'AUTO'
    data['i'] = content# 要输入的内容
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')# 编码

    #req = urllib.request.Request(url,data,head)
    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')# 解码

    target = json.loads(html)# 载入字符串，得到字典
    target = target['translateResult'][0][0]['tgt']

    print(target)
    time.sleep(5)# 等5s钟
