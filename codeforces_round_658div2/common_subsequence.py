from sys import *
t = int(stdin.readline())
while t > 0:
    n,m = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    brr = list(map(int,stdin.readline().split()))
    s = set()
    flag = 0
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
    for j in range(m):
        if brr[j] in s:
            flag = 1
            print("YES")
            print(1,brr[j])
            break
    if flag == 0:
        print("NO")
    t -= 1