import joblib
import numpy as np
import os
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier


class SklearnModel:
    @staticmethod
    def save_mode(x, y, model_name):
        knn = KNeighborsClassifier()

        knn.fit(x, y)
        joblib.dump(knn, model_name)

    @staticmethod
    def load_model(model_name):
        return joblib.load(model_name)

    @staticmethod
    def modeling_imgs(in_path, size):
        """
        :param in_path: 文件夹路径
        :param size: 图片大小
        :return: x,y
        """
        x = []
        y = []
        atoms = os.listdir(in_path)

        for index, atom in enumerate(atoms):
            value = atom
            for img_name in os.listdir(os.path.join(in_path, atom)):
                img = Image.open(os.path.join(in_path, atom, img_name))
                assert len(img.size) == 2, 'img_type err'
                img = img.resize(size)
                attr = np.asarray(img).reshape(size[0] * size[1])

                y.append(value)
                x.append(attr)

        x1 = np.asarray(x)
        y1 = np.asarray(y)
        return x1, y1

    @staticmethod
    def img_to_1d_ary(img, size: tuple):
        if not size:
            size = img.size
        img = img.resize(size)
        ary = np.asarray(img).reshape(size[0] * size[1])
        return ary


if __name__ == '__main__':
    size1 = (13, 30)
    a = SklearnModel()
    # x, y = a.modeling_imgs('origin', size1)
    # a.save_mode(x, y, 'origin.model')
    model = a.load_model('origin.model')
    img1 = Image.open('19_0.png')

    ary1 = a.img_to_1d_ary(img1, size1)
    aa = model.predict([ary1])
    bb = 1
