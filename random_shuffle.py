import os,random

f = open('train_pair_sr.lst', 'r')
ff = f.readlines()
print(ff)
random.shuffle(ff)
f.close()

gg = open('train_pair_sr_random.lst','w+')
for i in ff:
    gg.write(i)

gg.close()


