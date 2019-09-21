# coding:utf-8

import time
import json
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

args = sys.argv
ipv4 = args[1]
login_password = args[2]
ssh_password = args[3]

# Initialize Web driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
time.sleep(4)

driver.get("https://secure.sakura.ad.jp/vps/#/login?method=ip")
driver.set_window_size(1200, 833)
time.sleep(4)
html = driver.page_source
print(html)
driver.find_element(By.ID, "ip-id").send_keys(ipv4)
time.sleep(2)
driver.find_element(By.ID, "ip-password").send_keys(login_password)
time.sleep(2)
print(html)
driver.find_element(By.CSS_SELECTOR, ".navbar-right:nth-child(1)").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, ".navbar-right .btn").click()
time.sleep(4)
driver.find_element(By.ID, "ember528").click()
time.sleep(4)
driver.find_element(By.ID, "vps-select-0").click()
time.sleep(4)
dropdown = driver.find_element(By.ID, "vps-select-0")
time.sleep(4)
dropdown.find_element(By.XPATH, "//option[. = 'CentOS7 x86_64']").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#ember1351 > .form-control").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#ember1351 > .form-control").send_keys(ssh_password)
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, ".layout_main").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#ember1352 > .form-control").send_keys(ssh_password)
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
time.sleep(4)
driver.find_element(By.ID, "ember637").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT, "ログアウト").click()
