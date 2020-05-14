import re
import requests
from PIL import Image

from img_main import YundaCode
from yunda_conf import *

session = requests.Session()


def get_g_s():
    session.post(url, data=data)

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
    bb = get_g_s()
    aa = 1
