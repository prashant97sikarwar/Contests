from sys import *
t = int(stdin.readline())
while t > 0:
    n,k = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    d = dict()
    d[0] = 0
    for i in arr:
        des = (k-i)%k
        if des:
            if des not in d:
                d[des] = des + 1
            else:
                d[des] += k
    print(max(d.values()))
    t -= 1