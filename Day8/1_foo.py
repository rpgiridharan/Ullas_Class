# fn:
#	reuse (not the main goal)
#	process abstraction

# salient features:
# declaration 
# definition
# calling
# recursion
# returns (multiple)
# callback (handle to a function)
# if you can use that handle in multiple contexts
# parameters
# what can be the parameters?
#	how many? types?
# parameter passing mechanism
# scopes
# overloading
# multiple functions can have same name/signature
# "classes" -> can functions be part of them?

# declaration of fn:
# void f();
# no declaration in python
# because no type-declaration of parameters or return type

# keyword def is used to define a function
'''
f()	# error! 

def f():
	print("Hello")

f()
'''
# General syntax of defining a function
# def fn-name ( <parameters>):
#	stmts...

# def is an assignment
# def f(): ...
# f = <code of the fn>
# So, def can appear in any place that an assignment can

import sys
print(sys.getrefcount(10))
def f():
	x = 10
	print(sys.getrefcount(10))
	def g():	# nested fn
		print("Hello")
	g()

f()
print(sys.getrefcount(10))

# if a fn assigns to a variable
#  that variable becomes a local var to that fn
# all local variables are removed upon fn exit*
# * - except in some bizarre cases

#print(x)











