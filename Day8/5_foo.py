# scopes:
# Python follows the LEGB rule for scope resolution:
# Local
# Enclosing
# Global
# Builtins

# Every name in Python is resolved using the LEGB rule. 
# Given any use of a name, Python first looks up in Local scope
# then in Enclosing scopes (from inner to outer), then in Global scope
# and finally in builtins. If at any point in this search, it finds the name,
# the search stops. If at the end of all this lookup, it still did not find the name,
# then it gives NameError.

# Example: consider the following:
# print("Hello")
# To find the name print, it kicks off the LEGB rule
# Since this call happens outside of any function, so the 'L' part fails (since there is no local scope without a function).
# For the same reason, the 'E' part of the lookup fails (since there is no enclosing function).
# Since there is no assignment to a variable print at the global level, the 'G' lookup also fails.
# Now it looks up the builtins module ('B') to search for the name print. It finds it, and the search stops.


# assignment to a variable inside a fn creates a local variable
'''
x = 20
def f():
	x = 10	# this creates a local variable, which hides the global x
	print(x)
f()
print(x)
'''

'''
x = 20
def f():
	print(x)	# the fn prints whatever value x has at the time this fn is called
x = 30
f()	# the function prints the last value seen
# at the time of call, the value of x is taken
# not at the time of definition
print(x)
'''



# hoisting:
#  information about existence of local variable
# 	is hoisted to the top of the function
# if you refer to a variable which is local but not yet defined (through assignment)
#  you get an error (UnboundLocalError)
'''
x = 20
def f():
	print(x)
	x = 10
	print(x)
f()
print(x)
'''


'''
def f():
	def g():
		print("Hello")
	return g
x = f()
x()
'''

'''
x = 20
def f():
	x = 10
	print(x)
	del x
	print(x)
# unboundlocalerror:
# in this example, this does not delete hoisted info from the table
f()
print(x)
'''

'''
#x = 20
def f():
	#global x
	x = 10
	#print(x)
	global x 
	# above stmt hoists the info of existence of the global decl to the top
	# declaration announces that every reference
	# to x inside this fn will refer to the global
	# Note that it says "every reference to x", not "every reference from this point on"
	# this means that any prior reference to x before global declaration will give unboundlocalerror
	print(x)
	#x = 10
	#global y	# creates globals if they don't exist!
	#print(y)
	#y = 200
f()
print(x)
print(y)
'''



# Enclosing scope comes into play only when we have nested fns
x = 10
y = 200
def f():
	x = 20
	def g():
		x = 10
		print(x)
		def h():
			nonlocal x
			nonlocal y	#unlike global decl, does not create a new non-local variable if it doesn't already exist
			# also, does not refer to global y.
			# it only searches in enclosing functions.
			# if y is not found while searching in all enclosing scopes, gives error. Does not search up at global scope.
			x = 30
			y = 40
			print(x)
		h()
		print(x)
		print(y)
	g()
f()

