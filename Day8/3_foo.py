def f():
	return 10

x = f()
print(x)

def g():
	print("Hello")


# every function in python has a default return: None
y = g	#Nothing sacred about function name - it is just another variable
print(y) #Above assignment makes y also refer to function object
y()	# Thus, y is now callable.

# Advantage of not having a return type declaration:
# function can return multiple types along different branches of execution
# which you can't do in C
def f(x):
	if x > 10:
		return 100
	else:
		return "iisc", [10,20,30]

print(f(10))




