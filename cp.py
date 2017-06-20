# -*- coding:utf-8 -*-
import random
import time

#注数
try:
    zs = input('please input how many you want(integer):')
except:
    zs = 1

i = 0
strssqs = []
while i<zs:
    #红球  sample方法从集合中取样（集合，长度）
    hq = random.sample(range(1,34),6)
    hq.sort()

    #排除出现三个连续数字的情况
    l1 = hq[0:3]
    l2 = hq[1:4]
    l3 = hq[2:5]
    l4 = hq[3:]
    r1 = (l1[2]-l1[1])-(l1[1]-l1[0])
    r2 = (l2[2]-l2[1])-(l2[1]-l2[0])
    r3 = (l3[2]-l3[1])-(l3[1]-l3[0])
    r4 = (l4[2]-l4[1])-(l4[1]-l4[0])
    r = r1*r2*r3*r4
    if r!=0:
        #蓝球
        lq = random.sample(range(1,17),1)

        #一注双色球
        ssq = str(hq + lq)
        strssqs.append(ssq)
        i += 1
    else:
        continue

change_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f = file('cp.txt','a+')

try:
    f.write('\n')
    f.write(change_time) 
    f.write('\n')
    for j in strssqs:
        f.write(j)
        f.write('\n')
finally:
    f.close()

    


