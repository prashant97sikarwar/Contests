t = int(input())
while t > 0:
    n = int(input())
    ans = 0
    for i in range(n):
        s,p,v = map(int,input().split())
        lo = (p//(s+1)) * v
        ans = max(lo,ans)
    print(ans)
    t -= 1