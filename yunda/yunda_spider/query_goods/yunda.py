import re
import requests
from PIL import Image

from model.img_main import YundaCode

from yunda_spider.query_goods.yunda_conf import *

session = requests.Session()


def get_g_s(order_number):
    data = {'wen': order_number}
    session.post(url, data=data)

    # todo 验证码图片已无法获取
    req = session.get(url=url3, headers=headers).content
    with open(filename, "wb") as f:
        f.write(req)

    img = Image.open(filename)
    word = YundaCode().main(img)
    # word = input("请输入验证码：")
    da = {"wen": order_number,
          "hx": "23",
          "lang": "C",
          "hh": "23",
          "yzm": word
          }
    ht = session.post(url=url2, headers=headers, data=da, allow_redirects=False).headers
    location_url = ht["location"]
    html = session.get(url=location_url, headers=headers).text
    re_str = '(var wyts = false.*?var tmp_pic="";)'
    res = re.findall(re_str, html, re.S)[0]
    return res


if __name__ == '__main__':
    bb = get_g_s(order_number="4602680000000")
    aa = 1
