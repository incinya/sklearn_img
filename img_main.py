from PIL import Image

from conf import *
from img_format import ImgHandler
from model import AIModel


class YundaCode:
    def __init__(self):
        self.i = ImgHandler()
        self.m = AIModel()

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
    y = YundaCode()
    image = Image.open('30.png')
    y.main(image)
