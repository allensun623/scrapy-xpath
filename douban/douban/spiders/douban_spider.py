# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import random
from fake_useragent import UserAgent
import json
import pysnooper
"""get the information from douban top 250"""

def __product():
    top_url = "https://movie.douban.com/top250"
    url_detail = "https://movie.douban.com/top250"
    #Because of anti-scrapy, running until get the information or up to 30x
    count = 0
    for i in range(1000):
        parse(count, top_url, url_detail)
        print("attempted: %i" % i)

def parse(count, top_url, url_detail):    
    html_etree = html_request(url_detail)
    product_li_xpath1 = "//div[@class='article']/ol[@class='grid_view']/li"
    li = html_etree.xpath(product_li_xpath1)    
    #print move + actors
    for list_num in range(len(li)):
        count += 1
        product_title_xpath = product_li_xpath1 + \
                        "[%i]"%(list_num+1) + \
                        "/div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title']/text()"
        title = html_etree.xpath(product_title_xpath)[0]
        product_name_xpath = product_li_xpath1 + \
                        "[%i]"%(list_num+1) + \
                        "/div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()"
        name = html_etree.xpath(product_name_xpath)[0].strip()
        print(str(count) + ": " +title + "\n" + name)
    #next page
    product_page_xpath = "//div[@class='paginator']/span[@class='next']/a/@href"
    nextpage = html_etree.xpath(product_page_xpath)
    if nextpage:
        parse(count, top_url, top_url + nextpage[0])


def html_request(url_detail):
    #return html request with cookie, header
    cookies = 'v=3; \
                iuuid=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                webp=true; \
                ci=1%2C%E5%8C%97%E4%BA%AC; \
                __guid=26581345.3954606544145667000.1530879049181.8303; \
                _lxsdk_cuid=1646f808301c8-0a4e19f5421593-5d4e211f-100200-1646f808302c8; \
                _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                monitor_count=1; \
                _lxsdk_s=16472ee89ec-de2-f91-ed0%7C%7C5; \
                __mta=189118996.1530879050545.1530936763555.1530937843742.18'
    cookie = {}
    for line in cookies.split(';'):
        name, value = cookies.strip().split('=', 1)
        cookie[name] = value
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    response = requests.get(url_detail, cookies=cookie, headers=HEADERS)
    html_etree = etree.HTML(response.content.decode('utf-8'))
    return html_etree

def main():
    __product()

if __name__ == "__main__":
    main()

