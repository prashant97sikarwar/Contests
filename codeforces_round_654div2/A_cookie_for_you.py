from sys import *
t = int(stdin.readline())
while t > 0:
    t-=1
    a,b,n,m = map(int,stdin.readline().split())
    if a > b:
        a,b = b,a
    if a < m:
        print("No")
        continue
    if a + b < n + m:
        print("No")
        continue
    print("Yes")