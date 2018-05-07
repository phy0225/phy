# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:03:59 2018

@author: 01055226
"""


import requests
import urllib

r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')

arr = r.json()['result']['tracks']

for i in range(10):
    name = str(i+1) + ' ' + arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    urllib.request.urlretrieve(link,'网易云音乐\\' + name)
    print(name+'下载完成')
    