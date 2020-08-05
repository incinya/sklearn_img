import joblib
import numpy as np
import os
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier


def load_dataset():
    X = []
    y = []
    for i in "0123456789":
        target_path = "fenlei/resize/new/" + i

        if not os.path.exists(target_path):
            os.makedirs(target_path)
        for title in os.listdir(target_path):
            pix = np.asarray(Image.open(os.path.join(target_path, title)).convert('L'))

            X.append(pix.reshape(15 * 30))  # 二维降为一维
            y.append(target_path.split('/')[-1])

    X = np.asarray(X)
    y = np.asarray(y)
    return X, y


def check_everyone(model, part_path):
    pre_list = []
    y_list = []
    if not os.path.exists(part_path):
        os.makedirs(part_path)
    for title in sorted(os.listdir(part_path)):
        pix = np.asarray(Image.open(os.path.join(part_path, title)).convert('L').resize((15, 30)))
        pix = pix.reshape(15 * 30)
        pre_list.append(pix)
        y_list.append(part_path.split('/')[-1])
    pre_list = np.asarray(pre_list)
    y_list = np.asarray(y_list)

    result_list = model.predict(pre_list)
    acc = 0
    for i in result_list == y_list:

        if i == np.bool(True):
            acc += 1
    print(result_list)

    return result_list


X, y = load_dataset()
knn = KNeighborsClassifier()
knn.fit(X, y)
joblib.dump(knn, 'cnki.model')

if __name__ == '__main__':
    for i in "0123456789":
        try:
            check_everyone(knn, part_path="part/" + i + '/')
        except:
            pass