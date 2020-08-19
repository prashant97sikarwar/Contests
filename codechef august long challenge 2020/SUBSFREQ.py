import sys
mod = 1000000007
m = 1000000007
input = sys.stdin.readline

############ ---- Input Functions ---- ############

def comb(n,r):
    m = 1000000007
    if r == 0:
        return 1
    return (((fact[n]*mod_inverse(fact[n-r]))%m)*mod_inverse(fact[r]))%m
    
def mod_inverse(n):
    m = 1000000007
    return modexpo(n,m-2)
    
def modexpo(x,n):
    m = 1000000007
    ans = 1
    while n > 0:
        if n&1:
            ans = (ans*x)%m
        x = (x*x)%m
        n >>= 1
    return ans

    
    
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
    

    
fact = [1]*500005
for i in range(2,500005):
    fact[i] = (fact[i-1]*i)%mod
    
    
t = inp()
while t > 0:
    n = inp()
    arr = inlt()
    d =  dict()
    ramram = [1] * (n+2)
    karn = [1]*(n+2)
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1

    for i in d:
        sm = 1
        for j in range(1,d[i]+1):
            sm += comb(d[i],j)
            karn[j] *= (sm%mod)
            karn[j]%= mod
            sm = sm%mod
        ramram[d[i]+1] *= sm
        ramram[d[i]+1] %= mod
    
    ml = 1
    for i in range(1,n+1):
        ml *= ramram[i]
        ml %= mod
        karn[i] = (karn[i]*ml)%mod
    for i in range(1,n+1):
        sm,res,ans = 1,0,1
        if i in d:
            pq = d[i]
        else:
            pq = -1
        for j in range(1,pq+1):
            ans = comb(pq,j)
            var = ans
            sm += ans
            sm %= mod
            karn[j] *=mod_inverse(sm)
            karn[j] %= mod
            ans *= karn[j]
            ans %= mod
            karn[j] *= (sm-var+mod)%mod
            karn[j] %= mod
            res += ans
            res %= mod
        print(res%mod,end=' ')
    print()
    t -= 1
        
    
    
    