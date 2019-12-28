# scrapy-xpath
Scrapy data from related webs


#### requirements install

> pip3 install -r requirements.txt


### Install Redis

Start Redis under its path, ex.`/usr/local/binredis-3.2.9`

> src/redis-server redis.conf

### Setup proxypool

> cd proxy/proxypool

In the folder of `proxypool`, vim file `settings.py` 

setup the `PASSWORD` which is Redis password; if no password, leave it `None`


### Run proxy and API

> python3 proxy/run.py

#### Get the IP
In the file `proxy_list.py`
Get the ip and random list or from redis.

### PS
- get next page with `href`
    - `douban`, `amazon`, `github`

- get next page with `new url`
    - `costco`

- get next page with `driver for onclick()`
    - `gate`
        - install chrome driver in the folder `webdriver`
        - simulate js action