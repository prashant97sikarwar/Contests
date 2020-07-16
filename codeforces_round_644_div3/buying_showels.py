def smallestDivisor(n): 
	if (n % 2 == 0): 
		return 2; 
	i = 3; 
	while(i * i <= n): 
		if (n % i == 0): 
			return i; 
		i += 2; 

	return n; 
    
from sys import *
t= int(stdin.readline())
while t > 0:
    n,k = map(int,stdin.readline().split())
    if k >= n:
        ans = 1
    elif n % k == 0:
        ans = n//k
    else:
        dep = smallestDivisor(n)
        if dep == n:
            ans = n
        else:
            ans = dep
    print(ans)
    t -= 1