import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class TtSpiser():
    def __init__(self):
        self.url = "https://www.ttkdex.com/"
        self.browser = webdriver.Chrome()
        # self.mouse = ActionChains(self.browser)

    def tt(self):
        self.browser.get(self.url)
        self.browser.find_element_by_link_text("运单查询").click()
        self.browser.find_element_by_xpath('//*[@id="orderTextInput"]').send_keys('TT9901053279163')

    def capture_code(self):
        self.browser.find_element_by_xpath('//*[@id="captcha_sncaptcha_button"]/img').click()
        time.sleep(10)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[2]/a').click()

    def parse(self):
        status = self.browser.find_element_by_xpath('//*[@id="detail"]/div[1]/span[2]').text.split("：")[-1]
        li_list = self.browser.find_elements_by_xpath('//*[@id="orderList"]/div')
        result = list()
        for li in li_list:
            print(li.text)
            print("*"*50)
            _time=li.find_element_by_xpath('./span[1]').text
            content=li.find_element_by_xpath('./span[2]').text
            result.append({
                "time": _time,
                "content": content,
                "status": status
            })
        # if self.browser.find_element_by_xpath('//*[@id="page"]/div/a[2]').click():
        #     print("order_number")
        print(result)
        return result

    def run(self):
        self.tt()
        time.sleep(2)
        self.capture_code()
        time.sleep(3)
        self.parse()


if __name__ == "__main__":
    spider = TtSpiser()
    spider.run()
