# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:08:35 2018

@author: 01055226
"""

import urllib
import os
from bs4 import BeautifulSoup

def urlBS(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    return soup

def main(url,time):
    soup = urlBS(url)
    link = soup.select('.booklist a')
    path = os.getcwd() + '\\读者文摘\\'+'\\'+time+'\\'
    if not os.path.isdir(path):
        os.mkdir(path)
    for item in link:
        newurl = baseurl + item['href']
        result = urlBS(newurl)
        title = result.find('h1').string
        writer = result.find(id='pub_date').string.strip()
        filename = path+title+'.txt'
        print(filename)
        new = open(filename,'w')
        new.write("<<" + title + ">>\n\n")
        new.write(writer+'\n\n')
        text = result.select('.blkContainerSblkCon p')
        for p in text:
            context = p.text
            new.write(context)
            
        new.close()
        
        
if __name__ == '__main__':
    time = '2017_16'
    baseurl = 'http://www.52duzhe.com/' + time +'/'  
    fisturl = baseurl + 'index.html'
    main(fisturl,time)
