from sys import *
t = int(stdin.readline())
while t > 0:
    x,y,n = map(int,stdin.readline().split())
    de = n % x
    if de == y:
        ans = n
    elif de > y:
        ans = n - (de - y)
    elif de < y:
        ans = n - de - x + y
    print(ans)
    t -= 1