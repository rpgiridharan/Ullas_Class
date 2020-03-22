# Generate all prime numbers upto n
n = 1000000
# while sieve is not empty:
# 	find the smallest no
#	print that as if it was a prime
#	remove that and all its multiples
a = [True] * (n+1)
for i in range(2,n+1):
	if a[i]:
		for j in range(i+i, n+1, i):
			a[j] = False

for i in range(2, n+1):
	if a[i]:
		print(i)
