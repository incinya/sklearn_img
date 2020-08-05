import basic_handle as bh
from PIL import Image
import train


def main(filename):
    PATH = filename
    image = Image.open(PATH)
    image = image.convert('L')
    bh.twoValue(image, 125)
    bh.clearNoise(image, 3, 1)
    path1 = 'identify/' + 'tgt.png'
    bh.saveImage(path1, image.size)
    image = Image.open(path1)
    image = image.resize((80, 30))
    image.save(path1)


def crop_img():
    path = "identify/tgt.png"
    img = Image.open(path)
    w, h = img.size
    box = (7, 0, w - 15, h)
    img.crop(box).save("identify/basic.png")


def smartSliceImg(img, outDir, count=4, p_w=3):
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
        img.crop(box).save(outDir + str(i) + ".png")
        beforeX = nextX


def run(filename):
    main(filename)
    crop_img()
    img = Image.open('identify/basic.png')
    smartSliceImg(img, 'identify/strip/')
    res = train.check_everyone(train.knn, f'identify/strip/')
    return res

if __name__ == '__main__':
    run('img_test/imgs/96.png')