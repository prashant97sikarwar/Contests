from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    flag = 0
    for i in range(1,n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            flag = 1
            break
    if flag == 1:
        print("YES")
        print(i,i+1,i+2)
    else:
        print("NO")
    t -= 1