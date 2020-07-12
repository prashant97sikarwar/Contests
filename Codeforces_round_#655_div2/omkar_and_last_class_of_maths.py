from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    ans  = 0
    for i in range(2,100000):
        if n % i == 0:
            ans = i
            break
    if ans == 0:
        ans = n
    print(n//ans,n - (n//ans))
    t -= 1