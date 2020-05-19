# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    count = 1
    if n == 1:
        count = 1
    else:
        for i in range(1,n):
            if arr[i] <= arr[i-1]:
                count += 1
            else:
                arr[i] = arr[i-1]
        
    print(count)
    t -= 1