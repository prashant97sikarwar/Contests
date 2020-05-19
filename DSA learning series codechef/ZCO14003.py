n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
arr = sorted(arr)
mx =  0
for i in range(n):
    cost = arr[i]
    total = cost * (n-i)
    mx = max(mx,total)
print(mx)