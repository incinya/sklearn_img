"""
测试图片边缘位置负索引
"""
from PIL import Image, ImageDraw
import numpy as np

G = 150
t2val = {}

# 生成图片'9999.jpg'
def generate_img():
    img = Image.new('1', (50, 50))
    draw = ImageDraw.Draw(img)
    draw.point((25, 25), 255)
    draw.point((24, 25), 255)
    draw.point((25, 24), 255)
    draw.point((24, 24), 255)

    draw.point((-1, -1), 255)
    # 通过测试,负索引不能识别位置,但也不报错


    # 二值化处理
    for y in range(0, img.size[1]):
        for x in range(0, img.size[0]):
            g = img.getpixel((x, y))
            if g > G:
                t2val[(x, y)] = 1
            else:
                t2val[(x, y)] = 0

    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            draw.point((x, y), t2val[(x,y)])
    img.save('9999.jpg')

# 打印图片二值化数据
def prt_img_ary():
    img = Image.open('9999.jpg')
    img_ary = np.asarray(img)

    print(img_ary)
    # 可以从'结果矩阵'图像中看出,图片没有按照给定值变化
    # todo 优化成纯黑白图片

generate_img()