"""重设原子图片大小"""
from PIL import Image
import os

for i in '0123456789':
    DIR = f'fenlei/resize/{i}/'
    file_list = os.listdir(DIR)

    for title in file_list:
        if not os.path.exists(f'fenlei/resize/new/{i}/'):
            os.makedirs(f'fenlei/resize/new/{i}/')
        img = Image.open(DIR+title)

        img = img.resize((15,30))
        img.save(f'fenlei/resize/new/{i}/'+title)