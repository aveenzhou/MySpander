#coding=utf-8
'''
Created on 2015-9-25

@author: Administrator
'''
import re
from ConfigParser import ConfigParser
from download import down_pics_to_folder
from joinpics import join_pics
from pastelogo import pasteLogo


cf=ConfigParser()
cf.read('config.ini')

reg_lst=re.compile(r"^\[([\s\S]+)\]$")
re_int =re.compile(r"^(\d+)$")
re_float = re.compile(r"^(\d+\.\d+)$")

re_w=re.compile(r"\s")
 


 
def getIni(field,key):
    data = cf.get(field,key)
    if re_int.match(data):
        return int(re_int.match(data).group(1))
    if re_float.match(data):
        return int(re_float.match(data).group(1))
    if reg_lst.match(data):
        try:
            return re_w.sub("",reg_lst.match(data).group(1)).split(",")
        except Exception,e:
            return "data type error"
    
    return data


source_url = getIni('source','url')
print source_url
store_dir  = getIni('store','dir')
print store_dir
logo_path = getIni('logo','path')
print logo_path
logo_x=getIni('logo','x')
logo_y=getIni('logo','y')
mainflag = getIni('flag','mainPic')


def getData(source_url,mainflag,store_dir):
    res=down_pics_to_folder(source_url,mainflag,store_dir)
    if res:
        join_pic_dir,store_dir=res
        if not mainflag:
            join_pics(join_pic_dir,store_dir)
        pasteLogo(store_dir,logo_path,(int(logo_x),int(logo_y)))




if __name__=='__main__':
    
    if type(source_url) is list:
        for url in source_url:
            getData(url,mainflag,store_dir)
    else:
        getData(source_url,mainflag,store_dir)
    
    




