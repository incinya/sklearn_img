在main.py中设定cnki图片验证码路径并运行
模型需要重新训练,命名为cnki.model


basic_handle.py 是图片的二值化和降噪处理
core.py 是主程序,几乎包含所有处理过程
get_image.py是爬虫 使用 selenium完成
strip_image.py是图片的裁剪与切割
resize.py 是处理bug用的,重设原子级图片的大小,不然二位数组的大小不统一要报错
train.py 是生成训练模型并识别