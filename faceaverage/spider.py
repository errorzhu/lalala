# -*- coding:utf-8 -*-
import  requests
import re
import json
import urllib
url3='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%AF%81%E4%BB%B6%E7%85%A7%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E8%AF%81%E4%BB%B6%E7%85%A7%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={id}&rn=30&gsm=b4&1492507141415='
url2='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B1%ED%C7%E9%B0%FC&fr=ala&ori_query=%E8%A1%A8%E6%83%85%E5%8C%85&ala=0&alatpl=sp&pos=0&hs=2&xthttps=111111'
url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1503587687338_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%AF%81%E4%BB%B6%E7%85%A7%E5%A5%B3&f=3&oq=%E8%AF%81%E4%BB%B6%E7%85%A7&rsp=0'
headers ={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1503585105843_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%A7%E5%AD%A6%E7%94%9F+%E8%AF%81%E4%BB%B6%E7%85%A7',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}
index = 0
def parse_json(j):
    global index
    res = json.loads(j)
    datas = res ['data']
    for data in datas:
        image = data.get('thumbURL')
        print index
        down_image(image, index)
        index = index + 1

def get_page(pagenum):
    session = requests.session()
    session.headers = headers
    url = url3.format(id = pagenum)
    print url
    page = session.get(url)
    return page.content

def down_image(url,num):
    if url is not None:
        urllib.urlretrieve(url,r'e:\face\%s.jpg'%num)

def get_page2():
    html = requests.get(url2)
    print html.status_code
    print html.text
if __name__=="__main__":
    for i in range(20,22):
        response = get_page(i)
        parse_json(response)
