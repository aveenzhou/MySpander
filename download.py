#coding=utf-8
'''
Created on 2015-9-25

@author: Administrator
'''
import os 
import urllib3
from bs4 import BeautifulSoup


http = urllib3.PoolManager(100)

def down_pics_to_folder(source_url,mainflag=0,dir=''):
    '''
        source_url:资源页面地址
        mainflag:是否只下载主图
        dir:下载存放目录
    '''
    
    try:
        agent_header={"User-Agent":r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
        r=http.request('GET',source_url,headers=agent_header)
        if r.status==200:
            html_doc=r.data
            
            soup=BeautifulSoup(html_doc,'html.parser')
            baobao_num_doc=soup.find(id='ECS_FORMBUY')
            number=baobao_num_doc.find('li',class_='sn1').get_text().split(':')[1].split('-')[0].strip()
            folder_name='_N_'+number
            print "**",folder_name
            folder_dir_path=os.path.join(dir,folder_name)
            if not os.path.exists(folder_dir_path):
                os.mkdir(folder_dir_path)
                
            tmp_files_dir_path=os.path.join(folder_dir_path,'tmp_files')
            if not os.path.exists(tmp_files_dir_path):
                os.mkdir(tmp_files_dir_path)
            
            #获取主图
            main_pic_doc=soup.find(id='demo1')
            img_urls=[i.get('href') for i in main_pic_doc.find_all('a') ]
            color_doc=baobao_num_doc.find('div',class_='info_color')
            colors_imgs_doc=color_doc.find_all('img',class_='img')
            colors_imgs=[i.get('src').split('/')[-1].split('_')[0]  for i in colors_imgs_doc]
            
            main_img_len=len(img_urls)
            main_img_url_prev='/'.join(img_urls[0].split('/')[0:-1])
            
            for i in range(1,main_img_len+1):
                for j in colors_imgs:
                    img_urls.append('/'.join([main_img_url_prev,'_'.join([j,'0%s.jpg' % i])]))
                    
            
            for url in img_urls:
                name=url.split('/')[-1]
                res=http.request('GET',url)
                
                with open(os.path.join(folder_dir_path,name),'wb') as fd:
                    fd.write(res.data)
                    
                print 'Down the main pic %s ok' % name
                
            if mainflag:
                return  tmp_files_dir_path,folder_dir_path   
            #获取描述图片
            description_doc=soup.find(id='description')
            imgs=description_doc.find_all('img',{'class','lazyload'})
                      
            for img in imgs:
                img_url=img.get('original')
                name=img_url.split('/')[-1]
                res=http.request('GET',img_url)
                
                with open(os.path.join(tmp_files_dir_path,name),'wb') as fd:
                    fd.write(res.data)
                print 'Down the desciption pic %s ok' % name
                
            return  tmp_files_dir_path,folder_dir_path   
        else:
            print "Response status %s" % r.status
            
    except Exception,e:
        import traceback
        print traceback.format_exc()
        print "Download pics error %s" % str(e)
        


if __name__=="__main__":
    down_pics_to_folder(r'http://www.bagtree.cn/goods-8240.html?pf=search',r'H:\products\NUCELLE\_N_1170642')

