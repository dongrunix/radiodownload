#coding:utf-8 
import os
from selenium import webdriver
import wget

def download(url):
    #Chrome改FireFox
    driver=webdriver.Chrome()
    driver.get(url)
    allherf=driver.find_elements_by_link_text('下载')
    for herf in allherf:
        print(herf.get_attribute('onclick').split("\'")[1].split('/')[-1])
        wget.download('http://'+herf.get_attribute('onclick').split("\'")[1],herf.get_attribute('onclick').split("\'")[1].split('/')[-1])     
    driver.close()
if __name__=='__main__':
    url='http://www.radio.cn/pc-portal/sanji/zhibo_2.html?channelname=2&name=520799&title=radio'
    download(url)
