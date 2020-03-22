# decorate the dir function so that it returns back a list of all names that don't begin with double underscore


# list comprehension
# [o/p expr for var in iterable if ...]

def deco(f):
	def inner(x):
		return [names for names in f(x) if names[0] != "_"]
	return inner

dir = deco(dir)
print(dir(list))
