# Generate all prime numbers upto n
n = 100000
import math
for i in range(2, n+1):   # check if i is prime
	j = 2
	is_prime = True
	a = math.sqrt(i)
	while is_prime and j <= a:
		if i % j == 0:
			is_prime = False
		j += 1
	if is_prime:
		print(i)

