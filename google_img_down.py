from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("과속단속 카메라 사진")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
current_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    if scroll_height == current_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    current_height = scroll_height

results = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for result in results:
    try:
        result.click()
        time.sleep(3)
        # imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src") #240217 작동불능
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]').get_attribute("src")
        print(count, ':' , imgUrl)
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        print("failed")
        pass

driver.close()