import cv2
import numpy 
import os
l = os.listdir('./Untitled Folder/')

for i in l:
    label = cv2.imread('./Untitled Folder/'+i)
    if label.shape!= (512,440,3):
        label = label[4:516,1:441,:]
        cv2.imwrite('./Untitled Folder/'+i,label)
        print('./Untitled Folder/'+i,'done') 


