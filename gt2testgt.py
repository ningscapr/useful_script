import shutil
import os


l=os.listdir('./test_img')

for ll in l:
    name = './gt/' + ll[:-4] + '.png' 
    shutil.move(name, './test_gt/' + ll[:-4] + '.png')
    print(ll[:-4])




