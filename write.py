import cv2,glob

fps = 24   #视频帧率
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')  
videoWriter = cv2.VideoWriter('./random.avi', fourcc, fps, (720,480))   #(1360,480)为视频大小

l=glob.glob('./Untitled Folder/*.png')
l.sort()

for i in l:

    img12 = cv2.imread(i)
    assert img12 is not None
#    cv2.imshow('img', img12)
#    cv2.waitKey(1000/int(fps))
    videoWriter.write(img12)
videoWriter.release()

