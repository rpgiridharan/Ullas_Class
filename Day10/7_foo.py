# variable-number of keyword parameters

def f(*a):
	print(a)

f(10,20)

def f(a, b=0, *c, **d):
	pass

f(10, 20, 0, 40, b=400)


# the following collects all the keyword parameters (in call) into a single dictionary called kw.
# experiment: can you have default value for this **kw?
# 		can you have *parameter and **parameters together
# 		can you have two **parameters in a single def?

def f(**kw):
	print(kw)
f(a=10, b=20, c=30)

def f(a, b, c):
	pass


# **parameter can appear in call as well.
# works like mirror image at def.
# that is, unpacks the dictionary into key-value pairs
# each key-value pair becomes a keyword parameter passed to the function
f(**({'a':10, 'b':20, 'c':30}))
