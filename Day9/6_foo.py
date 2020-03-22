def bar():
	print("Greetings")
	temp()
	print("Goodbye")

def foo():
	print("Hello")

'''
temp = foo
foo = bar
foo()
'''

# Decorator:
# the function foo has been "decorated"
# to do more than what it was originally designed
 
def decorate(f):
	def inner():
		print("Greetings")
		f()
		print("Goodbye")
	return inner

foo = decorate(foo)
# when we now call foo, we are no longer calling the original foo function
# we are really calling the inner function.
# this inner function is a closure, because it references f
#   which is a variable of the enclosing scope
# f is the original foo
# so essentially, foo has been hijacked by inner
# inner does extra functionality, and wherever it wants, it makes call 
# to original foo function via f.

foo()




