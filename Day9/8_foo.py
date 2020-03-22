# decorator:
# we wish to extend the functionality of a fn

def embellish(f):	# f is the function that we wish to decorate
	# inner is the function that will get called when we call the original function which we have decorated. So, inner must ideally have the same number of parameters as the original (unless, you wish to change the interface itself for the client!)
	def inner(a, b): 
		if b != 0:
			return f(a, b)
		else:
			return None

	return inner

@embellish
def divide(a, b):
	return a/b

#divide = embellish(divide)	#above @ syntax is syntactic sugar for this line!


#divide = embellish(divide)
print(divide(10,  2))
print(divide(10,0))
