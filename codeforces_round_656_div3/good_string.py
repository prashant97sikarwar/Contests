from sys import *
def ans(l,r,c):
    if l == r:
        if s[l] == c:
            return 0
        else:
            return 1
    mid = l + (r-l+1)//2
    count = 0
    for i in range(l,mid):
        if s[i] != c:
            count += 1
            
    ans1 = count + ans(mid,r,chr(ord(c)+1))
    count = 0
    for i in range(mid,r+1):
        if s[i] != c:
            count += 1
    ans2 = count + ans(l,mid-1,chr(ord(c)+1)) 
    return min(ans1,ans2)
    
    

t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    s = stdin.readline()
    print(ans(0,n-1,'a'))
    t -= 1