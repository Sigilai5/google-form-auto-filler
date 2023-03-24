import time
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from variables import random_gender, random_before, random_method, random_importance,random_likely,challenge_list,benefits_list

# Malith lujok kulia
for i in range(0,2):

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.

    url = 'https://forms.gle/QyKr2hfQDkYT22aX7'

    driver.get(url)

    def fill_form(gender,before,method,importance,likely):
    
        radiobuttons = driver.find_elements_by_class_name("Od2TWd")
        checkboxes = driver.find_elements_by_class_name("uVccjd")

        time.sleep(1)
            

        for radio in radiobuttons:
            if radio.get_attribute("data-value").lower() == gender:
                radio.click()
            
            if radio.get_attribute("data-value").lower() == before:
                radio.click()

            if radio.get_attribute("data-value").lower() == method:
                radio.click()

            if radio.get_attribute("data-value").lower() == importance:
                radio.click()
            
            if radio.get_attribute("data-value").lower() == likely:
                radio.click()

        
        check = random.sample(challenge_list,k=4) # Select 4 random challenges
        for i in range(0,4):
            for checkbox in checkboxes:
                if checkbox.get_attribute("data-answer-value").lower() == check[i]:
                    checkbox.click()
        
    
    
        benefits = random.sample(benefits_list,k=4) # Select 4 random benefits
        for i in range(0,4):
            for checkbox in checkboxes:
                if checkbox.get_attribute("data-answer-value").lower() == benefits[i]:
                    checkbox.click()



        submit = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        
        submit.click()

        # close the browser and restart another session
        driver.close()
        driver.quit()
    
        


    fill_form(random_gender,random_before,random_method,random_importance,random_likely)
