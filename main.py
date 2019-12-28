from costco import costco_chairs
from douban import douban
from gate import gate_news
from zhihu import zhihu_hot
from twitter import twitter_nba
import timeit 

def main():
    #costco_chairs.product()
    #douban.run_spider()
    #gate_news.run_spider()
    #zhihu_hot.run_spider()

    '''cauculate runtime'''
    start = timeit.default_timer()
    #run

    twitter_nba.run_spider()
    stop = timeit.default_timer()
    time = stop - start
    print("================================================================")
    print('Runtime: ', time)  
    print("================================================================")

if __name__ == "__main__":
    main()