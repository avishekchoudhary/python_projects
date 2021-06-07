from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time

driver = webdriver.Chrome("C:/chrome_webdriver/chromedriver")

driver.get("https://tinder.com/")

id1 = driver.find_element_by_tag_name('div')#id of tinder changes after 24 hrs so xpath will not work so fetching id before proceeding
id1 = str(id1.get_attribute('id'))
print(id1)
id2 = driver.find_elements_by_tag_name('div')
id2 = str(id2[-1].get_attribute('id'))
id3 = driver.find_elements_by_tag_name('div')
id3 = str(id3[-3].get_attribute('id'))
print(id3)

time.sleep(2)

log_in = driver.find_element_by_xpath(f'//*[@id="{id1}"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(5)

more_options = driver.find_element_by_xpath(f'//*[@id="{id2}"]/div/div/div[1]/div/div[3]/span/button')
more_options.click()

time.sleep(2)

fb_login = driver.find_element_by_xpath(f'//*[@id="{id2}"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]

driver.switch_to.window(fb_window)

email = driver.find_element_by_name("email")
passwd = driver.find_element_by_name("pass")

email.send_keys("souravkoundal45@gmail.com")
time.sleep(2)
passwd.send_keys("savechanges")

passwd.send_keys(Keys.RETURN)

driver.switch_to.window(base_window)

time.sleep(8)

#popups after login
cookies = driver.find_element_by_xpath(f'//*[@id="{id1}"]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(2)

location = driver.find_element_by_xpath(f'//*[@id="{id2}"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(2)
notifications = driver.find_element_by_xpath(f'//*[@id="{id2}"]/div/div/div/div/div[3]/button[2]')
notifications.click()
time.sleep(2)
no_thanks = driver.find_element_by_xpath(f'//*[@id="{id2}"]/div/div/div[1]/button')
no_thanks.click()

time.sleep(10)
#swiping/liking profile
for i in range(0,10):
    try:
        like_button = driver.find_element_by_xpath(f'//*[@id="{id1}"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()
        time.sleep(2)

    except NoSuchElementException:   
        no_thanks = driver.find_element_by_xpath(f'//*[@id="{id2}"]/div/div/button[2]')
        time.sleep(1)
        no_thanks.click()
        continue
    except ElementClickInterceptedException:   
        match_popup = driver.find_element_by_xpath(f'//*[@id="t237084395"]/div/div/div[1]/div/div[4]/button')
        time.sleep(1)
        match_popup.click()
        continue
   
        






time.sleep(20)
driver.close()