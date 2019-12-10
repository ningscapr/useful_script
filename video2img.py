import cv2

for name in ['output_b.avi','output_r.avi','output_g.avi']:
    vc = cv2.VideoCapture(name) #读入视频文件
    c=0
    rval=vc.isOpened()

    while rval:   #循环读取视频帧
        c = c + 1
        rval, frame = vc.read()
    #    if(c%timeF == 0): #每隔timeF帧进行存储操作
    #        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
        if rval:
            cv2.imwrite( name[:-4] + '/' + str(c) + '.png', frame) #存储为图像
            cv2.waitKey(1)
        else:
            break
    
    print(name)

