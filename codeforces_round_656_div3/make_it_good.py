from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    if arr == sorted(arr):
        ans = 0
    elif arr == sorted(arr, reverse=True):
        ans = 0
    else:
        count = 0
        for i in range(n-1,-1,0):
            if arr[i] <= arr[i-1]:
                count += 1
            else:
                j = i
                break
        for i in range(i,-1,0):
            if arr[i] >= arr[i+1]:
                count += 1
            else:
                break
        ans = n - (count + 1)
    print(ans)
    t -=1