from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.remote import mobile

driver =  webdriver.Chrome("C:/chrome_webdriver/chromedriver")

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

signin = driver.find_element_by_link_text("Sign in")
signin.click()

time.sleep(2)


email = driver.find_element_by_id("username")
passwrd = driver.find_element_by_id("password")
signin_button = driver.find_element_by_css_selector(".login__form_action_container  button")

email.send_keys("#")
passwrd.send_keys("#")
signin_button.click()

time.sleep(2)

remember_button = driver.find_element_by_css_selector("#remember-me-prompt__form-primary button")
remember_button.click()

time.sleep(10)

hide_side_messaging = driver.find_elements_by_css_selector(".msg-overlay-bubble-header__controls button")
hide_side_messaging[2].click()

time.sleep(2)
job_search_list = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in job_search_list:
    job.click()
    time.sleep(2)
    try: 
        save_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        save_button.click()
        time.sleep(2)

        #phone entry in application
        mobile_entry = driver.find_element_by_class_name("fb-single-line-text__input")
        if mobile_entry.text == ' ':
            mobile_entry.send_keys("5")

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    
        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.

    except NoSuchElementException:
        print("No application button, skipped.")
        continue


driver.close()    

