# decorate the bin function so that it does not print the ugly '0b' prefix

def deco(f):
	def inner(x):
		return f(x)[2:]
	return inner
bin = deco(bin)
print(bin(10))
