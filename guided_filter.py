import cv2
import numpy as np
import os

img_dir='label_dilate/'
img_list=os.listdir(img_dir)
img_list.sort(key=lambda x:x[0:5])

print(len(img_list))

for i in range(102):    
    guide=cv2.imread(img_dir+img_list[i],0)
    src=255-cv2.imread('result/' + str(i+1) +'.png',0)
    
    
    dst3 = cv2.ximgproc.guidedFilter(guide=guide, src=src, radius=3, eps=5, dDepth=-1)
    ret, dst3_thresh = cv2.threshold(dst3,127,255,cv2.THRESH_BINARY)
    
    cv2.imwrite('result_gf/' + str(i+1) + '.png', dst3)
    cv2.imwrite('result_gf/' + str(i+1) + '_thresh.png', dst3_thresh)
    
    
    #diff=np.sum((src-dst3_thresh)**2)
    #print(diff)




