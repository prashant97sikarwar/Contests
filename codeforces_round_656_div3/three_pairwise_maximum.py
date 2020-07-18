from sys import *
t =  int(stdin.readline())
while t > 0:
    x,y,z = map(int,stdin.readline().split())
    if x == y and y == z:
        print("YES")
        print(x,x,x)
    elif x == y and z < y:
        print("YES")
        print(x,z,z)
    elif y == z and x < y:
        print("YES")
        print(y,x,x)
        
    elif x == z and y < x:
        print("YES")
        print(x,y,y)
    else:
        print("NO")
    t -= 1