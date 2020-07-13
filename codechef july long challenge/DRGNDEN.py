from sys import *
n,q = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
brr = list(map(int,stdin.readline().split()))
for i in range(q):
    p,m,n = map(int,stdin.readline().split())
    if p == 1:
        m-=1
        brr[m] = n
    else:
        if m == n:
            rt = brr[n-1]
        else:
            m-=1
            n -= 1
            if arr[n] >= arr[m]:
                rt = -1
            else:
                if m < n:
                    ans = brr[n]
                    dep = n
                    while n > m:
                        if arr[n-1] > arr[m]:
                            ans = -1
                            break
                        if arr[dep] < arr[n-1]:
                            ans += brr[n-1]
                            dep = n-1
                            n -= 1
                        else:
                            n -= 1
                    if dep == m:
                        rt = ans
                    else:
                        rt = -1
                elif m == n:
                    rt = brr[m]
                elif m > n:
                    ans = brr[n]
                    dep = n
                    while n < m:
                        if arr[n+1] > arr[m]:
                            ans = -1
                            break
                        if arr[n+1] > arr[dep]:
                            ans += brr[n+1]
                            dep = n+1
                            n += 1
                        else:
                            n += 1
                    if dep == m:
                        rt = ans
                    else:
                        rt = -1
        print(rt)
    
                        
            
    