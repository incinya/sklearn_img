import os
import unittest
from PIL import Image
from model.img_format import ImgHandler


class ImgTest(unittest.TestCase):
    def setUp(self) -> None:
        self.i = ImgHandler()
        self.path = 'yunda_sample'
        self.val2_path = '2val'
        self.num2_path = 'num2'
        self.operator_path = 'ops'

    def test_two_value(self):
        imgs_path = [os.path.join(self.path, item) for item in os.listdir(self.path)]
        for path in imgs_path:
            img = Image.open(path)
            output = self.val2_path + '/' + str(path.split('\\')[-1])
            self.i.two_value(img).save(output)

    def test_crop(self, out_path='num2', in_path='2val'):
        imgs_path = [os.path.join(in_path, item) for item in os.listdir(in_path)]
        for path in imgs_path:
            img = Image.open(path)
            out_put = out_path + '/' + str(path.split('\\')[-1])
            self.i.crop(img).save(out_put)
