from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import os

def rnd_char():
    """生成随机一个字符"""

    j = random.randint(1,3)
    if j == 1:
        # 随机个小写字母的十进制ASCII码
        an = random.randint(97, 122)
    if j == 2:
        # 随机个大写字母的十进制ASCII码
        an = random.randint(65, 90)
    if j ==3:
        # 随机个数字的十进制ASCII码
        an = random.randint(48, 57)

    return chr(an)

def rnd_color():
    """随机颜色"""
    return (random.randint(0,200), random.randint(30,255), random.randint(30,200))

def create_pic(width=240, height=60, fontsize=36, save_path = './test.jpeg'):

    image = Image.new('RGB', (width,height), (192,192,192))

    font  = ImageFont.truetype('./font/shouzhangti.ttf',fontsize)

    draw = ImageDraw.Draw(image)

    for x in range(0, width, random.randint(10,20)):
        for y in range(0, height, random.randint(5,10)):
            draw.point((x,y),fill=rnd_color())

    _str = ''
    for t in range(4):
        c = rnd_char()
        _str += c

        h = random.randint(1, height-40)
        w = width/4 * t + 10
        draw.text((w,h), c, font=font, fill=rnd_color())
    image.filter(ImageFilter.BLUR)
    image.save(save_path,'jpeg')
    print('---end---完成')
    return _str,save_path

if __name__ == '__main__':
    _str, save_path = create_pic(fontsize=40)
    print('%s--%s'%(_str,save_path))
    print(os.path.dirname(__file__))