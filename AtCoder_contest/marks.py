from sys import *
n,k = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
for i in range(n-k):
    if arr[i+k] > arr[i]:
        print("Yes")
    else:
        print("No")