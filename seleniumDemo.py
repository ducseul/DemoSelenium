#!/usr/bin/python
#!/usr/bin/env python

import sys
from sys import argv
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import string
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

email = "your email"
password = "your password"
projectName = "DemoSelenium"
description = "This repository is just for demo"
def automation():
    #this is how a function declare
    #for example, I will open fpt site and coding to do it.
    driver.get('https://github.com/') #open browser
    #there are a few method to select element in DOM using selenium: using xpath, class, id or querry all
    driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click() #click on Sign-in option
    driver.find_element_by_xpath("//*[@id='login_field']").send_keys(email) //
    driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click() #click on sign button
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN) #press keydown to scroll down
    driver.get('https://github.com/new') #directing new project to make a new repository
    driver.find_element_by_xpath("//*[@id='repository_name']").send_keys(projectName)
    driver.find_element_by_xpath("//*[@id='repository_description']").send_keys(description)
    driver.find_element_by_xpath("//*[@id='repository_auto_init']").click() #tick on "Initialize this repository with a README"
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN) #press keydown to scroll down
    driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button").click() #click confirm

    
if __name__ == '__main__':
    #this is main function
    from subprocess import call
    driver = webdriver.Chrome(ChromeDriverManager().install())
    automation()
    pass
