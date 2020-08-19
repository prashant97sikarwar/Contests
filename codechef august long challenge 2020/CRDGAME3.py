from sys import *
import math
t = int(stdin.readline())
while t > 0:
    c,r = map(int,stdin.readline().split())
    r_digit = math.ceil(r/9)
    c_digit = math.ceil(c/9)
    if r_digit <= c_digit:
        print(1,r_digit)
    else:
        print(0,c_digit)
    t -= 1