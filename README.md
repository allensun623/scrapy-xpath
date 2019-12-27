# scrapy-xpath
Scrapy data from related webs


#### requirements install

```
pip3 install -r requirements.txt
```

### Install Redis

Start Redis under its path, ex.`/usr/local/binredis-3.2.9`

> src/redis-server redis.conf

### setup proxypool

```
cd proxy/proxypool
```

in the folder of `proxypool`, change file `settings.py` 

setup the `PASSWORD` which is Redis password; if no password, change to `None`


#### run proxy and API

```
python3 run.py
```

## in the file `proxy_list.py`
Get the ip and random list or from redis.
