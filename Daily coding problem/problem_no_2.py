t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    left = [None] * n
    right = [None] * n
    left[0] = 1
    right[n-1] = 1
    for i in range(n-1):
        left[i+1] = left[i] * arr[i]
    for j in range(n-1,0,-1):
        right[j-1] = right[j] * arr[j]
    for i in range(n):
        arr[i] = left[i] * right[i]
    print(arr)
    t -= 1
        
    