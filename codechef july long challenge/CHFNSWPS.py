from collections import Counter
from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    brr = list(map(int,stdin.readline().split()))
    arr.sort()
    brr.sort()
    flag = 0
    if arr == brr:
        ans =  0
        print(ans)
    else:
        a1 = {}
        a2 = {}
        l = []
        for i in range(n):
            if arr[i] not in a1:
                a1[arr[i]] = 1
                a2[arr[i]] = 0
            else:
                a1[arr[i]] += 1
        for i in range(n):
            if brr[i] not in a2:
                a2[brr[i]] = 1
                if brr[i] not in a1:
                    a1[brr[i]] = 0
            else:
                a2[brr[i]] += 1
        for i in a1:
            if(a1[i] + a2[i]) % 2 == 1:
                ans = -1
                print(ans)
                flag = 1
                break
            elif a1[i] != a2[i]:
                k= (a1[i] + a2[i])/2
                y = int(abs(a1[i] - k))
                for j in range(y):
                    l.append(i)
        if flag == 0:
            l.sort()
            ans = 0
            mn = min(arr[0],brr[0])
            for i in range(len(l)//2):
                if l[i] <= 2*mn:
                    ans += l[i]
                else:
                    ans += 2*mn
            print(ans)
    t -= 1