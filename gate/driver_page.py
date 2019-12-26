# -*- coding: utf-8 -*-
"""
return url of next page
add chromedriver in urs/local/bin
https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
or download chromedriver 
"""

from selenium import webdriver

def next_page(url, url_xpath):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get(url)
    adv_elements = browser.find_element_by_xpath(url_xpath)
    adv_elements.click()
    url_next_page = browser.current_url
    #closh browser
    browser.close()
    #quit chreomedriver
    browser.quit()
    return(url_next_page)

def main():
    #next_page('https://www.gate.io/articlelist/ann'):
    pass

if __name__ == "__main__":
    main()
