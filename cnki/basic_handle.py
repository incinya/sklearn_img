"""
验证码二值化和降噪
"""
import sys, os
from PIL import Image, ImageDraw

# 二值数组
t2val = {}


def twoValue(image, G):
    """
        原理设定一个阈值G,当图片转为灰度图后,如果该点的灰度值小于阈值则为白色,大于阈值则为黑色
    """
    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            g = image.getpixel((x, y))
            if g > G:
                t2val[(x, y)] = 1
            else:
                t2val[(x, y)] = 0


def clearNoise(image, N, Z):
    """
        降噪原理:该点周围噪点数
    """
    for i in range(0, Z):
        t2val[(0, 0)] = 1
        t2val[(image.size[0] - 1, image.size[1] - 1)] = 1

        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                nearDots = 0
                L = t2val[(x, y)]
                if L == t2val[(x - 1, y - 1)]:
                    nearDots += 1
                if L == t2val[(x - 1, y)]:
                    nearDots += 1
                if L == t2val[(x - 1, y + 1)]:
                    nearDots += 1
                if L == t2val[(x, y - 1)]:
                    nearDots += 1
                if L == t2val[(x, y + 1)]:
                    nearDots += 1
                if L == t2val[(x + 1, y - 1)]:
                    nearDots += 1
                if L == t2val[(x + 1, y)]:
                    nearDots += 1
                if L == t2val[(x + 1, y + 1)]:
                    nearDots += 1

                if nearDots < N:
                    t2val[(x, y)] = 1


def crop_image(img, box, dirs):
    img.crop(box).save(dirs + str(i) + ".png")


def saveImage(filename, size):
    image = Image.new("1", size)
    draw = ImageDraw.Draw(image)

    for x in range(0, size[0]):
        for y in range(0, size[1]):
            draw.point((x, y), t2val[(x, y)])

    image.save(filename)

if __name__ == '__main__':

    for i in range(1, 101):
        path = "striped_imgs/" + str(i) + ".png"
        image = Image.open(path)
        image = image.convert('L')
        twoValue(image, 125)
        clearNoise(image, 3, 1)
        path1 = "striped_imgs" + str(i) + ".jpg"
        saveImage('2value/' + path1, image.size)

# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# 例如当N=3时,只要该点周围有3个点以上的RGB值与该点相同,则判断该点不是噪点
# G: Integer 图像二值化阀值  0<G<255
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败