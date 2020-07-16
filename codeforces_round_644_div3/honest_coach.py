from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    arr.sort()
    mn = abs(arr[1] - arr[0])
    for i in range(2,n):
        des = abs(arr[i] - arr[i-1])
        mn = min(mn,des)
    print(mn)
    t -= 1