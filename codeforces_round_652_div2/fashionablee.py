from sys import *
t = int(stdin.readline())
while t > 0:
    t -= 1
    n = int(stdin.readline())
    if n % 4 == 0:
        print("YES")
    else:
        print("NO")