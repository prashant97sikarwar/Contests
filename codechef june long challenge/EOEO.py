from sys import *
t = int(stdin.readline())
while t > 0:
    ts = int(stdin.readline())
    sm = ts
    if ts % 2 == 1:
        ans = ts//2
    else:
        count = 0
        while ts % 2 == 0:
            ts = ts//2
            count += 1
        des = 2 << count
        pic = sm//des
        ans = pic
    print(ans)
    t -= 1