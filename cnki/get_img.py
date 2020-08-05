"""爬取cnki图片验证码"""
from PIL import Image
from selenium import webdriver
import time


def main():
    url = "https://login.cnki.net/login/?platform=kns&ForceReLogin=1&ReturnURL=%2f%2fwww.cnki.net%2f"

    browser = webdriver.Firefox()
    browser.get(url)

    for i in range(3):
        username = browser.find_element_by_xpath('//*[@id="TextBoxUserName"]')
        password = browser.find_element_by_xpath('//*[@id="TextBoxPwd"]')
        login = browser.find_element_by_xpath('//*[@id="Button1"]')

        username.send_keys('test')
        password.send_keys('test')
        login.click()
        time.sleep(1)
    browser.maximize_window()
    for i in range(1, 101):
        img = browser.find_element_by_xpath('/html/body/form/div[4]/div/div/div[7]/a')
        img.click()
        browser.save_screenshot('img_test/' + str(i) + '.png')


def strip():
    for i in range(1, 101):
        ran = Image.open(f"img_test/original/{i}.png")
        box = (1210, 334, 1210 + 80, 334 + 30)  # 获取验证码位置代表（左，上，右，下）
        ran.crop(box).save(f"img_test/imgs/{i}.png")


main()
strip()