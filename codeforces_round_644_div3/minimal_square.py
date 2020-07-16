from sys import *
t = int(stdin.readline())
while t > 0:
    a,b = map(int,stdin.readline().split())
    ans = max(max(a,b),2*min(a,b))
    print(ans * ans)
    t -= 1