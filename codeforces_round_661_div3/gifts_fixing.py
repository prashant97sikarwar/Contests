from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    brr = list(map(int,stdin.readline().split()))
    ans  = 0
    f = min(arr)
    s = min(brr)
    for i in range(n):
        arr[i] -= f
        brr[i] -= s
    for i in range(n):
        ans += max(arr[i],brr[i])
    print(ans)
    t -= 1