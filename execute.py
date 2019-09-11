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

args = sys.argv
ipv4 = args[1]
login_password = args[2]
ssh_password = args[3]

# Initialize Web driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

self.driver.get("https://secure.sakura.ad.jp/vps/#/login")
self.driver.set_window_size(1200, 833)
self.driver.find_element(By.ID, "ember500").click()
self.driver.find_element(By.ID, "ip-id").send_keys(ipv4)
self.driver.find_element(By.ID, "ip-password").send_keys(login_password)
self.driver.find_element(By.CSS_SELECTOR, ".navbar-right:nth-child(1)").click()
self.driver.find_element(By.CSS_SELECTOR, ".navbar-right .btn").click()
self.driver.find_element(By.ID, "ember919").click()
self.driver.find_element(By.ID, "vps-select-0").click()
dropdown = self.driver.find_element(By.ID, "vps-select-0")
dropdown.find_element(By.XPATH, "//option[. = 'CentOS7 x86_64']").click()
self.driver.find_element(By.CSS_SELECTOR, "#ember1351 > .form-control").click()
self.driver.find_element(By.CSS_SELECTOR, "#ember1351 > .form-control").send_keys(ssh_password)
self.driver.find_element(By.CSS_SELECTOR, ".layout_main").click()
self.driver.find_element(By.CSS_SELECTOR, "#ember1352 > .form-control").send_keys(ssh_password)
self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
self.driver.find_element(By.ID, "ember637").click()
self.driver.find_element(By.LINK_TEXT, "ログアウト").click()
