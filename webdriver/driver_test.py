from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.gate.io/articlelist/ann')
print(browser.current_url)
aElements = browser.find_elements_by_tag_name("a")
adv_elements = browser.find_element_by_xpath("//div[@class='newsplink']/a[3]")
adv_elements.click()
print(browser.current_url)
#closh browser
browser.close()
#quit chreomedriver
browser.quit()
