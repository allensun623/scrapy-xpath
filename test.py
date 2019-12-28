# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import random
from fake_useragent import UserAgent
import json
import pysnooper
from proxy import proxy_list
import random
import time
"""get the information from douban top 250"""


def run_spider(): 
    url_detail = "https://twitter.com/search?q=nba&src=typed_query"
    product_li_xpath = "//body/div[@id='doc']"
    product_item1_xpath = "//div[@id='page-container']"
    product_item2_xpath = "//p[@class='TweetTextSize  js-tweet-text tweet-text']/text()"
    product_item3_xpath = "//strong[@class='fullname show-popup-with-id u-textTruncate ']/text()"
    product_item4_xpath = "//ol[@class='stream-items js-navigable-stream']/li"
    i = 0 
    list_success = []
    while i < 20:
        i += 1
        #html_choice = random.choice([True, False])
        #if html_choice:
        #    html_etree = html_request_cookie(url_detail)            
        #else:
        html_etree = html_request(url_detail)
        li = html_etree.xpath(product_li_xpath) 
        item1 = html_etree.xpath(product_item1_xpath)
        item2 = html_etree.xpath(product_item2_xpath)
        item3 = html_etree.xpath(product_item3_xpath)
        item4 = html_etree.xpath(product_item4_xpath)
        #print(html_choice)
        print(li)
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        print("Attempted %i: " % i)
        if len(li)!=0: 
            list_success.append("Succeeded at %i !" % i) 
        #delay = random.randint(3, 10)
        #print("Scrapy dealy %i seconds"%delay)
        #time.sleep(delay)
    print(list_success)
    print("Success times: %i" % len(list_success))

def html_request(url_detail):
    #return html request header
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    proxies = proxy_list.get_proxy()
    response = requests.get(url_detail, 
                            headers=HEADERS, 
                            proxies=proxies)
    print(response)
    html_etree = etree.HTML(response.content)
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
                'Referer': 'www.zhihu.com',
                'Host': 'www.zhihu.com'}
    proxies = proxy_list.get_proxy()
    response = requests.get(url_detail, 
                            cookies=cookie, 
                            headers=HEADERS, 
                            proxies=proxies)
    html_etree = etree.HTML(response.content)
    return html_etree

def main():
    run_spider()

if __name__ == "__main__":
    main()

