from unittest import TestCase

from PIL import Image

from model.img_main import YundaCode


class YundaTest(TestCase):

    def test_img_predict(self):
        img = Image.open('0.png')
        word = YundaCode().main(img)
        print(word)
