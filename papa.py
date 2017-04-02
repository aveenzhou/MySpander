#coding=utf-8
'''
Created on 2015-9-23

@author: Administrator
'''

import urllib3
from bs4 import BeautifulSoup

url="http://www.bagtree.cn/goods-8518.html"

name="_N_1170770"

http = urllib3.PoolManager(100)

r=http.request('GET',url)

html_doc=r.data

soup=BeautifulSoup(html_doc,'html.parser')
description=soup.find(id='description')
imgs=description.find_all('img',{'class','lazyload'})
print imgs
for img in imgs:
    img_url=img.get('original')
    name=img_url.split('/')[-1]
    res=http.request('GET',img_url)
    
    with open('baobao/%s' % name,'wb') as fd:
        fd.write(res.data)
        
        
        
        
from PIL import Image
import os
dir=os.path.join(os.getcwd(),'baobao')
files=os.listdir(dir) 
width=0
height=0
for item in files:
    img=Image.open(os.path.join(dir,item))
    size=img.size
    if size[0]>width:
        width=size[0]
    height+=size[1]
    
print width,height    

toImg=Image.new('RGBA',(width,height))

startHeight=0
for item in files:
    fromImg=Image.open(os.path.join(dir,item))
    size=img.size
    toImg.paste(fromImg, (0,startHeight))
    startHeight+=size[1]

toImg.save('baobao/%s.jpg' % name)
print "OK"
    


