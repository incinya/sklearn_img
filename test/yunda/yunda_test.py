from unittest import TestCase

from PIL import Image

from img_main import YundaCode


class YundaTest(TestCase):
    def setUp(self):
        self.y = YundaCode()

    def test_bds(self):
        image = Image.open('002.png')
        res = self.y.main(image)

