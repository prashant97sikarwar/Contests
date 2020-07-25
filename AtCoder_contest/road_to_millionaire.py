import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
total = 1000
for i in range(n-1):
    if arr[i] < arr[i+1]:
        stocks = total // arr[i]
        total += (arr[i+1] - arr[i]) * stocks
print(total)