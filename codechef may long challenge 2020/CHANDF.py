from sys import *
t = int(stdin.readline())
while t > 0:
    x,y,l,r = map(int,stdin.readline().split())
    if x == 0 or y == 0:
        ans = 0
    else:
        ans = x | y
    print(ans)
    t -= 1