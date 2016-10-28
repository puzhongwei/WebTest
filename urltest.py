# -*- coding: utf-8 -*
import os
import re
import shutil
import urllib2
import  time
import requests
import httplib

# connect to a URL
def testurl(url):
    website = urllib2.urlopen(url)
    # read html code
    html = website.read()
    # use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://.*?)"', html)  ###".*?"任意匹配
    fp=open('url.txt','w')
    for i in links :
        '''if ' 2x' in i[0]:
            s=i[0][:-3]
            print  >> fp,s
        else:'''
        print >> fp, i[0]
    fp.close()
    a=0
    b=0
    for line in open("url.txt"):
        if ',' in line:
            s=line.split(',')
            for i in s:
                try:
                    if ' ' in i:
                        s3=i.split(' ')
                        for s4 in s3:
                            if len(s4)>5:
                                i=s4
                    res = urllib2.urlopen(i)
                    code = res.getcode()
                    res.close()
                    print i
                    print code
                    a=a+1
                except Exception:
                    print i
                    print 'error'
                    b = b + 1
        else:
            try:
                res = urllib2.urlopen(line)
                code = res.getcode()
                res.close()
                print line
                print res.getcode()
                a=a+1
            except Exception:
                 print line
                 print 'error'
                 b=b+1

    print "成功:  {0}".format(a)
    print "失败:  {0}".format(b)


