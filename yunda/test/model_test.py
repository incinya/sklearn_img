from unittest import TestCase

from model.img_main import *
from model.model import SkModel


class ModelTest(TestCase):
    def setUp(self) -> None:
        self.m = SkModel()

    def test_model(self):
        x, y = self.m.modeling_imgs(in_path='../ops', size=SIZE_OP)
        self.m.save_mode(x, y, 'ops.model')

    def test_predict(self):
        model = self.m.load_model('../num1.model')
        img = Image.open('../30.png')
        img_ary = self.m.img_to_1d_ary(img, SIZE_1)
        res = model.predict([img_ary])
        print(res)

