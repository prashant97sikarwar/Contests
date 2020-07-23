def solution(arr,k,n):
    s = set()
    for i in range(n):
        if k - arr[i] not in s:
            s.add(arr[i])
        else:
            return True
    return False

t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr =  list(map(int,input().split()))
    if solution(arr,k,n):
        print("YES")
    else:
        print("NO")
    t -= 1