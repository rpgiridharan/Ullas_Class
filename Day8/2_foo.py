# this function will work with any two parameters of any types
# as long as those parameters support the + operator between them
def f(x, y):
	print(x+y)	# duck-typing!
#f(10,20)
#f("hello", "iisc")
#f("hello", 10)	#No!

# this function will work as long as its parameter x is "callable" (with no parameters)
def f(x):
	print(x)
	x()

#f(10)# int is not callable
#f([10,20])#list is not callable
f(f(print))
#f(10,20)
# python does not support function overloading!
# the earlier definition of f is gone... because, ... def is assignment

'''
x = 10
x = 20
print(x)
'''
