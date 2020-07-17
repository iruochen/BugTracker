# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> 画图
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/3 17:44
@Desc   ：
=================================================='''
from PIL import Image, ImageDraw

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))

# 在图片查看器中查看
# img.show()

draw = ImageDraw.Draw(img, mode='RGB')

# 第一个参数：表示起始坐标
# 第二个参数：表示写入内容
# 第三个参数：表示颜色
draw.text([0, 0], 'python', "red")

# 保存到本地
with open('../code.png', 'wb') as f:
    img.save(f, format='png')
