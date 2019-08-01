import os
import cv2
import numpy as np
import glob

l = glob.glob('./sr/*.png')
l=sorted(l) #,key=lambda x: int(x[4:-4])

img0_l = glob.glob('/media/dong/data1/Ning_Shaochun/数优数据_合并_128/碗杯侧面破损_顶部破损_S_R/test_label/*.png')
img0_l = sorted(img0_l)

img1_l = glob.glob('/media/dong/data1/Ning_Shaochun/数优数据_合并_128/碗杯侧面破损_顶部破损_S_R/test_img/*.jpg')
img1_l = sorted(img1_l)


for i in range(len(l)):
    img0 = cv2.imread(img0_l[i])
    img1 = cv2.imread(img1_l[i])
    img2 = cv2.imread(l[i])
    if not os.path.exists('./sr/concate/'):
        os.makedirs('./sr/concate/')
    cv2.imwrite('./sr/concate/' + img1_l[i].split('/')[-1],np.hstack((img0,img1,img2)))

