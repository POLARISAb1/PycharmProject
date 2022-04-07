# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 定义配置的实例对象option
option = Options()
# 修改实例属性为 debug 模式启动的 ip + 端口
option.debugger_address = "localhost:9222"
# 实例化 driver 的时候，添加 option 配置
driver = webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/frame")
sleep(2)
driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
sleep(2)
driver.find_element_by_id("username").send_keys("yyl")


