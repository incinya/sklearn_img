from PIL import Image

from model.img_format import ImgHandler
from model.model import SkModel


class Identifier:
    @staticmethod
    def main(img, model):
        img1_ary = model.img_to_1d_ary(img)
        a1 = str(model.predict([img1_ary])[0])
        return a1


def get_size(box):
    return abs(box[2] - box[0]), abs(box[3] - box[1])


YUNDA_THRES = 200
BOX_1 = (0, 0, 13, 22)
BOX_2 = (21, 0, 31, 22)
BOX_OP = (13, 0, 21, 22)

SIZE_1 = get_size(BOX_1)
SIZE_2 = get_size(BOX_2)
SIZE_OP = get_size(BOX_OP)


class YundaCode:
    def __init__(self):
        self.i = ImgHandler()
        self.m = SkModel()

    def main(self, img):
        img = self.i.two_value(img, YUNDA_THRES)

        img1 = self.i.crop(img, BOX_1)
        model = self.m.load_model('num1.model')
        img1_ary = self.m.img_to_1d_ary(img1, SIZE_1)
        a1 = str(model.predict([img1_ary])[0])

        img2 = self.i.crop(img, BOX_2)
        model = self.m.load_model('num2.model')
        img2_ary = self.m.img_to_1d_ary(img2, SIZE_2)
        a2 = str(model.predict([img2_ary])[0])

        imgops = self.i.crop(img, BOX_OP)
        model = self.m.load_model('ops.model')
        imgops_ary = self.m.img_to_1d_ary(imgops, SIZE_OP)
        op = '+' if str(model.predict([imgops_ary])[0]) == 'jia' else '*'

        bds = eval(a1 + op + a2)
        return bds


if __name__ == '__main__':
    y = Identifier()
    i = ImgHandler()

    img1 = Image.open('test/yunda_sample/1.png')
    img1 = i.two_value(img1)
    img1 = i.crop(img1)

    model1 = SkModel.load_model('num1.model')

    y.main(img1, model1)
