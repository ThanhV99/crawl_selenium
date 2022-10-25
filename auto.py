from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import re

def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

def phanloai(qua, noidung):
    for i in noidung:
        if len(i) == 13:
            return [qua[noidung.index(i)], i]
    return [0, 0]


ser = Service("D:/bai tap python/webtudong/chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.get("https://haitacdaichien.vn/su-kien/oan-tu-xi")
driver.implicitly_wait(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/p/span/i").click()

driver.find_element(By.ID, "UserName").send_keys("coderqueen9")
driver.find_element(By.ID, "Password").send_keys("gunny476")
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/form/div[1]/button").click()
time.sleep(2)

f = open("codequeen.txt", "w")
for i in range(20, 34):
    print(i)
    select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div/select'))
    select.select_by_value(str(i))
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/div/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]").click()
    them_luot = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/button[2]")
    driver.execute_script("arguments[0].click();", them_luot)
    time.sleep(1)

    #them luot
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[5]/div[2]/div[3]/div[1]/div[2]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]").click()
    time.sleep(1)
    #chia se
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[5]/div[2]/div[3]/div[2]/div[2]/div").click()

    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    time.sleep(1)
    driver.close()
    driver.switch_to.window(parent)

    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]").click()

    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[5]/div[2]/div[1]").click()
    time.sleep(1)
    #dot phao
    for i in range(3):
        time.sleep(random.randint(0,2))
        click = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div")
        driver.execute_script("arguments[0].click();", click)
        time.sleep(0.5)
        x = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/button")
        driver.execute_script("arguments[0].click();", x)
        time.sleep(6)
        x = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/button")
        driver.execute_script("arguments[0].click();", x)
        time.sleep(0.5)

    time.sleep(2)
    #lich su
    noidung = []
    qua = []
    lich_su = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/button[1]")
    driver.execute_script("arguments[0].click();", lich_su)

    time.sleep(random.randint(0,2))
    noidung.append(driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/div/div[1]/table/tbody/tr[1]/td[4]").text)
    noidung.append(driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/div/div[1]/table/tbody/tr[2]/td[4]").text)
    noidung.append(driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/div/div[1]/table/tbody/tr[3]/td[4]").text)

    qua.append(driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/div/div[1]/table/tbody/tr[1]/td[3]").text)
    qua.append(driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/div/div[1]/table/tbody/tr[2]/td[3]").text)
    qua.append(driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/div/div[1]/table/tbody/tr[3]/td[3]").text)

    t1, t2 = phanloai(qua, noidung)

    if t1 != 0 and t2 != 0:
        t1 = no_accent_vietnamese(t1)
        f.write(str(t1))
        f.write(" ")
        f.write(str(t2))
        f.write("\n")

    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div/div/div/a").click()

    time.sleep(random.randint(1,3))
    #doi nhan vat

    doinhanvat = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/div[2]/div[2]/div[2]")
    driver.execute_script("arguments[0].click();", doinhanvat)

    time.sleep(random.randint(1,3))

f.close()
driver.quit()