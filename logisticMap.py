from PIL import Image
import numpy as np




w = 2880
h = 1800
data = np.zeros((h,w,3),dtype = np.uint8)

for ru in range(0, w):
    r=(4*ru)/w
    x = 0.5
    for i in range(0,255):
        x=r*x*(1-x)
        data[round(x*h),ru] = [(ru/w)*255,(ru/w)*255,(ru/w)*255]
img = Image.fromarray(data, 'RGB')
img.save('my2.png')


