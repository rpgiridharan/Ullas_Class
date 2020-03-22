# parameter passing: ?
#  pass by assignment!
# parameters are really passed by assignment

def f(x):
	x = 20

a = 10
f(a)
print(a)


def g(x):
	#x[0] = 100
	x = [10000, 2000]

a = [10,20]
g(a)
print(a)
