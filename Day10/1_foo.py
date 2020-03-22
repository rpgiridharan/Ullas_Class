# what's in a name?
def f(x):
	return x*x

# anonymous fn (lambda): is also a fn
# it is an expression
# unlike def
# what is an expression?
# anything which evaluates to something.
# another easier way to think of it is:
# anything which can appear on the RHS of an assignment statement is an expression
# a = expr
# a def statement is not an expression because 
# we cannot say: a = def f():...
# but we can say: a = lambda : ...

# lambda <parameters> : <body>
# <body> is an expression
f = lambda x : x*x
print(f(10))

#print(2+3+4)
#2+3+4

# lambdas can appear where defs cannot
a = [2+3, 4+5, lambda x:x*x]

print(a[2](10))

# at the same time, lambdas are quite restrictive compared to defs
# since body of lambda has to be just a single expression,
# therefore, we cannot have things like loops, statements, etc. which can go in defs.





