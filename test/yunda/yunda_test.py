from unittest import TestCase

from PIL import Image

from img_main import Identifier


class YundaTest(TestCase):
    def setUp(self):
        self.y = Identifier()

    def test_bds(self):
        image = Image.open('002.png')
        res = self.y.main(image)

