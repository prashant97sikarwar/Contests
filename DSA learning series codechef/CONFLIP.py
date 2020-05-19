# cook your dish here
from sys import *
import math
t = int(stdin.readline())
while t > 0:
    g = int(stdin.readline())
    while g > 0:
        i,n,q = map(int,stdin.readline().split())
        ans = 0
        if (i ^ q) == 0:
            ans = int(math.floor(n/2))
        else:
            ans = int(math.ceil(n/2))
        print(ans)
        g -= 1
    t -= 1
   
            