#coding=utf-8
'''
Created on 2015-9-25

@author: Administrator
'''
from PIL import Image
import os



	


def join_pics(pic_dir,save_dir):
    files=os.listdir(pic_dir) 
    width=0
    height=0
    if len(files)>0:
        try:
            temp_files=[]
            for item in files:
                try:
                    img=Image.open(os.path.join(pic_dir,item))
                except IOError,e:
                    print "Open pic %s error,%s " % (item,e)
                    continue
                size=img.size
                if size[0]>width:
                    width=size[0]
                height+=size[1]
                item="%s=%s" % (item,size[1])
                temp_files.append(item)
                
            toImg=Image.new('RGBA',(width,height))
            print "Create new canvcas %s X %s" % (width,height) 
            startHeight=0
            for item in temp_files:
                name=item.split("=")[0]
                height=int(item.split("=")[1])
                print "**",name,height
                fromImg=Image.open(os.path.join(pic_dir,name))
                try:
                    toImg.paste(fromImg, (0,startHeight))
                except IOError,e:
                    continue
                startHeight+=height
            
            toImg.save(os.path.join(save_dir,'desciption.jpg'),quality = 100)
            
            print "Join pic OK"
            
        except Exception,e:
            import traceback
            print traceback.format_exc()
            print "Join pics error %s" % str(e)
    else:
        print "Join pics no pics"
        


if __name__=='__main__':
    join_pics(r'H:\smt\products\ZHULUXUE\_N_280055\tmp_files',
              r'H:\smt\products\ZHULUXUE\_N_280055')   
    
    