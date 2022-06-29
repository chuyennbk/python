#python -m pip install pillow
from statistics import mode
from PIL import Image,ImageFilter
import os
image1=Image.open('bang-dong-tu-bat-quy-tac.jpg')
#image1.show()
#image1.save('bang-dong-tu-bat-quy-tac.png')
# image1.convert()
image1.filter(ImageFilter.GaussianBlur(15)).save('blur.jpg')
def example1():
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i=Image.open(f)
            fn,fext=os.path.splitext(f)
            #print(fext)
            i.save('Picture_PNG/{}.png'.format(fn))
def example2():
    size_300=(300,300)
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i=Image.open(f)
            fn,fext=os.path.splitext(f)
            i.thumbnail(size_300)
            i.save('300/{}_300{}'.format(fn,fext))
if __name__ =="__main__":
    #example2()
    #image1.filter(ImageFilter.GaussianBlur(15)).save('blur.jpg')
    # image1.convert(mode='L').save('color.jpg')
    image1.rotate(90).save('rotate90.jpg')
