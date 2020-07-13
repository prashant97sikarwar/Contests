from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    ans = 0
    for i in range(1,n):
        ans += abs(arr[i] - arr[i-1]) - 1
    print(ans)
    t -= 1