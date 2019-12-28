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
    top_url = "https://twitter.com/search?q=nba&src=typed_query"
    #xpath
    xpath_dic = {
        "list_xpath": "//ol[@class='stream-items js-navigable-stream']/li",
        "page_xpath": "//div[@class='paging col-xs-12']/ul[@class='text-center']/li[@class='forward']/a/i[@class='co-arrow-right']/@href",
        "items_title_xpath": "//strong[@class='fullname show-popup-with-id u-textTruncate ']/text()",
        "items_content_xpath": "//div[@class='content']/div[@class='js-tweet-text-container']/p[@class='TweetTextSize  js-tweet-text tweet-text']/text()",
        "items_like_xpath": "//div[@class='css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr']//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-1n0xq6e r-bcqeeo r-d3hbe1 r-1wgg2b2 r-axxi2z r-qvutc0']/span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']/text()",
    }
    #info output form match item numbers in xpath
    item_output = {
            "title": "",
            "content": "",
            "likes": "",
            }
    return top_url, xpath_dic, item_output

def run_spider():
    top_url, xpath_dic, item_output = input_xpath()
    lixpath = [value for value in xpath_dic.values()]
    url_detail = top_url 
    count = 0
    data = []
    parse(data, count, url_detail, lixpath, item_output)

def parse(data, count, url_detail, lixpath, item_output):    
    html_etree = html_request(url_detail)
    product_li_xpath = lixpath[0]
    li = html_etree.xpath(product_li_xpath)
    items_xpath = lixpath[2:]
    items_value_lists = []
    #run unitl return value
    while True:
        html_etree = html_request(url_detail)
        for item_xpath in items_xpath:
            item_value_list = html_etree.xpath(item_xpath)
            if (len(item_value_list)) != 0:
                items_value_lists.append(item_value_list)
        if len(items_value_lists) != 0:
            break
    #iterate list      
    for j in range(len(items_value_lists[0])):
        item_output_dic = item_output.copy()
        for i, item_key in zip(range(len(items_value_lists)), item_output_dic):
            item_value = items_value_lists[i][j].strip()
            item_dic = {item_key: item_value}       
            item_output_dic.update(item_dic)
        print(item_output_dic)
        data.append(item_output_dic) 
    print(len(items_value_lists[0]))
    with open('twitter_nba.json', 'w') as outfile:
        #indent=4: indent item; ensure_ascii=False: not encode charactors
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    
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

