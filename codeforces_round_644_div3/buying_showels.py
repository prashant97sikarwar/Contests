import  math
from sys import *
t = int(stdin.readline())
while t > 0:
    n,k = map(int,stdin.readline().split())
    ans = n
    for j in range(1,int(math.sqrt(n)) + 1):
        if (n%j) == 0:
            if j <= k:
                ans = min(ans,n//j)
            if n//j <= k:
                ans = min(ans,j)
    print(ans)
    t -= 1