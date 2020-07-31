from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    if n % 4 == 0:
        zero = n//4
        ans = (n-zero) *  '9' + zero*'8'
    else:
        zero = n//4
        ans = (n-zero-1) * '9' + '8' + zero*'8'
    print(ans)
    t -= 1