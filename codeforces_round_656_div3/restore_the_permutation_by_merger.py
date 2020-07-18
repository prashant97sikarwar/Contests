from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    s = set()
    for i in range(2*n):
        if arr[i] not in s:
            s.add(arr[i])
            print(arr[i],end=' ')
        else:
            continue
    print()
    t -= 1