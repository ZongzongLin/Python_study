# coding=utf-8
import re
import urllib
import urllib2
import time
sy_time = 0
dj_time = 0
for k in range(11):
    url = 'http://www.library.fudan.edu.cn/main/list/1125-'+str(k+1)+'-20.htm'
    f = urllib.urlopen(url)
    page = f.read()

    pattern1 = re.compile(r'target="_blank">([\s\S]*?)</a>')
    pattern2 = re.compile(r'<span style="float:right;">([\s\S]*?)</span>')
    title = re.findall(pattern1, page)
    times = re.findall(pattern2, page)

    title = title[15:len(times)+15]

    for i in range(len(times)):
        print 'No.'+str(i+1+k*20)+' '+'time:'+str(times[i])+' '+'title:'+str(title[i])
        if i != len(title):
            time.sleep(0.1)
    stru = ''.join(title)
    stru = unicode(stru, "utf-8")
    shiyong = re.findall(u'试用', stru)
    if len(shiyong) > 0:
        sy_time = sy_time+len(shiyong)
    dingou = re.findall(u'订购', stru)
    if len(dingou) > 0:
        dj_time = dj_time+len(dingou)
print '爬虫爬完啦！总共试用' + str(sy_time)+'次,'+'订购'+str(dj_time)+'次.'
