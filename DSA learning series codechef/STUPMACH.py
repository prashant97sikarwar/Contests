from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    l = []
    l.append(arr[0])
    total = arr[0]
    mn = arr[0]
    for i in range(1,n):
        if arr[i] <= l[-1]:
            mn = arr[i]
            l.append(arr[i])
            total += arr[i]
        if arr[i] > l[-1]:
            total += mn
    print(total)
    t -= 1