from urllib import request
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import pandas as pd

# 2、解析数据过程
def cip_parse_HTMLData(htmlstr):
    ''' 解析HTML数据, htmlstr参数是HTML字符串, 返回的解析之后的当前页数据列表 '''
    sp = BeautifulSoup(htmlstr, 'html.parser')
    cip_list=sp.select('#list > li')
    page_list = []

    for item in cip_list:
        row_list=[]
        classCode=item.select('li > span')
        classCode=(classCode[0].text).strip()
        row_list.append(classCode)
        ClassName=item.select('li > a')
        ClassName=(ClassName[0].text).strip()
        row_list.append(ClassName)
        page_list.append(row_list)
    return page_list

# CIP数据
url_temp = "http://www.ztflh.com/?c={}"
#极致反扒，随机访问页面，
# nlist=list(range(1,45837))
# random.shuffle(nlist)
#
# 代理服务器 反反爬
proxyHost = "u3188.b5.t.16yun.cn"
proxyPort = "6460"

# 代理隧道验证信息
proxyUser = "16XLZWEK"
proxyPass = "673519"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

# 设置 http和https访问都是用HTTP代理
proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

# 1、数据爬取过程
def request_Data(url):
    ''' 爬取当前网页数据, 参数url是当前网页的地址, 返回当前页面数据列表 '''
    # 创建Request对象
    tunnel = random.randint(1, 10000) #通知代理随机ＩＰ
    handler = request.ProxyHandler(proxies=proxies)
    opener = request.build_opener(handler)
    ua = UserAgent()　#随机切换传送给服务器的Ｈｔｔｐ头部的客户端信息，防止单一的浏览器被封
    opener.addheaders=[('User-Agent', ua.random),('Proxy-Tunnel',str(tunnel))]
    request.install_opener(opener)
    # 数据列表
    page_data_list = []
    # print(opener.handlers)
    # request.
    with request.urlopen(url,timeout=10) as response:
        # 获得字节序列对象
        # print(req.headers)
        # print(request.`)
        print(response.geturl())
        data = response.read()
        # print(data)
        htmlstr = data.decode()
        L = cip_parse_HTMLData(htmlstr)
        page_data_list.extend(L)
    # return L
    return page_data_list


data_list = []
error_page=[]
for i in range(25000,29000): #nlist:#45837

    # i是当前页码
    url = url_temp.format(i)
    print(url)
    print("++++++++++++第{}页++++++++++++++".format(i))

    try:
        # 3、反反爬
        # 休眠5秒
        # x=random.randint(1,6)
        # print('休眠{}秒，反反爬'.format(x))
        # time.sleep(4)
        L = request_Data(url)
        # print(L)
        data_list.extend(L)
        print('正常处理{}页完成'.format(i))
        # print(data_list)
    except Exception as e:
        print(e)
        # 3、反反爬
        # 休眠10秒
        c= random.randint(10,15)
        time.sleep(c)
        try:
            L = request_Data(url)
            data_list.extend(L)
            continue
        except Exception as e1:
            print(e1)
            time.sleep(10)
            try:
                L = request_Data(url)
                data_list.extend(L)
                continue
            except Exception as e2:
                print(e2)
                time.sleep(10)
                try:
                    L = request_Data(url)
                    data_list.extend(L)
                    continue
                except Exception as e3:
                    error_page.append([i])
                    continue

print('data_list2 =', len(data_list))
print('爬取数据结束')

# 4、保存数据
# 列名
colsname = ['分类名', '分类名称']

df = pd.DataFrame(data_list, columns=colsname)
df.to_csv('CipClass.csv', index=False)
#

print(error_page)

print('保存数据结束')