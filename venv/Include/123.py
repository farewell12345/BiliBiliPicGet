import requests
import json
import random
from lxml import etree
from bs4 import BeautifulSoup
import urllib
try:
    with open('path.txt') as m:
        path=m.readline()
        print("当前路径："+path)
except:
    path=r"C:\Users\Administrator\Downloads\\"
    print("默认路径："+path+"\n请确定该路径是否正确，若不正确请更改路径")
while 1:
    print("输入0更改下载目录,输入-1退出\n输入1使用网页链接爬取")
    print("请输入视频av号：例如：av170001：\n")
    str = input()
    
    if str=='0':
        print("请输入你的下载路径：")
        path=input();
        with open('path.txt','w') as f:
            f.write(path)
        print("路径修改成功")
        continue;
    elif str=='-1':
        break
    try:

        if str!='1':
            if str[0] == 'A':
                str = str.replace('A', 'a')
            if str[1] == 'V':
                str = str.replace('V', 'v')
            data = requests.get("https://www.bilibili.com/video/"+str+"/?redirectFrom=h5")
        else :
            print("请输入视频链接地址：例如：av170001：\n")
            str = input()
            data = requests.get(str)
        data.encoding='utf-8'
        text=data.text
        if text:
            soup=BeautifulSoup(text,'html.parser')
            name=soup.find_all('title')
            fileName=name[0].text
            headers = soup.find_all('meta',itemprop='image')
            i=0
            for header in headers:
                i+=1
                url = header['content']
                src=requests.get(url)
                file=path+fileName+".jpg"
                f=open(file,'wb')
                f.write(src.content)
                print("下载成功，目录："+file)

        else:print("下载失败")
    except:
        print("视频无效或链接有误")
