from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("D:/bai tap python/webtudong/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--lang=en-ca")
driver = webdriver.Chrome(service=ser, options=options)
danh_sach = ["manchester united", "paris saint germain", "manchester city"]
info = []

for i in range(len(danh_sach)):
    driver.get("http://www.google.com")
    time.sleep(1)

    search = driver.find_element(By.NAME, "q")
    search.send_keys("information " + danh_sach[i])
    search.send_keys(Keys.RETURN)

    time.sleep(1)

    if i == 0:
        manager = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[2]')
        manager = manager.text.replace('\n', ' ')
        info.append(manager)
        arena = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[3]')
        arena = arena.text.replace('\n', ' ')
        info.append(arena)
        location = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[7]')
        location = location.text.replace('\n', ' ')
        info.append(location)
    elif i == 1:
        manager = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[2]')
        manager = manager.text.replace('\n', ' ')
        info.append(manager)
        arena = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[3]')
        arena = arena.text.replace('\n', ' ')
        info.append(arena)
        location = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[6]')
        location = location.text.replace('\n', ' ')
        info.append(location)
    elif i == 2:
        manager = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[2]')
        manager = manager.text.replace('\n', ' ')
        info.append(manager)
        arena = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[4]')
        arena = arena.text.replace('\n', ' ')
        info.append(arena)
        location = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[6]')
        location = location.text.replace('\n', ' ')
        info.append(location)


    player = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[2]/div[1]')
    player1 = player.text.replace('\n', ' ')
    info.append(player1)

    player = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[2]/div[2]')
    player2 = player.text.replace('\n',' ')
    info.append(player2)

    player = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[2]/div[3]')
    player3 = player.text.replace('\n', ' ')
    info.append(player3)

    info.append('\n')
    print(info)

driver.close()

with open('data_info.txt', 'w') as f:
    for i in info:
        if i == '\n':
            f.write(i)
        else:
            f.write(i)
            f.write('?')
    f.close()
