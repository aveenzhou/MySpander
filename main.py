#coding=utf-8
'''
Created on 2015-9-25

@author: Administrator
'''
from ConfigParser import ConfigParser
from download import down_pics_to_folder
from joinpics import join_pics
from pastelogo import pasteLogo


cf=ConfigParser()
cf.read('config.ini')

source_url = cf.get('source','url')
print source_url
store_dir  = cf.get('store','dir')
print store_dir
logo_path = cf.get('logo','path')
print logo_path
logo_x=cf.get('logo','x')
logo_y=cf.get('logo','y')
mainflag = int(cf.get('flag','mainPic'))


if __name__=='__main__':
    
    res=down_pics_to_folder(source_url,mainflag,store_dir)
    if res:
        join_pic_dir,store_dir=res
        if not mainflag:
            join_pics(join_pic_dir,store_dir)
        pasteLogo(store_dir,logo_path,(int(logo_x),int(logo_y)))



