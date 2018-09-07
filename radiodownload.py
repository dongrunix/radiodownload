#coding:utf-8 
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import wget

def download(url):
    #Chrome改FireFox
    driver=webdriver.Chrome()
    driver.get(url)
    html=driver.page_source
    driver.close()
    soup = BeautifulSoup(html,'lxml')
    allherf=soup.find_all('a')
    for herf in allherf:
        try:
            if('.m4a' in herf.attrs['onclick']):
                print(herf.attrs['onclick'].split("\'")[1].split('/')[-1])
                wget.download('http://'+herf.attrs['onclick'].split("\'")[1],herf.attrs['onclick'].split("\'")[1].split('/')[-1])     
        except:
            pass

if __name__=='__main__':
    url='http://www.radio.cn/pc-portal/sanji/zhibo_2.html?channelname=2&name=520799&title=radio'
    download(url)