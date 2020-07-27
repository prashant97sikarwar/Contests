from sys import *
def myfun(arr,n):
    for i in range(n):
        pos = arr[i]-1
        while 1 <= arr[i] <= n and arr[pos] != arr[i]:
            arr[i],arr[pos] = arr[pos],arr[i]
            pos = arr[i] -1
    for i in range(n):
        if arr[i] != i+1:
            return i+1
    return n +1
            

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
print(myfun(arr,n))