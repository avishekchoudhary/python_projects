from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\chrome_webdriver\chromedriver")

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes


boosters = driver.find_elements_by_css_selector("#store div")
items = [item.get_attribute("id") for item in boosters]

while True:
    cookie.click()
    if(time.time()>timeout):
        price = driver.find_elements_by_css_selector("#store  b")
        perks_cost = []
        for i in range(len(price)-1):
            text = price[i].text
            cost = text.split(" - ")[1]
            cost = ''.join([cost[i] for i in range(len(cost)) if cost[i] != ","])
            perks_cost.append(int(cost))
            
        money = driver.find_element_by_id("money")
        money = (money.text)
        money = int(''.join([money[i] for i in range(len(money)) if money[i] != ","]))
        
        affordable_boost = {}
        for perk_cost in perks_cost:
            if money > perk_cost:
                ind = perks_cost.index(perk_cost)
                affordable_boost[perk_cost] = items[ind]       

        highest_price_affordable_upgrade = max(affordable_boost)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_boost[highest_price_affordable_upgrade]
        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5

    if(time.time() > five_min):
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break




    

