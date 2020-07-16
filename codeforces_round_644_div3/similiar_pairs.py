from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    arr.sort()
    odd = 0
    even = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd % 2 == 0 and even % 2 == 0:
        ans = "YES"
        print(ans)
    else:
        flag = 0
        for i in range(1,n):
            if arr[i] - arr[i-1] == 1:
                flag = 1
                break
        if flag == 0:
            print("NO")
        else:
            print("YES")
    t -= 1
    