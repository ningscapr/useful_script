import os
import cv2

file_list = ['点状_丝状杂物_M_N'] 

#'丝状杂物_N','表面气泡_Q','漏金线_G','点状杂物_M','碗杯溢胶_A','碗杯侧面破损_S','碗杯顶部破损_R','胶面_碗杯脏污_JK'
#'漏金线_G','点状_丝状杂物_M_N','碗杯侧面破损_顶部破损_S_R','碗杯溢胶_A','表面气泡_Q'
  
img_list = [f + '/img' for f in file_list]   ####/256*256_oversample_undersample

for img in img_list:
    name = os.listdir(img)
    for nnn in name:
        pre =  img + '/' + nnn
        suc =  img[:-3] + 'label/' + nnn[:-4] + '_label.png'
        image_h, image_w  = cv2.imread(pre).shape[0:2]
        label_h, label_w  = cv2.imread(suc,0).shape
        if image_h != 512 or image_w != 440:
            print('image:{}'.format(pre))
        if label_h != 512 or label_w != 440:
            print('label:{}'.format(suc))

print('done!')



