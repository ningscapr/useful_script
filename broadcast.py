import cv2,glob

l_ran = glob.glob('./badminton_res/Untitled Folder/*.png')
l_sort = glob.glob('./badminton_res_sort/Untitled Folder/*.png')

l_ran.sort()
l_sort.sort()

assert len(l_ran)==len(l_sort)
for i in range(len(l_ran)):
    img_ran = cv2.imread(l_ran[i])
    cv2.imshow('random',img_ran)
    
    img_sort = cv2.imread(l_sort[i])
    cv2.imshow('sort',img_sort)
    
    cv2.waitKey(50)
    




