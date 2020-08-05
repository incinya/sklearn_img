import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

url = "http://jw.sdufe.edu.cn/"
# 1、打开浏览器，最大化浏览器
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

# 用户名元素
# userElement = driver.find_element(By.XPATH, "//*[@id='user']/input")
# 密码元素
# passElement = driver.find_element(By.XPATH, '//*[@id="pwd"]/input')
# 验证码输入框元素
codeElement = driver.find_element(By.XPATH, '//*[@id="RANDOMCODE"]')

# 验证图片元素
imgElement2 = driver.find_element(By.XPATH, '//*[@id="SafeCodeImg"]').click()
imgElement = driver.find_element(By.XPATH, '//*[@id="SafeCodeImg"]')
# 2、截取屏幕内容，保存到本地
# driver.save_screenshot("01.png")

# 3、打开截图，获取验证码位置，截取保存验证码
ran = Image.open("01.png")
location = imgElement.location  # 获取验证码x,y轴坐标
print(location)
size = imgElement.size  # 获取验证码的长宽
print(size)
box = (1338, 453, 1338+80, 453+40)  # 获取验证码位置代表（左，上，右，下）
ran.crop(box).save("02.png")

# 4、获取验证码图片，读取验证码
imageCode = Image.open("02.png")  # 图像增强，二值化
# imageCode.load()
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("03.png")
sharp_img.load()  # 对比度增强
time.sleep(2)
print(sharp_img)
code = pytesseract.image_to_string(sharp_img).strip()
# 5、收到验证码，进行输入验证
print(code)
#
# userElement.send_keys('user')
# passElement.send_keys('password')

time.sleep(1)
codeElement.send_keys(code)
# click_login = driver.find_element(By.XPATH, "//*[@id='submit']")
# click_login.click()