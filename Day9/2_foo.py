# callback:
#  you pass a fn to another as parameter
#  and call it
def f(g):
	g()


#x is a list
def squareElements(x):
	res = []
	for i in x:
		res.append(i*i)
	return res

a = [10,20,30]
print(squareElements(a))


def cubeElements(x):
	res = []
	for i in x:
		res.append(i*i*i)
	return res

print(cubeElements(a))



def fn(x, g):
	res = []
	for i in x:
		res.append(g(i))

	return res

def sq(x):
	return x*x

print(fn(a, sq))

