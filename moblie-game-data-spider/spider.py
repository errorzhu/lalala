# coding: utf-8

import requests
from bs4 import BeautifulSoup
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

tags = []
details = []
tag_url = r'https://www.taptap.com/ajax/tag/hot-list?page=10'
index_url = r'https://www.taptap.com/categories'
url = r'https://www.taptap.com/app/61620'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36", \
    "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}


def get_all_tags():
    tags = []
    html = open('jshtml.html', 'r')
    soup = BeautifulSoup(html.read(), "lxml")
    divs = soup.find_all('div', class_="section-title")
    for div in divs:
        tags.append(div.find('a')['href'])
    html.close()
    return tags


def get_one_tag_list(url):
    items = []
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "lxml")
    for item in soup.find_all('a', class_='app-card-left'):
        items.append(item['href'])
    return items


def get_item_detail(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "lxml")

    name = soup.find('h1', itemprop="name").get_text()

    company = soup.find('span', itemprop="name").get_text()

    download_times = ''
    if soup.find('span', class_="text-download-times") is not None:
        download_times = soup.find('span', class_="text-download-times").get_text()

    rank_value = ''
    if soup.find('span', itemprop="ratingValue") is not None:
        rank_value = soup.find('span', itemprop="ratingValue").get_text()

    size = soup.find('span', class_="info-item-content").get_text()

    last_update = soup.find('span', itemprop="datePublished", class_="info-item-content").get_text()

    remark_num = soup.find('small').get_text()

    tag_all = ''
    temp_tag = []
    tags = soup.find(id='appTag').find_all('li')
    for tag in tags:
        if tag.find('a') is not None:
            tag_text = tag.find('a').get_text().strip()
            temp_tag.append(tag_text)
    tag_all = ','.join(temp_tag)

    item_info = [name, company, download_times, rank_value, size, last_update, remark_num, tag_all]
    return item_info


def write2csv(datas):
    with open('result.csv', 'w') as f:
        writer = csv.writer(f)
        for row in datas:
            writer.writerow(row)


def main():
    tags = get_all_tags()
    for tag in tags:
        items = get_one_tag_list(tag)
        for item in items:
            detail = get_item_detail(item)
            print detail
            details.append(detail)
            write2csv(details)


if __name__ == "__main__":
    main()
