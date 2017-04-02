#coding=utf8
'''
Created on 2017-1-10

@author: chowpeng
'''
from PIL import Image
import os


def pasteLogo(source_img_dir,logo_img,logo_pos):
    files=os.listdir(source_img_dir)
    
    print "*****Start paste logo for main picture*****"
    if len(files)>0:
        for item in files:
            item_name_c=item.split(".")

            if item_name_c[-1]=='jpg' and len(item_name_c[0].split("_"))>1 and item_name_c[0].split("_")[1]=='01':
                source_img_path = os.path.join(source_img_dir,item)
                try:
                    source_img = Image.open(source_img_path)
                except IOError,e:
                    print "Open pic %s error,%s " % (item,e)
                    continue
                
                try:
                    logo = Image.open(logo_img)
                except IOError,e:
                    print "Open logo pic error,%s" % e
                    break
                try:
                    source_img.paste(logo,(logo_pos[0],logo_pos[1]))
                    source_img.save(source_img_path)
                except Exception,e:
                    print "Paste logo error,%s",e
                    continue
                
                
        
    else:
        print "There are no image to paste logo"
    
    print "Paste successfully!"    



if __name__=="__main__":
    
    source_img_dir = r"H:\smt\products\SAMMONS\_N_190404"
    logo_img = r"H:\smt\products\SAMMONS\sammons.png"
    pasteLogo(source_img_dir,logo_img,(30,30))
    
    
    
    
    
    
    