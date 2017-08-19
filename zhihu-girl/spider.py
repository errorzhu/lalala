# -*-  coding: utf-8 -*-
import requests
import json
import re
header={
"Host": "www.zhihu.com",
"Connection": "keep-alive",
"X-UDID": "AABAD2f9VwqPTpmt-mVtuvDq0Nl1vaQwcJE=",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"authorization": "",
"Referer": "https://www.zhihu.com/question/34078228",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.8",
"Cookie": ''
}
url = r'https://www.zhihu.com/api/v4/questions/34078228/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={offset}&limit=20&sort_by=default'

pattern = 'data-original=\\"(.*?)\\"'
re_pattern = re.compile(pattern,re.S)
def get_one_page(url):
    session = requests.session()
    session.headers = header
    page = session.get(url)
    page_json = json.loads(page.content)
    return page_json

def parse_json(j,f):
    if "data" in j.keys():
        data = j["data"]
        for contents in data:
            if "content" in contents.keys():
                content = contents["content"]
                get_image_url(f,content)

def get_image_url(f,xml):
    images = re.findall(re_pattern,xml)
    i = 1
    for image in  images:
        if i%2==0:
            write2txt(f, image)
        i = i+1

def write2txt(f,context):
    f.write(context)
    f.write('\n')

def main():
    f = open("menu.txt","a")
    flag = True
    offset = 3
    while flag:
        u = url.format(offset=offset)
        print u
        j = get_one_page(u)
        if j["paging"]["is_end"] == True:
            break
        parse_json(j, f)
        offset = offset + 20
    f.close()
if __name__ =="__main__":
    main()
