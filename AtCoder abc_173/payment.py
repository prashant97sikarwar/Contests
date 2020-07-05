import math
n = int(input())
ans = math.ceil(n/1000)
dep = ans * 1000 - n
print(dep)