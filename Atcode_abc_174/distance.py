n,d = map(int,input().split())
count = 0
while n > 0:
    s,t = map(int,input().split())
    dep = s*s + t*t
    if dep <= (d*d):
        count += 1
    n -= 1
print(count)