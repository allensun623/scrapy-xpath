# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import random
from fake_useragent import UserAgent
import json
import pysnooper
import time
from proxy import proxy_list

"""get the information from douban top 250"""

def input_xpath():
    "input attributes"
    #scrapy path
    top_url = "https://www.costco.com/CatalogSearch?dept=All&keyword=chairs"
    #xpath
    xpath_dic = {
        "list_xpath": "//div[@class='col-xs-6 col-md-6 col-lg-4 col-xl-3 product']",
        "page_xpath": "//div[@class='paging col-xs-12']/ul[@class='text-center']/li[@class='forward']/a/i[@class='co-arrow-right']/@href",
        "items_title_xpath": "/div[@class='product-tile-set']/div[@class='thumbnail']/div[@class='caption link-behavior']/div[@class='caption']/p[@class='description']/a/text()",
        "items_price_xpath": "/div[@class='product-tile-set']/div[@class='thumbnail']/div[@class='caption link-behavior']/div[@class='caption']/div[1]/div[@id='price-100507881']/text()",
    }
    #info output form match item numbers in xpath
    item_output = {
            "title": "",
            "price": "",
            }
    return top_url, xpath_dic, item_output

def product():
    top_url, xpath_dic, item_output = input_xpath()
    lixpath = [value for value in xpath_dic.values()]
    url_detail = top_url 
    count = 0
    data = []
    parse(data, count, url_detail, lixpath, item_output)

@pysnooper.snoop()
def parse(data, count, url_detail, lixpath, item_output):    
    html_etree = html_request(url_detail)
    product_li_xpath = lixpath[0]
    li = html_etree.xpath(product_li_xpath) 
    #print move + actors   
    for list_num in range(len(li)):
        count += 1
        item_output_dic = item_output.copy()
        #iterate xpath in lixpath and items in movie
        for i_xpath, item_key in zip(lixpath[2:], item_output_dic):
            item_xpath = product_li_xpath + \
                        "[%i]"%(list_num+1) + \
                        i_xpath
            item_value = html_etree.xpath(item_xpath)[0].strip() 
            item_dic = {item_key: item_value}       
            item_output_dic.update(item_dic)
        print(item_output_dic)
        data.append(item_output_dic) 

    with open('github-scrapy.json', 'w') as outfile:
        #indent=4: indent item; ensure_ascii=False: not encode charactors
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    
    #next page
    product_page_xpath = lixpath[1]
    nextpage = html_etree.xpath(product_page_xpath)  
    if nextpage: 
        url_detail = nextpage
        delay = random.randint(3, 10)
        print("scrapy delay %i seconds"%delay)
        time.sleep(delay)
        parse(data, count, url_detail, lixpath, item_output)

@pysnooper.snoop()
def html_request(url_detail):
    #return html request header, some web would ban coocikes
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    proxies = proxy_list.get_random_ip()
    response = requests.get(url_detail, headers=HEADERS, proxies=proxies)
    html_etree = etree.HTML(response.content.decode('utf-8'))
    return html_etree

def html_request_cookie(url_detail):
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
    proxies = proxy_list.get_random_ip()
    response = requests.get(url_detail, cookies=cookie, headers=HEADERS, proxies=proxies)
    html_etree = etree.HTML(response.content.decode('utf-8'))
    return html_etree

def main():
    product()

if __name__ == "__main__":
    main()

