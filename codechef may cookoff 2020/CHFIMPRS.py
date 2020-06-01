
T = int(input())
for _ in range(T):
    n, m = list(map(int, input().split()))
	A = []
	hashmap = {}
	for i in range(n):
		temp = list(map(int ,input().split()))
		A.append(temp)
		for j in temp:
			if j in hashmap:
				hashmap[j] += 1
			else:
				hashmap[j] = 1
	uniq = 0
	u = []
	for i in hashmap:
		if hashmap[i] % 2 != 0:
			uniq += 1
			u.append(i)
			hashmap[i] -= 1
	k = m % 2
	no_of_uni = k * n
	if no_of_uni < uniq or (abs(no_of_uni - uniq)) % 2 != 0:
		print(-1)
		continue


	mid = m // 2
	val = m // 2
	if m % 2 == 0:
		mid = -1
		val = m // 2 + 1
	t = 0
	for key in hashmap:
		while hashmap[key]:
			if len(u) == no_of_uni:
				break
			u.append(key)
			hashmap[key] -= 1
		if len(u) == no_of_uni:
			break
	i, j = 0, 0
	for key in hashmap:
		while hashmap[key]:
			A[i][j] = key
			A[i][m-j-1] = key
			j += 1
			if j == m // 2:
				j = 0
				i += 1
			hashmap[key] -= 2


	if mid != -1:
		for i in range(n):
			A[i][mid] = u[t]
			t += 1
	for i in A:
		for j in range(m):
			if j == m-1:
				print(i[j])
			else:
				print(i[j], end = " ")
