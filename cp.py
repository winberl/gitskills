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

    #蓝球
    lq = random.sample(range(1,17),1)

    #一注双色球
    ssq = str(hq + lq)
    strssqs.append(ssq)
    i += 1

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

    


