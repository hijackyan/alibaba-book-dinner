#! /usr/bin/env python
#coding=utf8

import urllib
import urllib2
import cookielib
import smtplib
import ConfigParser
import os
import sys
import re

def dingcan(user, password):
        opener=login(user, password)
        url_check = "http://bjdc.taobao.ali.com"
	url_cancel = "http://bjdc.taobao.ali.com/budingcan"
        req = urllib2.Request(url_check)
        f = opener.open(req)
        result = f.read().decode("utf-8").encode(sys.getfilesystemencoding())   
	if result.find("/budingcan") != -1:
		print "你已经过餐了"
	else:
		print "你今天还未订餐"
	num = int(raw_input("输入1订餐(覆盖之前所选餐类),输入2退订\n"))
	req = urllib2.Request(url_cancel)
	f = opener.open(req)
	f.read()
	if num == 1:
		success = 1
		while success == 1:
			foodurl = re.findall(r'/dingcan/[0-9]*',result)    
			foodlist = re.findall(r'<h1>(.*)</h1>', result)
			for i in range(0,4):
				print foodlist[i]
			num = int(raw_input("选择你要想的：输入1,2,3或4\n"))
			url_dingcan = url_check+foodurl[(num-1)*2]
        		req = urllib2.Request(url_dingcan)
			f = opener.open(req)
        		result = f.read()
			success = 0
			if result.find("已售") != -1:
				print "卖光了，换一种吧"
				success = 1
	print "操作完成"
	   
def login(user, password) :
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    data = {"name": user, "pass": password, "form_id": "user_login_block"}
    url_login = "http://bjdc.taobao.ali.com/"
    req = urllib2.Request(url_login, urllib.urlencode(data))
    f = opener.open(req)
    return opener



if __name__ == "__main__":
    user = ""
    password = "" 
    dingcan(user, password)
