# -*- coding: utf-8 -*-
import random
import requests

def get_random_ip():
    ip_list = [
        "223.85.196.75:9797",
        "124.205.155.153:9090",
        "123.169.168.158:9999",
        "43.247.132.88:3129",
        "24.245.100.212:48678",
        "186.193.23.17:3128",
        "197.232.36.43:8080"
    ]
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def get_proxy():
    PROXY_POOL_URL = 'http://localhost:5555/random'
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            proxy_ip = 'http://' + response.text
            proxies = {'http': proxy_ip}
            return proxies
    except ConnectionError:
        return None

def main():
    get_random_ip()
    get_proxy()

if __name__ == "__main__":
    main()
