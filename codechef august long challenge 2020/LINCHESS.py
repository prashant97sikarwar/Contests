from sys import *
import math
t = int(stdin.readline())
while t > 0:
    n,k = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    ans = math.inf
    flag = 0
    for i in range(n):
        if arr[i] <= k and k % arr[i] == 0:
            dep = k//arr[i]
            if dep < ans:
                flag = 1
                ans = dep
                rt = arr[i]
    if flag == 0:
        print(-1)
    else:
        print(rt)
    t -= 1