from sys import *
a,b,c = map(int,stdin.readline().split())
k = int(stdin.readline())
while b <= a:
    b = b*2
    k -= 1
while c <= b:
    c = c*2
    k -= 1
if k < 0:
    print("No")
else:
    print("Yes")