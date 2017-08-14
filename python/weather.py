#coding:utf_8

import requests
import time
import csv
from bs4 import BeautifulSoup

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")

def get_url(city):
    url = 'http://www.weather.com.cn/weather/'
    with open('city.txt','r',encoding='utf-8') as fs:
        lines=fs.readlines()
        for line in lines:
            if city in line:
                code=line.split('=')[0].strip()
                return url+code+'.shtml'

    raise ValueError('invalit city name')


def get_content(url,date=None):
    re=requests.get(url,timeout=60)
    re.encoding='utf-8'
    return re.text

def getdata(text,city):
    content=[]
    bs=BeautifulSoup(text, "html.parser")
    body=bs.body
    data=body.find('div',{'id':'7d'})
    ul=data.find('ul')
    li=ul.find_all('li')
    for day in li:
        line=[city]
        date=day.find('h1').content
        line.append(date)
        text=day.find_all('p')
        line.append(text[0].string)
        if text[1].find('span') is None:
            tem_h=None
        else:
            tem_h=text[1].find('span').string.replace('℃','')
        tem_l=text[1].find('i').string.replace('℃','')
        line.append(tem_h)
        line.append(tem_l)
        content.append(line)
    return content

def saveContent(data,filename):
    with open(filename,'a',errors='ignore',newline='') as f:
        f_csv=csv.writer(f)
        f_csv.writerows(data)



if __name__ == '__main__':
    cities=input('city_name:').split(' ')
    for city in cities:
        url=get_url(city)
        content=get_content(url)
        result=getdata(content,city)
        saveContent(result,'/Users/wangxiaojie/Desktop/python/weather.csv')













