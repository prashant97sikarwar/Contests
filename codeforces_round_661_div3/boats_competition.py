from collections import defaultdict
def findPairs(arr, size): 
    Map = defaultdict(list)
    for i in range(0, size - 1):  
        for j in range(i + 1, size):
            flag = 0
            Sum = arr[i] + arr[j] 
            if Sum in Map:
                for pair in Map[Sum]:  
                    m, n = pair 
                    if ((m == i or n == j) or (n == i or m == j)):
                        flag = 1
                        break
                if flag == 0:
                    Map[Sum].append((i,j))
            if Sum not in Map: 
                Map[Sum].append((i, j)) 
    
    mx = 0
    for i in Map:
        mx = max(mx,len(Map[i]))
    return mx

from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    print(findPairs(arr,n))
    t -= 1
    