from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    s = set()
    count = 0
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
            count += 1
        else:
            continue
    print(count)
    t -= 1