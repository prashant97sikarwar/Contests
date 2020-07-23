from sys import *
t = int(stdin.readline())
while t > 0:
    n,r = map(int,stdin.readline().split())
    if n > r:
        print((1+r)*r//2)
    elif n <= r:
        a = n-1
        print((a+1)*a//2 + 1)
    t -= 1