from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    dep = 0
    l = []
    for i in range(n):
        if (i + 1) != arr[i]:
            dep = -1
            l.append(i+1) 
    if dep == 0:
        ans = 0
    else:
        s = 0
        for i in range(len(l)-1):
            if l[i] != l[i+1] - 1:
                s = 1
        if s == 0:
            ans = 1
        else:
            ans = 2
    print(ans)
    t -= 1
            