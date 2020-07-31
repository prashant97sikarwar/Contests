from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    if n >30:
        print("YES")
        if n-30 == 6:
            print(6,10,15,n-31)
        elif n-30 == 10:
            print(6,10,15,n-31)
        elif n-30 == 14:
            print(6,10,21,n-37)
        else:
            print(6,10,14,n-30)
    else:
        print("NO")
    t -= 1