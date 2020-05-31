from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr1 = list(map(int,stdin.readline().split()))
    arr2 = list(map(int,stdin.readline().split()))
    sum1 = arr1.copy()
    sum2 = arr2.copy()
    for i in range(1,n):
        sum1[i] = sum1[i] + sum1[i-1]
    for i in range(1,n):
        sum2[i] = sum2[i] + sum2[i-1]
    total = 0
    for i in range(n):
        if arr1[i] == arr2[i] and sum1[i] == sum2[i]:
            total += arr1[i]
    print(total)
    t -= 1
    