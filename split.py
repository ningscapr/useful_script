import cv2
import os


img_list=os.listdir('data/')
img_list = ['data/' + ele for ele in img_list]


for i in img_list:
    img=cv2.imread(i)
    b,g,r=cv2.split(img)
    cv2.imwrite('BLUE/' + i.split('/')[-1], b)
    cv2.imwrite('GREEN/' + i.split('/')[-1], g)
    cv2.imwrite('RED/' + i.split('/')[-1], r)
    print(i)

