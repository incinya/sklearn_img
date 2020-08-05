"""
    1.裁剪图片
    2.切割原子级图片
"""
from PIL import Image


def smartSliceImg(img, outDir, ii, count=4, p_w=3):
    '''
    :param img:
    :param outDir:
    :param count: 图片中有多少个图片
    :param p_w: 对切割地方多少像素内进行判断
    :return:
    '''
    w, h = img.size
    pixdata = img.load()
    eachWidth = int(w / count)
    beforeX = 0
    for i in range(count):

        allBCount = []
        nextXOri = (i + 1) * eachWidth

        for x in range(nextXOri - p_w, nextXOri + p_w):
            if x >= w:
                x = w - 1
            if x < 0:
                x = 0
            b_count = 0
            for y in range(h):
                if pixdata[x, y] == 0:
                    b_count += 1
            allBCount.append({'x_pos': x, 'count': b_count})
        sort = sorted(allBCount, key=lambda e: e.get('count'))

        nextX = sort[0]['x_pos']
        box = (beforeX, 0, nextX, h)
        img.crop(box).save(outDir + str(ii) + "_" + str(i) + ".png")
        beforeX = nextX


def crop_img():
    for i in range(1, 101):
        path = "2value/striped_imgs" + str(i) + ".jpg"
        img = Image.open(path)
        w, h = img.size
        outDir = '2value/strip/'
        box = (7, 0, w - 15, h)
        img.crop(box).save(outDir + str(i) + ".png")


for i in range(1, 101):
    path = "2value/strip/" + str(i) + ".png"
    img = Image.open(path)
    outDir = '3qiege/'
    smartSliceImg(img, outDir, i, count=4, p_w=2)

crop_img()