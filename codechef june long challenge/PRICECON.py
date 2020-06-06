from sys import *
t = int(stdin.readline())
while t > 0:
    n,k = map(int,stdin.readline().split())
    arr = list(map(int,input().split()))
    dep = sum(arr)
    total = 0
    for i in range(n):
        if arr[i] > k:
            total += k
        else:
            total += arr[i]
    ans = dep - total
    print(ans)
    t -= 1