# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#! 获取一个get请求
# repose = urllib.request.urlopen('http://www.baidu.com')
#! 对获取的网页进行utf-8的解码
# print(repose.read().decode('utf-8'))

#! 获取一个host请求
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf -8")
repose=urllib.request.urlopen("http://httpbin.org/post", data=data)
print(repose.read().decode('utf-8'))

