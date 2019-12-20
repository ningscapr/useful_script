import cv2
import os
import numpy as np

img_list=os.listdir('BLUE/defect_bg/')
img_list = ['BLUE/defect_bg/' + ele for ele in img_list]


for i in img_list:
    img_b = cv2.imread(i, 0)
    img_g = cv2.imread('GREEN/' + i.split('/')[1] + '/' + i.split('/')[2], 0)
    img_r = cv2.imread('RED/' + i.split('/')[1] + '/' + i.split('/')[2], 0)
    
    img=cv2.merge([img_b, img_g, img_r])
    #img=np.zeros((img_b.shape[0], img_b.shape[1], 3))
    #img[:,:,0]=img_b
    #img[:,:,1]=img_g
    #img[:,:,2]=img_r
    
    cv2.imwrite('merge_m/' + i.split('/')[-1], img)
    print(i)
    
    
    
