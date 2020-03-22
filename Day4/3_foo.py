# Generate all prime numbers upto n
n = 100000
for i in range(2, n+1):   # check if i is prime
	count = 0
	for j in range(2, i):
		if i % j == 0:
			count += 1
	if count == 0:
		print(i)

