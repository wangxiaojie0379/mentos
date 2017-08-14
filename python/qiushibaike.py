#coding:utf-8




import requests
from bs4 import BeautifulSoup
import random
import time
import urllib.response
from urllib import error

class QSBK:

    def __init__(self):
        self.page=1
        self.stores=[]
        self.enable=False

    def getPageContent(self,pageIndex):
        header={
            'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        try:
            re=requests.get(url,headers=header)
            re.encoding='utf-8'
            return re.text
        except error.URLError as e:
            if hasattr(e,"reason"):
                print('连接失败')
                return None

    def getPageItems(self,pageIndex):
        pageCode=self.getPageContent(pageIndex)
        if not pageCode:
            print('加载失败')
            return None
        bs=BeautifulSoup(pageCode,'html.parser')
        body=bs.body
        a=body.find_all('div',{'class':'content'})
        pageStores=[]
        for item in a:
            b=item.find('span')
            pageStores.append(b.get_text())
        return pageStores

    def loadPage(self):
        if self.enable==True:
            if len(self.stores)<2:
                pageStores=self.getPageItems(self.page)
                if pageStores:
                    self.stores.append(pageStores)
                    self.page+=1

    def getOneItems(self,pageStores,page):
        for story in pageStores:
            inp=input()
            self.loadPage()
            if inp =='Q':
                self.enable=False
                return
            print(story)
    def start(self):
        print ("正在读取糗事百科,按回车查看新段子，Q退出")
        self.enable=True
        self.loadPage()
        nowPage=0
        while self.enable:
            if len(self.stores)>0:
                pageStores=self.stores[0]
                nowPage+=1
                del self.stores[0]
                self.getOneItems(pageStores,nowPage)






spider=QSBK()
spider.start()





