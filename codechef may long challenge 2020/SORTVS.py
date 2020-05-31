from sys import *
def despo(arr): 
    n = len(arr) 
    position = [*enumerate(arr)] 
    position.sort(key = lambda x:x[1]) 
    arjun = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if arjun[i] or position[i][0] == i: 
            continue
        chakra = 0
        j = i 
        while not arjun[j]: 
            arjun[j] = True
            j = position[j][0] 
            chakra += 1
        if chakra > 0: 
            ans += (chakra - 1) 
    return ans 

t = int(stdin.readline())
while t > 0:
    n,m = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    for i in range(m):
        x,y = map(int,stdin.readline().split())
    print(despo(arr))
    t -= 1
    