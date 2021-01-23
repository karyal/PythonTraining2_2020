# https://www.toptal.com/python/web-scraping-with-python?utm_campaign=Toptal%20Engineering%20Blog&utm_source=hs_email&utm_medium=email&utm_content=88285312&_hsenc=p2ANqtz-8b7vrFlEbC9k5Zdvxu4zKMv5kYi1MtcYKsin5k2OYc1dG0ZM1CaxQP0hOD-JYtEWXqzLjiLoswDo0GZMUGPwi32gNZ5A&_hsmi=88285312

import sys
# Load libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/info_/Downloads/Softwares/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
url = "https://kathmandupost.com/politics"
driver.get(url)
title_elements  = driver.find_elements_by_tag_id('block--morenews')
print(len(title_elements))
time.sleep(1000*5) # Let the user actually see something!
driver.quit()