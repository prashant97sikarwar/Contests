from sys import *
t = int(stdin.readline())
while t > 0:
    n,x = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    arr.sort(reverse=True)
    count = 0
    de = 1
    for i in arr:
        if i * de >= x:
            count += 1
            de = 0
        de += 1
    print(count)
    t -= 1