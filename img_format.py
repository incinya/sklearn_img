from PIL import Image, ImageDraw


class ImgHandler:
    @staticmethod
    def two_value(img, t=120):
        """
            原理设定一个阈值t,当图片转为灰度图后,如果该点的灰度值小于阈值则为白色,大于阈值则为黑色
        """
        # 二值数组
        t2val = {}
        img = img.convert('L')
        for y in range(0, img.size[1]):
            for x in range(0, img.size[0]):
                g = img.getpixel((x, y))
                if g > t:
                    t2val[(x, y)] = 1
                else:
                    t2val[(x, y)] = 0

        img2 = Image.new("1", img.size)
        draw = ImageDraw.Draw(img2)
        for x in range(0, img2.size[0]):
            for y in range(0, img2.size[1]):
                draw.point((x, y), t2val[(x, y)])

        return img2

    @staticmethod
    def crop(img, box=None):
        """box : left,upper,right,lower"""
        return img.crop(box)


if __name__ == '__main__':
    i1 = ImgHandler()
    img1 = Image.open('0.png')
    img1 = i1.two_value(img1)
