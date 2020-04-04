import requests
import threading
import os
import shutil

path=os.getcwd()
print("your current dictionary is "+ path)


t=[]
def core():
    code=str(input("the file code: "))
    url="https://hentaifox.com/g/"+ code +"/1/"
    #print(url)
    req=requests.get(url)
    r=req.text
    first='''class="total_pages">'''
    last='''</span></button>'''
    global pages
    pages=r[r.find(first)+len(first):r.find(last)].strip()
    print(pages)
    one='''<a class="next_img"><img id="gimg" class="lazy image_1" src="'''
    two='''1.jpg'''
    global link
    link=r[r.find(one)+len(one):r.find(two)].strip()
    print(link)
    global new_path
    new_path=path +"/"+ code
    dis=os.mkdir(new_path)
 
    

def dow(i):
    x=requests.get(link+ str(i) +".jpg")
    print("downloading "+ str(i) +"-th image")
    file=open(new_path +"/"+ str(i) +'.jpg',"wb")
    file.write(x.content)
    file.close     
    
core()

page=int(pages)+1
for i in range (1,int(page)):
    thread=threading.Thread(target=dow,args=(str(i),))
    t.append(thread)
    thread.start()
    
for im in t:
    im.join()
    
print("all done")
shutil.make_archive(str(new_path),"zip",new_path)
shutil.rmtree(str(new_path))