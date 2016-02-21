import os
import re
import urllib.request
targetadd = r"D:\pythonspace\downloadimg"

def getHtml (url):
    webheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req=urllib.request.Request(url=url,headers=webheader)
    webpage = urllib.request.urlopen(req)
    return webpage.read()

def getUrl(html):
    reg = r'<img src="(.*?\.png)"'
    urllist = re.findall(reg,html.decode('utf-8'))
    return urllist

def getImg(urllist):
    if not os.path.isdir(targetadd):
        os.mkdir(targetadd)
    for i in urllist:
        print(i)
        pos = i.rindex('/')
        try:
            imgpath = os.path.join(targetadd,i[pos+1:])
            urllib.request.urlretrieve(i,imgpath)
        except:
            print('失败')

if __name__ =="__main__":
    weburl="http://simpledesktops.com"
    html = getHtml(weburl)
    urllist = getUrl(html)
    getImg(urllist)
