# closure:
# Happens only when all three of the following are satisfied:
# 1. you have a nested fn.
# 2. you should return that nested fn.
# 3. the nested fn should access some enclosing variable

# What is closure?
# a nested function "remembers" the environment in which it was called,
# i.e., it retains a reference to enclosing variables that it references.

# when you encounter a nested def,
# compiler scans through the body of this nested def
# to check if it has accessed an enclosing variable
# if there is an enclosing variable, then this enclosing variable
# is retained in a special frame
# when this nested fn is returned, this special frame is not destroyed
# and hence this local variable of the enclosing variable is not destroyed.
# think of this as an extension to concept of Reference Count
# we know that an object is not garbage collected, until
#  its reference count becoems zero
# so when we have a closure,
# the nested fn gets a reference to the outer enclosing variable
# as a result of this, the enclosing variable 
#   is not destroyed upon exit, even though it is local variable!
# so this local variable is destroyed only when the nested fn is destroyed




def f():
	x = 10
	def g():
		print(x)
		print("Hello")
	#print(x)
	x = 40
	return g

x = 20
y = f()
x = 30
y()
