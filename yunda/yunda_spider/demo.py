from PIL import Image
from model.img_main import YundaCode

image = Image.open('002.png')
res = YundaCode().main(image)
print('识别结果为')
print(res)
