import os

img=os.listdir('./img/')
test_img=os.listdir('./test_img/')


for t in test_img:
    if t in img:
        print(t)
