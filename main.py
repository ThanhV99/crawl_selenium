from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

ba_tieng_sau = ["wob_t wob_gs_l0", "wob_t wob_gs_l3", "wob_t wob_gs_l6", "wob_t wob_gs_l9", "wob_t wob_gs_l12", "wob_t wob_gs_l15", "wob_t wob_gs_l18", "wob_t wob_gs_l21"]
thoi_gian = []
trang_thai = []
nhiet_do = []
kha_nang_co_mua = []
do_am = []
toc_do_gio = []

def laydulieu():
    time_city = driver.find_element(By.ID, "wob_dts")
    thoigian = time_city.text
    trangthai = driver.find_element(By.ID, "wob_dcp")
    trangthai = trangthai.text
    nhietdo = driver.find_element(By.ID, "wob_tm")
    nhietdo = nhietdo.text
    khanangcomua = driver.find_element(By.ID, "wob_pp")
    khanangcomua = khanangcomua.text
    doam = driver.find_element(By.ID, "wob_hm")
    doam = doam.text
    tocdogio = driver.find_element(By.ID, "wob_ws")
    tocdogio = tocdogio.text

    thoi_gian.append(thoigian)
    trang_thai.append(trangthai)
    nhiet_do.append(nhietdo)
    kha_nang_co_mua.append(khanangcomua)
    do_am.append(doam)
    toc_do_gio.append(tocdogio)

ser = Service("D:/bai tap python/webtudong/chromedriver.exe")

driver = webdriver.Chrome(service=ser)

driver.get("http://google.com")

# search
search = driver.find_element(By.NAME, "q")
time.sleep(random.randint(0,3))
search.send_keys("du bao thoi tiet")
search.send_keys(Keys.ENTER)
time.sleep(2)

name_city = driver.find_element(By.ID, "wob_loc")
ten = name_city.text
q = driver.find_element(By.CLASS_NAME, "wob_t wob_gs_l3")
q.click()

# for i in ba_tieng_sau:
#     time.sleep(random.randint(0,2))
#     laydulieu()
#     q = driver.find_element(By.CLASS_NAME, i)
#     q.click()
#
# print(ten)
# print("thoi gian: ", thoi_gian)
# print("trang thai: ", trang_thai)
# print("nhiet do: ", nhiet_do)
# print("do am: ", do_am)
# print("toc do gio: ", toc_do_gio)
# print("kha nang co mua: ", kha_nang_co_mua)
#
# time.sleep(random.randint(0,3))
#
# driver.quit()