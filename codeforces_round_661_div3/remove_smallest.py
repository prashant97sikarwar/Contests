from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    arr.sort()
    flag = 0
    if n == 1:
        print("YES")
    else:
        for i in range(1,n):
            if abs(arr[i] - arr[i-1])  > 1:
                print("NO")
                flag = 1
                break
        if flag == 0:
            print("Yes")
    t -= 1 