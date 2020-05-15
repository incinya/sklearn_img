from PIL import Image
from img_format import ImgHandler
from model import SklearnModel


class Identifier:
    @staticmethod
    def main(img, model):
        img1_ary = model.img_to_1d_ary(img)
        a1 = str(model.predict([img1_ary])[0])
        return a1


if __name__ == '__main__':
    y = Identifier()
    i = ImgHandler()

    img1 = Image.open('test/yunda_sample/1.png')
    img1 = i.two_value(img1)
    img1 = i.crop(img1)

    model1 = SklearnModel.load_model('num1.model')

    y.main(img1, model1)
