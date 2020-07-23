from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    if n % 2 == 0:
        ans = n//2
    else:
        ans = n//2 + 1
    print(ans)
    t -= 1