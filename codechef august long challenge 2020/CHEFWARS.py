from sys import *
t = int(stdin.readline())
while t > 0:
    h,p = map(int,stdin.readline().split())
    ans = 0
    while p > 0:
        ans += p
        p= p//2
    if ans >= h:
        print(1)
    else:
        print(0)
    t -= 1