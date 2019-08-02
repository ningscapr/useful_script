import os
import cv2,shutil

l = os.listdir('./test_img/')
l=sorted(l)

des = os.listdir('./FgSegNet_v2/rail_test/')
des=sorted(des)

for ll in l:
    #name = os.path.split(ll)[-1]
    shutil.copy2('./FgSegNet_v2/rail_test/' + str(l.index(ll)+1) + '.png', './FgSegNet_v2/rename/' + ll[:-4] + '.png')
    shutil.copy2('./FgSegNet_v2/rail_test/' + str(l.index(ll)+1) + '_thresh.png', './FgSegNet_v2/rename/' + ll[:-4] + '_thresh.png')
