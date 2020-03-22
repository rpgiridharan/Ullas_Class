# Generate all prime numbers upto n
n = 100000
# while sieve is not empty:
# 	find the smallest no
#	print that as if it was a prime
#	remove that and all its multiples
sieve = set(range(2, n+1))
while sieve:
	mymin = min(sieve)
	print(mymin)
	sieve -= set(range(mymin, n+1, mymin))
