from unittest import TestCase
import cv2
import numpy as np


class ImgXY(TestCase):
    @staticmethod
    def test_mario():
        """模板匹配"""
        img_rgb = cv2.imread('mario.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread('2.png', 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        print(len(loc))

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
            print('rectangle')

        cv2.imshow('result', img_rgb)
        cv2.waitKey(0)

    @staticmethod
    def test_rectangel():
        img = cv2.imread('mario.png')
        cv2.rectangle(img, (72, 82), (112, 92), (255, 255, 255), 1)
        cv2.imshow('res', img)
        cv2.waitKey(0)

    @staticmethod
    def test_gray():
        img = cv2.imread('mario.png')
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('res', img_gray)
        cv2.waitKey(0)

    @staticmethod
    def test_sift():
        import cv2

        imgname2 = '2.png'
        imgname1 = 'mario.png'

        sift = cv2.xfeatures2d.SIFT_create()

        # FLANN 参数设计
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        img1 = cv2.imread(imgname1)
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 灰度处理图像
        kp1, des1 = sift.detectAndCompute(gray1, None)  # des是描述子

        img2 = cv2.imread(imgname2)

        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        kp2, des2 = sift.detectAndCompute(gray2, None)

        matches = flann.knnMatch(des1, des2, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0. * n.distance:
                good.append([m])

        img5 = cv2.drawMatchesKnn(gray1, kp1, gray2, kp2, good, None, flags=2)
        cv2.imshow("FLANN", img5)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



