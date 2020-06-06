from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    n5 = 0
    n10 = 0
    n15 = 0
    flag = 0
    for i in range(n):
        if arr[i] == 5:
            n5 += 1
        elif arr[i] == 10 and n5 > 0 :
            n10 += 1
            n5 -= 1
        elif (arr[i] == 15) and ((n5 > 1) or (n10 > 0)):
            n15 += 1
            if n10 > 0:
                n10 -= 1
            elif n5 > 1:
                n5 -= 2
        else:
            flag = 1
            break
    if flag == 0:
        print("YES")
    if flag == 1:
        print("NO")
    t -= 1
                