#-*- conding=utf-8 -*-
i=0
for i in range(101):
    if i%10==0:
        continue
    if i%7==0:
        continue
    if i//10===7:
        continue
    print(i)
