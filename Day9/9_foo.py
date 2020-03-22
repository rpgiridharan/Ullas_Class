def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

def deco(f):
	memo = {}
	def optimal(n):
		if n not in memo:
			memo[n] = f(n)
		return memo[n]
	return optimal

fib = deco(fib)
fact = deco(fact)

print(fib(8))
print(fib(45))



